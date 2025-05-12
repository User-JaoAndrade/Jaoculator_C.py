import ctypes
import platform
import os
from time import sleep
from python_libs.matriz_lib import matriz_menu

# Verifica se o sistema é linux ou windows
if platform.system() == "Windows":
    lib = ctypes.CDLL(os.path.abspath("calculos/libcalc.dll"))
else:
    lib = ctypes.CDLL(os.path.abspath("calculos/libcalc.so"))


""" Definindo os tipos de argumentos e o tipo de retorno das funções em C++ """
# SOMA
lib.sum.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]           # Argumento para lista de Números e tamanho do array
lib.sum.restype = ctypes.c_float                                            # Retorna um float

# Subtração
lib.subtration.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]
lib.subtration.restype = ctypes.c_float

# Multiplicação
lib.product.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]
lib.product.restype = ctypes.c_float

# Divisão
lib.division.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]
lib.division.restype = ctypes.c_float


# Função que recebe os números do usuário
def user_numbers(type_of_calculation: str) -> list:
    """
    Cria uma lista com n números informados pelo usuário

    Parâmetros:

    type_of_calculation (string): O nome do tipo de calculo que será realizado

    Retorna:
    
    list: Uma lista com os números informados pelo usuário
    """

    list_of_numbers: list = []
    n: int = 1
    print(f"\n>> Informe os números para serem {type_of_calculation} <<\n"
                      " - Aperte '=' para ver o resultado\n")
    while (True):
        try:
            number = input(f"{n}º Número: ")

            if (number == '='):
                return list_of_numbers
            else:
                number = float(number)
                list_of_numbers.append(number)
                n += 1

        except ValueError:
            print("Por favor, informe um número inteiro ou com casa decimal", end='')
            for _ in range(3):
                print(".", end='')
                sleep(1)

# Função que mostra TODOS os números informados pelo usuário
def showing_user_numbers(list_of_numbers: list, symbol: str) -> None:
    """
    Mostra todos os números informados pelo usuário

    Parâmetros:

    list_of_numbers (list): Lista com os números informados pelo usuário
    symbol (str): Operação que será realizada
    """
    print("")
    for index, number in enumerate(list_of_numbers):
        print(number, end=' ')

        if index == len(list_of_numbers) - 1:
            break
        print(symbol, end=' ')

    print("=", end=' ')


def main() -> None:
    while (True):
        numbers_array: list = []
        option: str = input("| Jaoculadora |\n\n"
                            "Operações básicas\n"
                            "1- Adição\n"
                            "2- Subtração\n"
                            "3- Multiplicação\n"
                            "4- Divisão\n"
                            "5- Matrizes\n"
                            
                            "6- Sair\n"
                            "\n-> ")
        
        match (option):
            case '1': # Soma
                numbers_array = user_numbers('Somados')
                cpp_numbers_array = (ctypes.c_float * len(numbers_array))(*numbers_array)
                showing_user_numbers(numbers_array, '+')
                print(lib.sum(cpp_numbers_array, len(numbers_array)))
                input("\nqualquer tecla para continuar...")
                
            case '2': # Subtração
                numbers_array = user_numbers('Subtrair')
                cpp_numbers_array = (ctypes.c_float * len(numbers_array))(*numbers_array)
                showing_user_numbers(numbers_array, '-')
                print(lib.subtration(cpp_numbers_array, len(numbers_array)))
                input("\nqualquer tecla para continuar...")

            case '3': # Multiplicação
                numbers_array = user_numbers('Multiplicar')
                cpp_numbers_array = (ctypes.c_float * len(numbers_array))(*numbers_array)
                showing_user_numbers(numbers_array, 'x')
                print(lib.product(cpp_numbers_array, len(numbers_array)))
                input("\nqualquer tecla para continuar...")
            
            case '4': # Divisão
                numbers_array = user_numbers('Dividir')
                cpp_numbers_array = (ctypes.c_float * len(numbers_array))(*numbers_array)
                showing_user_numbers(numbers_array, '/')
                print(lib.division(cpp_numbers_array, len(numbers_array)))
                input("\nqualquer tecla para continuar...")
            
            case '5': # Matriz
                matriz_menu()

            case '6':
                print("Bye bye")
                break
            
            case _:
                pass