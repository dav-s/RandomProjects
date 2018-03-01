uniform float time;
varying vec3 normalInterp;
varying vec4 worldPos;

float vertexHeight(float x, float z, vec2 direction, float freq, float t, float speed, float amplitude) {
	return amplitude * sin(dot(direction, vec2(x,z)) * freq + t * speed * freq);
}

vec4 vertexNormal(float x, float z, vec2 direction, float freq, float t, float speed, float amplitude) {
	float d = freq * amplitude * cos(dot(direction, vec2(x,z)) * freq + time * speed * freq);
	float dx = direction.x * d;
	float dz = direction.y * d;
	return vec4(-dx, 0.0, -dz, 0.0);
}

void main(){
    vec4 wpos = vec4(position, 1.0);
    wpos.z += vertexHeight(position.x,  position.y, vec2(1.0, 0.0), 0.5, time, 2.5, 0.5);
    wpos.z += vertexHeight(position.x,  position.y, normalize(vec2(1.0, 1.0)), 1.0, time, 1.0, 0.65);
    vec4 wnorm = vec4(0,1,0,0);
    wnorm += vertexNormal(position.x,  position.y, vec2(1.0, 0.0), 0.5, time, 2.0, 0.5);
    wnorm += vertexNormal(position.x,  position.y, normalize(vec2(1.0, 1.0)), 1.0, time, 1.0, 0.65);

    gl_Position = projectionMatrix * modelViewMatrix * wpos;
    worldPos = wpos;
    normalInterp =  normalize(wnorm.xyz);
}