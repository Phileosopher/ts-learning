#version 430

layout (location=0) in vec3 position;
layout (location=1) in vec2 texCoord;
layout (location=2) in vec3 vertNormal;
out vec3 varyingNormal;
out vec3 varyingLightDir;
out vec3 varyingVertPos;
out vec2 tc;

layout (binding=0) uniform sampler3D noiseTex;

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

void main(void)
{	varyingVertPos = (mv_matrix * vec4(position,1.0)).xyz;
	varyingLightDir = light.position - varyingVertPos;
	varyingNormal = (norm_matrix * vec4(vertNormal,1.0)).xyz;

	gl_Position = proj_matrix * mv_matrix * vec4(position,1.0);
	tc = texCoord;
} 
