//
// Created by angela on 03/11/20.
//

#include "ex_1.h"

double df(double x, double y){
    return pow(x,2) + pow(y,2);
}

double euler(const double h, const double final){
    double x, y;
    double x0 = 0, y0 = 0;

    for(unsigned int i = 0; i < final/h; i++){
        x = x0 + h;
        y = y0 + h * df(x0, y0);
        x0 = x; y0 = y;
    }
    return y;
}

double rk4(const double h, const double final){
    double x, y, aux1, aux2, aux3, aux4;
    double x0 = 0, y0 = 0;
    for(unsigned i = 0; i < final/h; i++){
        x = x0 + h;
        aux1 = (h) * df(x0, y0);
        aux2 = (h) * df(x0 + h/2, y0 + aux1/2);
        aux3 = (h) * df(x0 + h/2, y0 + aux2/2);
        aux4 = (h) * df(x0 + h, y + aux3);
        y = y0 + (aux1/6 + aux2/3 + aux3/3 + aux4/6);
        x0 = x;
        y0 = y;
    }
    return y;
}

double convergenceQuotient(const std::vector<double>& solutions){
    double S = solutions.at(0), SS = solutions.at(1), SSS = solutions.at(2);
    return (SS-S)/(SSS-SS);
}

double error(const std::vector<double>& solutions){
    double SS =solutions.at(1), SSS = solutions.at(2);
    return SSS-SS;
}

void a(){
    const double h = 0.1;

    std::cout << SEPARATOR << std::endl;
    std::cout << "Exercise 1. a)" << std::endl;
    std::cout << SEPARATOR << std::endl;

    std::cout << "Euler" << std::endl;
    std::cout << "y(0.7) = " << euler(h, 0.7)<< std::endl;
    std::cout << "y(1.4) = " << euler(h, 1.4) << std:: endl;
    std::cout<<std::endl << std::endl;

    std::cout << "Rk4" << std::endl;
    std::cout << "y(0.7) = " << rk4(h, 0.7) << std::endl;
    std::cout << "y(1.4) = " << rk4(h, 1.4) << std::endl;
    std::cout << SEPARATOR << std::endl << std::endl << std::endl;

}

void b(){
    double h = 0.1/2;

    std::cout << SEPARATOR << std::endl;
    std::cout << "Exercise 1. b)" << std::endl;
    std::cout << SEPARATOR << std::endl;

    for(unsigned int i=0; i < 2; i++){
        std::cout << "h = " << h << std::endl << std::endl;
        std::cout << "Euler" << std::endl;
        std::cout << "y(0.7) = " << euler(h, 0.7)<< std::endl;
        std::cout << "y(1.4) = " << euler(h, 1.4) << std:: endl;

        std::cout << "Rk4" << std::endl;
        std::cout << "y(0.7) = " << rk4(h,0.7) << std::endl;
        std::cout << "y(1.4) = " << rk4(h,1.4) << std::endl;
        if(i==1) std::cout << SEPARATOR << std::endl;
        std::cout << std::endl << std::endl;
        h /= 2;
    }

}

void c(){
    double h = 0.1;
    std::vector<double> solutionsEuler, solutionsRk4;
    for(unsigned int i=0; i < 3; i++){
        solutionsEuler.push_back(euler(h,1.4));
        solutionsRk4.push_back(rk4(h, 1.4));
        h /= 2;
    }
    std::cout << SEPARATOR << std::endl;
    std::cout << "Exercise 1. c)" << std::endl;
    std::cout << SEPARATOR << std::endl;
    std::cout << "Convergence quocient" << std::endl;
    std::cout << "Euler" << std::endl;
    std::cout << "QC = " << convergenceQuotient(solutionsEuler) << std::endl << std::endl;
    std::cout << "Rk4" << std::endl;
    std::cout << "QC = " << convergenceQuotient(solutionsRk4) << std::endl;
    std::cout << SEPARATOR << std::endl << std::endl << std::endl;
}

void d(){
    double h = 0.1;
    std::vector<double> solutionsEuler, solutionsRk4;
    for(unsigned int i=0; i < 3; i++){
        solutionsEuler.push_back(euler(h, 1.4));
        solutionsRk4.push_back(rk4(h, 1.4));
        h /= 2;
    }
    std::cout << SEPARATOR << std::endl;
    std::cout << "Exercise 1. d)" << std::endl;
    std::cout << SEPARATOR << std::endl;
    std::cout << "Euler" << std::endl;
    std::cout << "Error = " << error(solutionsEuler) << std::endl << std::endl;
    std::cout << "Rk4" << std::endl;
    std::cout << "Error = " << error(solutionsRk4)/15 << std::endl;
    std::cout << SEPARATOR << std::endl << std::endl << std::endl;
}

void ex_1(){
    a(); b(); c(); d();
}