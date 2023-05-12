#Implementar uma função que recebe como parâmetro a altura em metros (exemplo: 1.70) 
# e o sexo ('M' para masculino e 'F' para feminino) de uma pessoa e retorne o seu peso ideal, 
# sendo que:
# Peso Ideal (para homens) = (72.7 * altura) -58 
# Peso Ideal (para mulheres) = (62.1 * altura) -44.7

def peso_ideal(altura, sexo):
    if sexo == "F":
        peso = (62.1 * altura) -44.7
        print(f"O peso ideal, para mulher, é: {peso} ")
    elif sexo == "M":
        peso = (72.7 * altura) -58 
        print(f"O peso ideal, para homem, é: {peso} ")
    else:
        print("Opção Inválido")
    return peso


altura = float(input("Infome a sua altura: "))
sexo = input("Informe o seu sexo (M = Masculino e F = Feminino): ")
peso = peso_ideal(altura, sexo)




