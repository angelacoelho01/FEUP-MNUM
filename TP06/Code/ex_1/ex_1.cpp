//
// Created by angela on 03/11/20.
//

#include "ex_1.h"

double df(double x, double y){
    return pow(x,2) + pow(y,2);
}

double euler(double h, double final){
    double x, y;
    double x0 = 0, y0 = 0;

    for(unsigned int i = 0; i < final/h; i++){
        x = x0 + h;
        y = y0 + h * df(x0, y0);
        x0 = x; y0 = y;
    }
    return y;
}

double rk4(double h, double final){
    double x, y, aux1, aux2, aux3, aux4;
    double x0 = 0, y0 = 0;
    for(unsigned i = 0; i < final/h; i++){
        x = x0 + h;
        aux1 = (h) * df(x0,y0);
        aux2 = (h) * df(x0 + h/2, y0 + aux1/2);
        aux3 = (h) * df(x0 + h/2, y0 + aux2/2);
        aux4 = (h) * df(x0 + h, y + aux3);
        y = y0 + (aux1/6 + aux2/3 + aux3/3 + aux4/6);
        x0 = x;
        y0 = y;
    }
    return y;
}

double convergenceQuotient(double solutions[]){
    double S = solutions[0], SS = solutions[1], SSS = solutions[2];
    return (SS-S)/(SSS-SS);
}

double error(double expectedValue, double obtainedValue){
    return expectedValue - obtainedValue;
}

void a(){
    double h = 0.1;
    std::cout << "Euler" << std::endl;
    std::cout << "y(0.7) = " << euler(h, 0.7)<< std::endl;
    std::cout << "y(1.4) = " << euler(h, 1.4) << std:: endl;
    std::cout<<std::endl << std::endl;

    std::cout << "Rk4" << std::endl;
    std::cout << "y(0.7) = " << rk4(h, 0.7) << std::endl;
    std::cout << "y(1.4) = " << rk4(h, 1.4) << std::endl;
    std::cout << std::endl << std::endl;

}

void b(){
    double h = 0.1/2;
    for(unsigned int i=0; i < 2; i++){
        std::cout << "h = " << h << std::endl << std::endl;
        std::cout << "Euler" << std::endl;
        std::cout << "y(0.7) = " << euler(h, 0.7)<< std::endl;
        std::cout << "y(1.4) = " << euler(h, 0.7) << std:: endl;

        std::cout << "Rk4" << std::endl;
        std::cout << "y(0.7) = " << rk4(h,0.7) << std::endl;
        std::cout << "y(1.4) = " << rk4(h,0.7) << std::endl;
        std::cout << std::endl << std::endl;
        h /= 2;
    }

}

void c(){
    double h = 0.1;
    double solutionsEueler[3], solutionsRk4[3], sE[3], sR[3];
    for(unsigned int i=0; i < 3; i++){
        double result = euler(h, 0.7);
        result = euler(h, 1.4);
        solutionsEueler[i] = result;

        result = rk4(h, 0.7);
        result = rk4(h, 1.4);
        solutionsRk4[i] = result;
        h /= 2;
    }

    std::cout << "Convergence quocient" << std::endl;
    std::cout << "Euler" << std::endl;
    std::cout << "QC = " << convergenceQuotient(solutionsEueler) << std::endl << std::endl;
    std::cout << "Rk4" << std::endl;
    std::cout << "QC = " << convergenceQuotient(solutionsRk4) << std::endl << std::endl;

}

void d(){
    std::cout << "Aproximation error" << std::endl;
    std::cout << "Not yet implemented!" << std::endl;
}

void ex_1(){
    a(); b(); c(); d();
}