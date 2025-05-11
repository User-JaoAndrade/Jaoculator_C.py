import ctypes
import platform
import os
from time import sleep

# Verifica se o sistema é linux ou windows
if platform.system() == "Windows":
    lib = ctypes.CDLL(os.path.abspath("calculos/libcalc.dll"))
else:
    lib = ctypes.CDLL(os.path.abspath("calculos/libcalc.so"))

lib.sum.argtypes = [ctypes.c_float, ctypes.c_float]
lib.sum.restype = ctypes.c_float

lib.subtration.argtypes = [ctypes.c_float, ctypes.c_float]
lib.subtration.restype = ctypes.c_float

lib.product.argtypes = [ctypes.c_float, ctypes.c_float]
lib.product.restype = ctypes.c_float

lib.division.argtypes = [ctypes.c_float, ctypes.c_float]
lib.division.restype = ctypes.c_float

def convertion_type(x: str) -> float:
    try:
        x = float(x)
        return x
    
    except:
        print("POR FAVOR, INFORME APENAS NÚMEROS", end='')
        for i in range(3):
            print(".", end='')
            sleep(1)
        main()


def main() -> None:
    while (True):
        option: str = input("| Jaoculadora |\n\n"
              "1- Adição\n"
              "2- Subtração\n"
              "3- Multiplicação\n"
              "4- Divisão\n"
              "5- Sair\n"
              "\n-> ")
        
        match (option):
            case '1':
                print("Informe dois números para serem Somados\n")
                a: str = input("1º Número: ")
                a = convertion_type(a)

                b: str = input("2º Número: ")
                b = convertion_type(b)
                
                print(f"\n{a} + {b} = {lib.sum(a, b)}\n")
                
            case '2':
                print("Informe dois números para serem Subtraidos\n")
                a: str = input("1º Número: ")
                a = convertion_type(a)

                b: str = input("2º Número: ")
                b = convertion_type(b)
                
                print(f"\n{a} - {b} = {lib.subtration(a, b)}\n")
                
            case '3':
                print("Informe dois números para serem Multiplicados\n")
                a: str = input("1º Número: ")
                a = convertion_type(a)

                b: str = input("2º Número: ")
                b = convertion_type(b)
                
                print(f"\n{a} * {b} = {lib.product(a, b)}\n")
            
            case '4':
                print("Informe dois números para serem Divididos\n")
                a: str = input("1º Número: ")
                a = convertion_type(a)

                b: str = input("2º Número: ")
                b = convertion_type(b)
                
                print(f"\n{a} / {b} = {lib.division(a, b)}\n")
            
            case '5':
                print("Bye bye")
                break
            
            case _:
                pass
        

if (__name__ == "__main__"):
    main()