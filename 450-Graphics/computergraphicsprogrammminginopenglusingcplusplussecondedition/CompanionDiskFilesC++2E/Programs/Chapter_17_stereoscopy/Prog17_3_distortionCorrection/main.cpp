#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <SOIL2/soil2.h>
#include <string>
#include <iostream>
#include <fstream>
#include <glm/gtc/type_ptr.hpp> // glm::value_ptr
#include <glm/gtc/matrix_transform.hpp> // glm::translate, glm::rotate, glm::scale, glm::perspective
#include "ImportedModel.h"
#include "Utils.h"
using namespace std;

float toRadians(float degrees) { return (degrees * 2.0f * 3.14159f) / 360.0f; }

#define numVAOs 1
#define numVBOs 4

float cameraX, cameraY, cameraZ;
float gndLocX, gndLocY, gndLocZ;
GLuint renderingProgram, distCorrectionProgram;
GLuint vao[numVAOs];
GLuint vbo[numVBOs];

// variable allocation for display
GLuint mvLoc, projLoc, leftRightLoc, sizeXLoc, sizeYLoc;
int width, height;
float aspect;
glm::mat4 pMat, vMat, mMat, mvMat;
float rotAmt = 0.0f;

ImportedModel ground("grid.obj");
int numGroundVertices;

GLuint heightMap;
GLuint rockyTexture;

// VR stuff
float IOD = 0.01f;
float near = 0.01f;
float far = 100.0f;
int sizeX = 1920, sizeY = 1080;
GLuint leftRightBuffer, leftRightTexture;

void setupVertices(void) {
	numGroundVertices = ground.getNumVertices();
	std::vector<glm::vec3> vert = ground.getVertices();
	std::vector<glm::vec2> tex = ground.getTextureCoords();
	std::vector<glm::vec3> norm = ground.getNormals();

	std::vector<float> pvalues;
	std::vector<float> tvalues;
	std::vector<float> nvalues;

	for (int i = 0; i < numGroundVertices; i++) {
		pvalues.push_back((vert[i]).x);
		pvalues.push_back((vert[i]).y);
		pvalues.push_back((vert[i]).z);
		tvalues.push_back((tex[i]).x);
		tvalues.push_back((tex[i]).y);
		nvalues.push_back((norm[i]).x);
		nvalues.push_back((norm[i]).y);
		nvalues.push_back((norm[i]).z);
	}

	glGenVertexArrays(1, vao);
	glBindVertexArray(vao[0]);
	glGenBuffers(numVBOs, vbo);

	glBindBuffer(GL_ARRAY_BUFFER, vbo[0]);
	glBufferData(GL_ARRAY_BUFFER, pvalues.size() * 4, &pvalues[0], GL_STATIC_DRAW);

	glBindBuffer(GL_ARRAY_BUFFER, vbo[1]);
	glBufferData(GL_ARRAY_BUFFER, tvalues.size() * 4, &tvalues[0], GL_STATIC_DRAW);

	glBindBuffer(GL_ARRAY_BUFFER, vbo[2]);
	glBufferData(GL_ARRAY_BUFFER, nvalues.size() * 4, &nvalues[0], GL_STATIC_DRAW);

	float lensQuad[18] = {
		-1.0, 1.0, 0.0,  -1.0, -1.0, 0.0,  1.0, 1.0, 0.0,
		 1.0, 1.0, 0.0,  -1.0, -1.0, 0.0,  1.0, -1.0, 0.0
	};
	glBindBuffer(GL_ARRAY_BUFFER, vbo[3]);
	glBufferData(GL_ARRAY_BUFFER, sizeof(lensQuad), &lensQuad[0], GL_STATIC_DRAW);
}

void setupLeftRightBuffer(GLFWwindow* window) {
	GLuint bufferId[1];
	glGenBuffers(1, bufferId);
	glfwGetFramebufferSize(window, &width, &height);
	glGenFramebuffers(1, bufferId);
	leftRightBuffer = bufferId[0];
	glBindFramebuffer(GL_FRAMEBUFFER, leftRightBuffer);
	glGenTextures(1, bufferId);
	leftRightTexture = bufferId[0];
	glBindTexture(GL_TEXTURE_2D, leftRightTexture);
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width / 2, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, NULL);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER);
	float blackColor[4] = { 0.0f, 0.0f, 0.0f, 1.0f };
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR, *blackColor);

	glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, leftRightTexture, 0);
	glDrawBuffer(GL_COLOR_ATTACHMENT0);
	glGenTextures(1, bufferId);
	glBindTexture(GL_TEXTURE_2D, bufferId[0]);
	glTexImage2D(GL_TEXTURE_2D, 0, GL_DEPTH_COMPONENT24, width / 2, height, 0, GL_DEPTH_COMPONENT, GL_FLOAT, NULL);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	glFramebufferTexture2D(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_TEXTURE_2D, bufferId[0], 0);
}

void init(GLFWwindow* window) {
	renderingProgram = Utils::createShaderProgram("vertShader.glsl", "fragShader.glsl");
	distCorrectionProgram = Utils::createShaderProgram("vertDistCorrShader.glsl", "fragDistCorrShader.glsl");
	cameraX = 0.0f; cameraY = 0.13f; cameraZ = 0.3f;
	gndLocX = 0.0f; gndLocY = 0.05f; gndLocZ = 0.0f;

	glfwGetFramebufferSize(window, &width, &height);
	aspect = (float)width / (float)height;
	pMat = glm::perspective(1.0472f, aspect, near, far);

	setupVertices();

	rockyTexture = Utils::loadTexture("bkgd1.jpg");
	heightMap = Utils::loadTexture("height.jpg");
}

