#include <iostream>
#include "basic_calc.h"


// Função de soma
float sum(float* numbers_array, int size) {
    float result = 0;

    for (int i = 0; i < size; i+=1) {
        result += numbers_array[i];
    }

    return result;
}

// Função de subtração
float subtration(float* numbers_array, int size) {
    float result = numbers_array[0];

    for (int i = 1; i < size; i+=1) {
        result -= numbers_array[i];
    }

    return result;
}

// Função de Multiplicação
float product(float* numbers_array, int size) {
    float result = 1;

    for (int i = 0; i < size; i+=1) {
        result *= numbers_array[i];
    }

    return result;
}

// Função de Divisão
float division(float* numbers_array, int size) {
    float result = numbers_array[0];

    for (int i = 1; i < size; i+=1) {
        result /= numbers_array[i];
    }

    return result;
}
