//
// Created by angela on 03/11/20.
//

#ifndef UNTITLED1_EX_1_H
#define UNTITLED1_EX_1_H

#include <iostream>
#include "cmath"

float Sin(float x);

float regraDosTrapezios(float n, float (*f)(float), float x0, float xn);

float regraDeSimpson(float n, float (*f)(float), float x0, float x2n);

float quocienteDeConvergencia(float n, float (*f)(float), float x0, float xn);

float erroAbsoluto(float valorEsperado, float valorObtido);

void ex_1();

#endif //UNTITLED1_EX_1_H
