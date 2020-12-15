//
// Created by angel on 15/12/2020.
//

#include "ex_1.h"

double df(double m){
    return (double)((g*t*exp(-(c*t))/m) - (g*(1-exp(-(c*t)/m)))/c);
}

double f(double m){
    return (double)(v - ((g*m)/c) * (1-exp(-(c/m *t))));
}

double getAbsoluteError(double a0, double an){
    return abs(an-a0);
}

void bisectionMethod(double a0, double b0) {
    unsigned int numIter = 0;
    double m, an = a0, bn = b0;
    double absoluteError = 1000;
    while(absoluteError >= 0.0001) {
        double temp_m = (an+bn)/(double)2;
        if(f(a0)*f(m) < 0)  bn = m;
        else an = m;
        m = (an+bn)/(double)2;
        absoluteError = getAbsoluteError(temp_m, m);
        numIter++;
    }
    std::cout << "\tMass = " << m << std::endl;
    std::cout << "\tNumber of iterations = " << numIter << std::endl;
}

void newtonMethod(double x0){
    unsigned int numIter = 0;
    double xn = x0, absoluteError = 1000;
    while(absoluteError >= 0.0001){
        xn = (x0 - (f(x0)/df(x0)));
        absoluteError = getAbsoluteError(x0, xn);
        x0 = xn;
        numIter++;
    }
    std::cout << "\tMass = " << x0 << std::endl;
    std::cout << "\tNumber of iterations = " << numIter << std::endl;
}

void ex1(){
    std::cout << "----------------Exercise 1----------------" << std::endl;
    std::cout << "Bisection method:" << std:: endl;
    double a0 = 10, b0 = 100;
    bisectionMethod(a0, b0);
    std::cout << "Newton method:" << std::endl;
    double x0 = 1;
    newtonMethod(x0);
    std::cout << "------------------------------------------" << std::endl << std::endl;
}
