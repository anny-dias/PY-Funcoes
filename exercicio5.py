#Escreva um programa que leia o raio de um círculo e faça duas funções: 
# uma função chamada area que  calcula  e  retorna  a  área  do  círculo  
# e  outra  função  chamada perimetro que  calcula  e  retorna  o perímetro do círculo.
# Utilize as fórmulas abaixo Área = π * r2 Perímetro = π * 2 * r
def area(raio):
    area = 3.14 * raio ** 2
    print(f"A área do círculo é {area}")

def perimetro(raio):
    perimetro = 3.14 * 2 * raio
    print(f"O perímetro do círculo é {perimetro}")

raio = float(input("Insira o raio do círculo: "))
area(raio)
perimetro(raio)