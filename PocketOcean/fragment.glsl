precision mediump float;

varying vec3 normalInterp;
varying vec3 vertPos;

const vec3 lightPos 	= vec3(200,60,100);
const vec3 ambientColor = vec3(0.0, 0, 0.1);
const vec3 diffuseColor = vec3(0, .4666 , .745);
const vec3 specColor 	= vec3(1.0, 1.0, 1.0);

void main() {
	vec3 normal = normalize(normalInterp);
	vec3 lightDir = normalize(lightPos - vertPos);

	float lambertian = max(dot(lightDir,normal), 0.0);
	float specular = 0.0;

    if(lambertian > 0.0){
        vec4 r = vec4(normalize(reflect(lightDir, normal)), 0.0);
        vec4 v = normalize(viewMatrix * vec4(cameraPosition - vertPos, 0.0));
        specular = pow(clamp(max(dot(v, r), 0.0), 0.0, 1.0), 20.0);
    }


	gl_FragColor = vec4(ambientColor + lambertian * diffuseColor + specular * specColor, 1.0);
}