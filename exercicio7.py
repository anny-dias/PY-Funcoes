#Escreva um programa que solicita um valor inteiro ao usuário e exibe a tabuada desse número. 
# Você deverá escrever as seguintes funções:
#-ler_numero(): Solicitaum número inteiro e retorna esse número para o programa principal.
#-tabuada(n): Recebe como parâmetro um número inteiro e mexibe na tela a tabuada desse número.

def ler_numero(numero):
    n = numero 
    return n
def tabuada(n):
    print(f"Tabuada do {n}: ")
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")


numero = int(input("Informe um número: "))
n = ler_numero(numero)
tabuada(n)