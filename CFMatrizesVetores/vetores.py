'''
Desenvolva um programa que leia pelo teclado os valores x, y e z de um vetor de 3 dimensões. Em seguida, apresente
o usuário um menu com as seguintes opções:

Calcular o tamanho do vetor;
Normalizar o vetor, apresentando o vetor resultante da normalização;
Adicionar outro vetor ao que foi lido anteriormente, lendo os valores x, y e z deste novo vetor;
Subtrair outro vetor ao que foi lido anteriormente, lendo os valores x, y e z deste novo vetor;
Ler o valor de um escalar e realizar a multiplicação do mesmo pelo vetor, mostrando o vetor resultante;
Ler o valor de um escalar e realizar a divisão do mesmo pelo vetor, mostrando o vetor resultante;
Calcular o produto escalar do vetor lido anteriormente por outro vetor, lendo os valores x, y e z deste
novo vetor e mostrando o resultado na tela.
'''
import numpy as np

def menu(vetor_A):

    while True:
        escolha = int(input("----Bem vindo ao menu----\nEscolha uma opção; \n(0) Calcular o tamanho do vetor\n(1) Normalizar o vetor, \n"
                    "(2) Adicionar outro vetor, \n(3) Subtrair outro vetor,\n"
                    "(4) Ler o valor de um escalar e realizar a multiplicação do vetor \n"
                    "(5) Ler o valor de um escalar e realizar a divisão do vetor \n"
                    "(6) Calcular o produto escalar do vetor lido anteriormente por outro vetor\n"
                    "(7) Sair \n"))
        if escolha == 1:
            tamanho = ((vetor_A[0] ** 2) + (vetor_A[1] ** 2) + (vetor_A[2] ** 2)) ** 0.5
            print("A norma do vetor é : {}".format(tamanho))
        elif escolha == 2:
            valor_x = int(input("Informe o valor do x"))
            valor_y = int(input("Informe o valor do y"))
            valor_z = int(input("Informe o valor do z"))
            vetor_tmp = np.array([valor_x,valor_y,valor_z])
            soma = vetor_A + vetor_tmp
            print("A soma do vetor {} e o vetor {} é: {}".format(vetor_A,vetor_tmp,soma))

        elif escolha == 3:
            valor_x = int(input("Informe o valor do x"))
            valor_y = int(input("Informe o valor do y"))
            valor_z = int(input("Informe o valor do z"))
            vetor_tmp = np.array([valor_x, valor_y, valor_z])
            diferenca = vetor_A - vetor_tmp
            print("A diferença do vetor {} e o vetor {} é: {}".format(vetor_A,vetor_tmp,diferenca))
        elif escolha == 4:
            escalar = int(input("Informe o valor do escalar para multiplicar o vetor"))
            vetor_resultante = vetor_A * escalar
            print("O vetor resultante da multiplicação é {} ".format(vetor_resultante))
        elif escolha == 5:
            escalar = int(input("Informe o valor do escalar para dividir o vetor"))
            vetor_resultante = vetor_A / escalar
            print("O vetor resultante da divisão é {}".format(vetor_resultante))
        elif escolha == 6:
            valor_x = int(input("Informe o valor do x"))
            valor_y = int(input("Informe o valor do y"))
            valor_z = int(input("Informe o valor do z"))
            vetor_tmp = np.array([valor_x, valor_y, valor_z])
            produto_escalar = np.dot(vetor_A,vetor_tmp)
            print(produto_escalar)
        elif escolha == 7:
            exit(-1)

valor_x = int(input("Informe o valor do x"))
valor_y = int(input("Informe o valor do y"))
valor_z = int(input("Informe o valor do z"))
vetor_A = np.array([valor_x,valor_y,valor_z])
print(vetor_A)
menu(vetor_A)