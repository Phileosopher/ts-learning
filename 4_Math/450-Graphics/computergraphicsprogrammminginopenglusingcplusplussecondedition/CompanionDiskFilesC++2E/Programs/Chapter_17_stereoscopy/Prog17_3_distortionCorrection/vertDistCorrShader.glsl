#version 430

layout (location=0) in vec3 position;
uniform int leftRight;
uniform float winSizeX;
uniform float winSizeY;
layout (binding=0) uniform sampler2D lensTex;

void main(void)
{	gl_Position = vec4(position, 1.0);
} 
