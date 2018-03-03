uniform float time;
varying vec3 normalInterp;
varying vec4 worldPos;

float vertexWaveHeight(float x, float z, vec2 direction, float freq, float t, float speed, float amplitude) {
	return amplitude * sin(dot(direction, vec2(x,z)) * freq + t * speed * freq);
}

vec4 vertexWaveNormal(float x, float z, vec2 direction, float freq, float t, float speed, float amplitude) {
	float d = freq * amplitude * cos(dot(direction, vec2(x,z)) * freq + time * speed * freq);
	float dx = direction.x * d;
	float dz = direction.y * d;
	return vec4(-dx, -dz, 0.0,  0.0);
}

float vertexGaussianHeight(float x, float z, float t, float var, float amplitude){
    float cx = 15.0 * sin(t * .5);
    float cz = 15.0 * cos(t * .5);
    return amplitude * exp(-(pow(x - cx, 2.0) + pow(z - cz, 2.0))/(2.0 * var * var)) / (var * var);
}

vec4 vertexGaussianNormal(float x, float z, float t, float var, float amplitude){
    float cx = 15.0 * sin(t * .5);
    float cz = 15.0 * cos(t * .5);
    float d = -amplitude * exp(-(pow(x - cx, 2.0) + pow(z - cz, 2.0))/(2.0 * var * var)) / (var * var * var * var);
    return vec4(-d * (x - cx), -d * (z - cz), 0.0,  0.0);
}



void main(){
    vec4 wpos = vec4(position, 1.0);
    wpos.z += vertexWaveHeight(position.x,  position.y, vec2(1.0, 0.0), 0.5, time, 2.5, 0.5);
    wpos.z += vertexWaveHeight(position.x,  position.y, normalize(vec2(1.0, 1.0)), 1.0, time, 1.0, 0.65);
    wpos.z += vertexGaussianHeight(position.x, position.y, time, 2.5, 80.0);
    
    vec4 wnorm = vec4(0, 0, 1.0, 0);
    wnorm += vertexWaveNormal(position.x,  position.y, vec2(1.0, 0.0), 0.5, time, 2.0, 0.5);
    wnorm += vertexWaveNormal(position.x,  position.y, normalize(vec2(1.0, 1.0)), 1.0, time, 1.0, 0.65);
    wnorm += vertexGaussianNormal(position.x, position.y, time, 2.5, 80.0);

    gl_Position = projectionMatrix * modelViewMatrix * wpos;
    worldPos = wpos;
    normalInterp =  normalize(wnorm.xyz);
}
