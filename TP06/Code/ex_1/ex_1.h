//
// Created by angela on 03/11/20.
//

#ifndef UNTITLED1_EX_1_H
#define UNTITLED1_EX_1_H

#define SEPARATOR "----------------------------------------"
#include <iostream>
#include <cmath>
#include <vector>

double df(double x, double y);

double euler(const double h, const double final);

double rk4(const double h, const double final);

double convergenceQuotient(double solutions[]);

double error(double expectedValue, double obtainedValue);

void a();

void b();

void c();

void d();

void ex_1();

#endif //UNTITLED1_EX_1_H
