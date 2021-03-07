#version 430

out vec4 fragColor;

uniform int leftRight;  // -1 for left, +1 for right
uniform float winSizeX;
uniform float winSizeY;
layout (binding=0) uniform sampler2D lensTex; // previously rendered framebuffer

void main(void)
{	float K1 = -0.55;  // distortion parameters for Google cardboard
	float K2 = 0.34;
	
	// compute the location in the half window scaled to (-0.5 ... +0.5) with (0,0) center
	float xd = (gl_FragCoord.x - winSizeX*leftRight) / winSizeX - 0.5;
	float yd = gl_FragCoord.y / winSizeY - 0.5;

	// compute the distance to the center of the half window
	float ru = sqrt(pow(xd,2.0) + pow(yd,2.0));
	
	// tune conversion from screen units  to physical millimeters
	float mmRatio = 1.3;  // ratio of ru/d where d is distance to lens
	float rn = ru * mmRatio;
	
	// compute the undistorted corresponding location
	float distortionFactor = 1+ K1 * pow(rn,2.0f) + K2 * pow(rn,4.0f);
	float xu = xd / distortionFactor;
	float yu = yd / distortionFactor;
	
	// move the resulting point by (+0.5, +0.5) to convert to texture space
	fragColor = texture(lensTex, vec2(xu+0.5,yu+0.5));
}
