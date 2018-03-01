precision mediump float;

varying vec3 normalInterp;
varying vec4 worldPos;

const vec3 lightPos 	= vec3(200,60,100);
const vec3 ambientColor = vec3(0.0, 0, 0.1);
const vec3 diffuseColor = vec3(0, .4666 , .745);
const vec3 specColor 	= vec3(1.0, 1.0, 1.0);


void main() {

	vec3 normal = normalize(normalInterp);
	vec3 lightDir = normalize(lightPos - worldPos.xyz);

	float lambertian = max(dot(lightDir,normal), 0.0);
	float specular = 0.0;

	vec3 r = normalize(reflect(-lightDir, normal));
    vec3 v = normalize(cameraPosition - worldPos.xyz);
    specular = pow(clamp(max(dot(v, r), 0.0), 0.0, 1.0), 12.0);

	gl_FragColor = vec4(ambientColor + lambertian * diffuseColor + specular * specColor, 1.0);
}