#Crie uma função que recebe como parâmetro um número inteiro e retorna o seu dobro.

def dobro_numero(numero):
    d = numero * 2
    return d

numero = int(input("Insira um número: "))
d = dobro_numero(numero)
print(f"O dobro de {numero} é {d}")