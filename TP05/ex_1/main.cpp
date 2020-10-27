#include <iostream>
#include "cmath"


float Sin(float x){
    return sin(x);
}

float regraDosTrapezios(float n, float (*f)(float), float x0, float xn){
    //Para sin(x)
    float h = M_PI / n;
    float result = f(x0) + f(xn);
    float sum = h;
    for (unsigned int i = 1; i < n; i++) {
        result += 2*(f(sum));
        sum += h;
    }
    return (h/2)*result;
}

float regraDeSimpson(float n, float (*f)(float), float x0, float x2n){
    float h = M_PI/(2*n);
    float result  = f(x0) +f(x2n);
    float sum = 0;
    for(unsigned int i=1; i < (2*n); i++){
        if(i%2 == 0)
            result += 2*(f(sum));
        else
            result += 4*(f(sum));
        sum += h;
    }
    return (h/3)*result;
}

float quocienteDeConvergencia(float n, float (*f)(float), float x0, float xn){
    float h = M_PI/n;
    float S = regraDosTrapezios(n, Sin, x0, xn);
    float SS = regraDosTrapezios(2*n, Sin, x0, xn);
    float SSS = regraDosTrapezios(4*n, Sin, x0, xn);
    return ((SS-S)/(SSS-SS));
}


float erroAbsoluto(float valorEsperado, float valorObtido){
    return(fabs(valorEsperado-valorObtido));
}


int main() {
    //Para integral(sin(x),x,0,%pi)
    float valorEsperado = 2;
    float v[] = {4, 8, 16, 64};
    for(unsigned int i=0; i < 4; i++){
        float valorObtidoTrapezio = regraDosTrapezios(v[i], Sin, 0, M_PI);
        float valorObtidoSimpson = regraDeSimpson(v[i], Sin, 0, M_PI);
        std::cout << "n = " << v[i] << std::endl << std::endl;
        std::cout << "Com a regra dos trapezios" << std:: endl;
        std::cout << "Resultado: " << valorObtidoTrapezio << std::endl;
        std::cout << "Erro absoluto: " << erroAbsoluto(valorEsperado, valorObtidoTrapezio) << std::endl;
        if(v[i] < 64)
            std::cout << "Quociente de convergencia: " << quocienteDeConvergencia(v[i], Sin, 0, M_PI) << std:: endl;
        std::cout << std::endl;

        std::cout << "Com a regra de Simpson" << std::endl;
        std::cout << "Resultado: " << valorObtidoSimpson << std::endl;
        std::cout << "Erro absoluto: " << erroAbsoluto(valorEsperado, valorObtidoSimpson) << std::endl;
        if(v[i] < 64)
            std::cout << "Quociente de convergencia: " << quocienteDeConvergencia(v[i], Sin, 0, M_PI) << std:: endl;
        std::cout << std::endl << std::endl;
    }

    return 0;
}
