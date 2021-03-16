#version 430

layout (location=0) in vec3 position;
layout (location=1) in vec2 texCoord;
layout (location=2) in vec3 vertNormal;
out vec3 varyingNormal;
out vec3 varyingLightDir;
out vec3 varyingVertPos;
out vec2 tc;
out vec4 glp;

layout (binding=0) uniform sampler2D reflectTex;
layout (binding=1) uniform sampler2D refractTex;
layout (binding=2) uniform sampler3D noiseTex;

struct PositionalLight
{	vec4 ambient;
	vec4 diffuse;
	vec4 specular;
	vec3 position;
};
struct Material
{	vec4 ambient;
	vec4 diffuse;
	vec4 specular;
	float shininess;
};

uniform vec4 globalAmbient;
uniform PositionalLight light;
uniform Material material;
uniform mat4 mv_matrix;
uniform mat4 proj_matrix;
uniform mat4 norm_matrix;
uniform int isAbove;
uniform float depthOffset;

void main(void)
{	varyingVertPos = (mv_matrix * vec4(position,1.0)).xyz;
	varyingLightDir = light.position - varyingVertPos;
	varyingNormal = (norm_matrix * vec4(vertNormal,1.0)).xyz;

	tc = texCoord;
	glp = proj_matrix * mv_matrix * vec4(position,1.0);
	gl_Position = glp;
}
