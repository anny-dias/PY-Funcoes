#Faça  um  programa  para  uma  calculadora  simples  com  as  seguintes  operações:  
#adição,  subtração, multiplicação e divisão. O programa começa apresentando ao usuário
#um menu de opções semelhante ao mostrado abaixo:
# Calculadora: 
# 1 -Adição
# 2 -Subtração
# 3 -Multiplicação
# 4 -Divisão
# 5 -Sair do programa
# Selecione sua opção:
#Crie  uma  função  chamada Menu,  que  exiba  o  menu  acima  e  retorna  a  opção  do  usuário
#para o programa  principal. Se  a  opção  for  inválida,  informe  ao  usuário  e  peça  a  
#ele  para  entrar com  uma opção válida. De   acordo   com  a   opção   do   usuário,   chame
#uma   das   seguintes funções: adicao,   subtracao, multiplicacao, divisao, passando como 
#parâmetros dois números também informados pelo usuário. Após a execução da operação o programa
#volta a apresentar o menu inicial até que o usuário encerre o programa com a opção 5.

def menu():
    print("Calculadora: ")
    print("1 -Adição")
    print("2 -Subtração")
    print("3 -Multiplicação")
    print("4 -Divisão")
    print("5 -Encerrar programa")

def adicao(num1, num2):
    resultado = num1 + num1 
    print(f"O resultado da soma de {num1} e {num2} é {resultado}")

def subtracao(num1, num2):
    resultado = num1 - num1 
    print(f"O resultado da subtração de {num1} e {num2} é {resultado}")

def multiplicacao(num1, num2):
    resultado = num1 * num1 
    print(f"O resultado da multiplicação de {num1} e {num2} é {resultado}")

def divisao(num1, num2):
    resultado = num1 / num1 
    print(f"O resultado da divisão de {num1} e {num2} é {resultado}")

def fim():
    print("Fim do programa")


while True:
    menu()
    opcao = int(input("Selecione sua opção: "))
    num1 = float(input("Informe o primeiro número: "))
    num2 = float(input("Informe o segundo número: "))
    
    if opcao == 1:
        adicao(num1, num2)
    elif opcao == 2:
        subtracao(num1, num2)
    elif opcao == 3:
        multiplicacao(num1, num2)
    elif opcao == 4:
        divisao(num1, num2)
    elif opcao == 5:
        fim()
        break
    else:
        print("Opção Inválida")
        
    