void display(GLFWwindow* window, double currentTime, int leftRight) {
	glUseProgram(renderingProgram);

	mvLoc = glGetUniformLocation(renderingProgram, "mv_matrix");
	projLoc = glGetUniformLocation(renderingProgram, "proj_matrix");

	vMat = glm::translate(glm::mat4(1.0f), glm::vec3(-(cameraX + leftRight * IOD / 2.0f), -cameraY, -cameraZ));
	mMat = glm::translate(glm::mat4(1.0f), glm::vec3(gndLocX, gndLocY, gndLocZ));
	mMat = glm::rotate(mMat, toRadians(10.0f), glm::vec3(1.0f, 0.0f, 0.0f));
	mMat = glm::rotate(mMat, rotAmt, glm::vec3(0.0f, 1.0f, 0.0f));
	mvMat = vMat * mMat;
	rotAmt += 0.001f;

	glUniformMatrix4fv(mvLoc, 1, GL_FALSE, glm::value_ptr(mvMat));
	glUniformMatrix4fv(projLoc, 1, GL_FALSE, glm::value_ptr(pMat));

	glBindBuffer(GL_ARRAY_BUFFER, vbo[0]);
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0);
	glEnableVertexAttribArray(0);

	glBindBuffer(GL_ARRAY_BUFFER, vbo[1]);
	glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 0, 0);
	glEnableVertexAttribArray(1);

	glBindBuffer(GL_ARRAY_BUFFER, vbo[2]);
	glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 0, 0);
	glEnableVertexAttribArray(2);

	glActiveTexture(GL_TEXTURE0);
	glBindTexture(GL_TEXTURE_2D, rockyTexture);

	glActiveTexture(GL_TEXTURE1);
	glBindTexture(GL_TEXTURE_2D, heightMap);

	glEnable(GL_CULL_FACE);
	glFrontFace(GL_CCW);
	glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_LEQUAL);

	glDrawArrays(GL_TRIANGLES, 0, numGroundVertices);
}

void window_size_callback(GLFWwindow* win, int newWidth, int newHeight) {
	aspect = (float)newWidth / (float)newHeight;
	glViewport(0, 0, newWidth, newHeight);
	pMat = glm::perspective(1.0472f, aspect, near, far);
}

void copyFrameBufferToViewport(GLFWwindow* window, int leftRight) {
	glUseProgram(distCorrectionProgram);
	leftRightLoc = glGetUniformLocation(distCorrectionProgram, "leftRight");
	sizeXLoc = glGetUniformLocation(distCorrectionProgram, "winSizeX");
	sizeYLoc = glGetUniformLocation(distCorrectionProgram, "winSizeY");
	glUniform1i(leftRightLoc, leftRight);
	glUniform1f(sizeXLoc, (float)sizeX/2.0f);
	glUniform1f(sizeYLoc, (float)sizeY);

	glBindBuffer(GL_ARRAY_BUFFER, vbo[3]);
	glVertexAttribPointer(0, 3, GL_FLOAT, false, 0, 0);
	glEnableVertexAttribArray(0);
	glActiveTexture(GL_TEXTURE0);
	glBindTexture(GL_TEXTURE_2D, leftRightTexture);
	glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_LEQUAL);
	glDrawArrays(GL_TRIANGLES, 0, 6);
}

void clearDisplay() {
	glClearColor(0, 0, 0, 1);
	glBindFramebuffer(GL_FRAMEBUFFER, 0);
	glClear(GL_DEPTH_BUFFER_BIT);
	glClear(GL_COLOR_BUFFER_BIT);
}

void clearBuffer() {
	glClearColor(0.7f, 0.8f, 0.9f, 1.0f);
	glBindFramebuffer(GL_FRAMEBUFFER, leftRightBuffer);
	glClear(GL_DEPTH_BUFFER_BIT);
	glClear(GL_COLOR_BUFFER_BIT);
}

int main(void) {
	if (!glfwInit()) { exit(EXIT_FAILURE); }
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	GLFWwindow* window = glfwCreateWindow(sizeX, sizeY, "Chapter 17 - program 3", NULL, NULL);
	glfwMakeContextCurrent(window);
	if (glewInit() != GLEW_OK) { exit(EXIT_FAILURE); }
	glfwSwapInterval(1);

	glfwSetWindowSizeCallback(window, window_size_callback);

	init(window);

	setupLeftRightBuffer(window);

	while (!glfwWindowShouldClose(window)) {
		clearDisplay();

		// draw left viewport
		clearBuffer();
		glBindFramebuffer(GL_FRAMEBUFFER, leftRightBuffer);
		glViewport(0, 0, sizeX/2, sizeY);
		display(window, glfwGetTime(), -1);
		// transfer it to the screen
		glBindFramebuffer(GL_FRAMEBUFFER, 0);
		glViewport(0, 0, sizeX/2, sizeY);
		copyFrameBufferToViewport(window, 0.0f);

		// draw right viewport
		clearBuffer();
		glBindFramebuffer(GL_FRAMEBUFFER, leftRightBuffer);
		glViewport(0, 0, sizeX/2, sizeY);
		display(window, glfwGetTime(), 1);
		// transfer it to the screen
		glBindFramebuffer(GL_FRAMEBUFFER, 0);
		glViewport(sizeX/2, 0, sizeX/2, sizeY);
		copyFrameBufferToViewport(window, 1.0f);

		glViewport(0, 0, sizeX, sizeY);
		glfwSwapBuffers(window);
		glfwPollEvents();
	}

	glfwDestroyWindow(window);
	glfwTerminate();
	exit(EXIT_SUCCESS);
}