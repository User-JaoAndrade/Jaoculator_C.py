from time import sleep

# Função que printa 3 pontinhos
def three_dots() -> None:
    """
    Mostrar 3 pontos em um intervalo de 1 seg cada
    
    """
    for i in range(3):
        print(".", end='')
        sleep(1)