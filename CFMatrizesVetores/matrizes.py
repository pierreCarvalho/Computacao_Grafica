'''
Desenvolva um programa que leia pelo teclado os valores de uma matriz 3x3, e então apresente um menu com as seguintes opções:

Adição e subtração de outra matriz, lendo os valores dessa outra matriz 3x3 e mostrando o resultado na tela;
Multiplicação e Divisão de um escalar lido pelo teclado;
Multiplicação da matriz por um vetor de 3 elementos, este lido pelo teclado;
Multiplicação da matriz por outra matriz 3x3, esta lida pelo teclado;
Apresentar a transposta da matriz lida inicialmente.
'''
import numpy as np
def criarMatriz(matriz):
    for i in range(3):
        for j in range(3):
            valor = int(input("Informe um valor:"))
            matriz[i][j] = valor
    print("Sua matriz é:")
    for i in range(len(matriz)):
        print("{}".format(matriz[i]))
    return matriz
def multVetor(vetor,matriz):
    matriz_resultado = [0,0,0]
    
    for i in range(len(matriz)):
        mult = 0
        for j in range(len(matriz[0])):
            mult += vetor[j] * matriz[i][j]
        matriz_resultado[i] = mult
    return matriz_resultado

def menu(matriz_A):
    escolha = int(input("----Bem vindo ao menu----\nEscolha uma opção; \n"
                    "(0) Soma da matrizes \n(1) Subtração de matrizes  \n"
                    "(2) Multiplicação de matrizes de um escalar desejado \n(3) Divisão de matrizes de um escalar desejado\n"
                    "(4) Multiplicação da matriz por um vetor de 3 elementos\n"
                    "(5) Multiplicação da matriz por outra matriz 3x3 \n"
                    "(6) Exibir a matriz trasnposta da matriz inicial\n"
                    "(7) Sair \n"))
    if escolha == 0:
        matriz_B = np.array([[0,0,0],[0,0,0],[0,0,0]])
        matriz_B = criarMatriz(matriz_B)
        matriz_soma = matriz_A + matriz_B
        print(matriz_soma)
        #realiza a soma      
    elif escolha == 1:
        matriz_B = np.array([[0,0,0],[0,0,0],[0,0,0]]) 
        matriz_B = criarMatriz(matriz_B)
        matriz_sub = matriz_A - matriz_B
        print(matriz_sub)
        #realiza a subtração
    elif escolha == 2:
        escalar = int(input("Informe o escalar"))
        matriz_mult = escalar * matriz_A
        print(matriz_mult)
        #realiza a multiplicação       
    elif escolha == 3:
        escalar = int(input("Informe o escalar"))
        matriz_div = matriz_A / escalar
        print(matriz_div)
        #realiza a divisão
    elif escolha == 4:
        valor_x = int(input("Informe o valor do x"))
        valor_y = int(input("Informe o valor do y"))
        valor_z = int(input("Informe o valor do z"))
        vetor_tmp = np.array([valor_x, valor_y, valor_z])
        #realiza a multiplicação de vetor e matriz
        matriz_resultado = multVetor(vetor_tmp,matriz_A)
        print(matriz_resultado)
    elif escolha == 5:
        matriz_B = np.array([[0,0,0],[0,0,0],[0,0,0]]) 
        matriz_B = criarMatriz(matriz_B)
        #realiza a mult entre as duas
        matriz_resultado = matriz_A * matriz_B
        print(matriz_resultado)
    elif escolha == 6:
        #matriz_transposta = matriz_A.transpose()
        print(matriz_A.transpose())
        
        #realiza a subtração
    elif escolha == 7:
        exit(-1)

matriz = np.array([[0,0,0],[0,0,0],[0,0,0]])
matriz = criarMatriz(matriz)
menu(matriz)

