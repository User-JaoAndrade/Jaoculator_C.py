from python_libs.others_lib import three_dots
import ctypes
import platform
import os

if platform.system() == "Windows":
    lib = ctypes.CDLL(os.path.abspath("calculos/libmatriz.dll"))
else:
    lib = ctypes.CDLL(os.path.abspath("calculos/libmatriz.so"))

# Tipos de Argumentos e Retorno para função soma
lib.matriz_sum.argtypes = [ctypes.POINTER(ctypes.c_float), # Argumento pra Matriz A
                           ctypes.POINTER(ctypes.c_float), # Argumento pra matriz B
                           ctypes.POINTER(ctypes.c_float), # Argumento pra Matriz Result
                           ctypes.c_int,                   # Argumento pro número de linhas
                           ctypes.c_int ]                  # Argumento pro número de colunas

lib.matriz_sum.restype = None                              # Tipo de retorno

# Tipos de Argumentos e Retorno para função subtração
lib.matriz_subtration.argtypes = [ctypes.POINTER(ctypes.c_float),
                                  ctypes.POINTER(ctypes.c_float),
                                  ctypes.POINTER(ctypes.c_float),
                                  ctypes.c_int,
                                  ctypes.c_int ]

lib.matriz_subtration.restype = None

# Tipos de Argumentos e Retorno para função de multiplicar por um número
lib.matriz_product.argtypes = [ctypes.POINTER(ctypes.c_float),
                               ctypes.c_float,
                               ctypes.POINTER(ctypes.c_float),
                               ctypes.c_int,
                               ctypes.c_int ]

lib.matriz_product.restype = None

# Função que mostra as Matrizes
def showing_user_matriz(matriz: list, matriz_name: str, rows: int, columns: int) -> None:
    """
    Função que printa as matrizes que o usuário informou

    Parâmetros:

    matriz(list): Matriz do tipo vetor linear
    matriz_name(str): Nome da matriz
    rows(int): Linhas
    columns(int): colunas

    """
    print(f"\n{matriz_name}")
    for i in range(rows):
        for j in range(columns):
            print(matriz[i * columns + j], end='   ')
        print('')

# Função para os valores de linhas e colunas
def rows_and_columns(matriz_name: str) -> int:
    """
    Receber os valores de linhas e colunas

    Parâmetros:

    matriz_name(str): Nome da Matriz
    Retorna:

    int: Valor de linhas e colunas
    """
    print(f"\n>> MATRIZ {matriz_name}<< ")
    try:
        rows: int = int(input("Informe a quantidade de LINHAS\n-> "))
        columns: int = int(input("Informe a quantidade de COLUNAS\n-> "))
        return rows, columns

    except ValueError:
        print("Por favor, informe um número inteiro", end='')
        three_dots()

# Função que recebe os números do usuário pra matriz
def user_matriz_numbers(matriz_name: str, rows: int, columns: int) -> list:
    """
    Recebe os valores do usuário e retorna um vetor contínuo

    Parâmetros:

    matriz_name(str): Nome da Matriz
    rows(int): Número de linhas
    columns(int): Número de colunas

    Retorna:

    lista: Uma Matriz de números como um vetor contínuo
    """
    matriz: list = []

    print(f"\nINFORME OS DADOS PRA MATRIZ {matriz_name}\n")

    for i in range(rows):
        for j in range(columns):
            try:
                print("")
                number: float = float(input(f"Linha {i+1}, Coluna {j+1} -> "))
                matriz.append(number)
            except ValueError:
                print("Por favor, informe um número inteiro ou com casas decimais")
                three_dots()
                continue
    return matriz

