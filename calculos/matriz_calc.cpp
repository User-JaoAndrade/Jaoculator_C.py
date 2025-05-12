#include <iostream>

extern "C" {
    // indice = i * Número de colunas + j
    // Soma de Matriz
    void matriz_sum(float* A, float* B, float* result, int rows, int columns){
        for (int i = 0; i < rows; i += 1){
            for (int j = 0; j < columns; j++){
                result[i * columns + j] = A[i * columns + j] + B[i * columns + j];
            }
        }
    }

    // Subtração de Matriz
    void matriz_subtration(float* A, float* B, float* result, int rows, int columns){
        for (int i = 0; i < rows; i += 1){
            for (int j = 0; j < columns; j++){
                result[i * columns + j] = A[i * columns + j] - B[i * columns + j];
            }
        }
    }

    // Produto entre uma Matriz por um número
    void matriz_product(float* A, float multiplier, float* result, int rows, int columns){
        for (int i = 0; i < rows; i += 1){
            for (int j = 0; j < columns; j++){
                result[i * columns + j] = A[i * columns + j] * multiplier;
            }
        }
    }
}