# Função de menu pras matrizes
def matriz_menu() -> None:
    while (True):
        Matriz_A: list = []
        Matriz_B: list = []

        print("\n>> MATRIZES<< \n")
        option: str = input("1- Adição de Matrizes\n"
                            "2- Subtração de Matrizes\n"
                            "3- Multiplicação Distributiva\n"
                            "4- Multiplicação entre Matrizes (Preciso adicionar)\n"
                            "5- Determinante (Preciso Adicionar)\n"
                            "6- Inversa (Preciso Adicionar)\n\n"
                            
                            "7- Voltar ao menu principal\n"
                            "-> ")

        match (option):
            # Soma 
            case '1': 
                print("\nSOMA ENTRE DUAS MATRIZES\n")
                rows, columns = rows_and_columns('A')                       # Quantidade de linhas e colunas
                Matriz_A = user_matriz_numbers('A', rows, columns)          # Chamando função que vai preencher a matriz
                cpp_matriz_A = (ctypes.c_float * len(Matriz_A))(*Matriz_A)  # Convertendo a Matriz para ser utilizada em cpp

                Matriz_B = user_matriz_numbers('B', rows, columns)
                cpp_matriz_B = (ctypes.c_float * len(Matriz_B))(*Matriz_B)

                cpp_result = (ctypes.c_float * len(Matriz_A))()
                lib.matriz_sum(cpp_matriz_A, cpp_matriz_B, cpp_result, rows, columns)

                showing_user_matriz(Matriz_A, 'A', rows, columns)
                print("\n+\n")
                showing_user_matriz(Matriz_B, 'B', rows, columns)
                print("\n=\n")

                # Mostrando o resultado da soma
                print("A + B")
                for i in range(rows):
                    for j in range(columns):
                        print(cpp_result[i * columns + j], end='   ')
                    print("")

                input("pressione qualquer tecla pra continuar...")
            
            # Subtração
            case '2': 
                print("\nSUBTRAÇÃO ENTRE DUAS MATRIZES\n")
                rows, columns = rows_and_columns('A')
                Matriz_A = user_matriz_numbers('A', rows, columns)
                cpp_matriz_A = (ctypes.c_float * len(Matriz_A))(*Matriz_A)

                Matriz_B = user_matriz_numbers('B', rows, columns)
                cpp_matriz_B = (ctypes.c_float * len(Matriz_B))(*Matriz_B)

                # Verificando se as matrizes tem o mesmo tamanho
                if len(Matriz_A) != len(Matriz_B):
                    print("As Matrizes precisam ter o mesmo tamanho pra realizar a subtração\n")
                    continue

                cpp_result = (ctypes.c_float * len(Matriz_A))()
                lib.matriz_subtration(cpp_matriz_A, cpp_matriz_B, cpp_result, rows, columns)

                showing_user_matriz(Matriz_A, 'A', rows, columns)
                print("\n-\n")
                showing_user_matriz(Matriz_B, 'B', rows, columns)
                print("\n=\n")

                # Mostrando o resultado da soma
                print("A - B")
                for i in range(rows):
                    for j in range(columns):
                        print(cpp_result[i * columns + j], end='   ')
                    print("")
                
                input("pressione qualquer tecla pra continuar...")
            
            # Multiplicação Distributiva
            case '3':
                print("\nMULTIPLICAÇÃO DISTRIBUTIVA DE MATRIZ\n")
                multiplier: float = float(input("Multiplicador -> "))

                rows, columns = rows_and_columns('A')
                Matriz_A = user_matriz_numbers('A', rows, columns)
                cpp_matriz_A = (ctypes.c_float * len(Matriz_A))(*Matriz_A)

                cpp_result = (ctypes.c_float * len(Matriz_A))()
                lib.matriz_product(cpp_matriz_A, multiplier, cpp_result, rows, columns)

                showing_user_matriz(Matriz_A, 'A', rows, columns)

                print(f"\n{multiplier} * (A)")
                for i in range(rows):
                    for j in range(columns):
                        print(cpp_result[i * columns + j], end='   ')
                    print("")

                input("pressione qualquer tecla pra continuar...")

            case '7': # Voltar pro menu principal
                return