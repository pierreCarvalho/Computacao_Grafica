'''
1. Desenvolva uma aplicação em que o usuário insere os pontos referentes aos vértices de um triângulo (P0, P1 e P2),
e então calcule, de acordo com um dos algoritmos de rasterização de linhas, os pontos que fazem parte das arestas do triângulo especificado.
Obs: caso escolha o algoritmo de Bresenham para rasterização de linhas, será concedido + 0.5 a nota.
'''
def gerarVetor():
    vetor_tmp = []
    for i in range(2):
        valor = int(input("Informe um valor para o vetor"))
        vetor_tmp.append(valor)
    return vetor_tmp

def gerarPontos(vetor_tmp1,vetor_tmp2):
    print('({},{})'.format(vetor_tmp1[0],vetor_tmp1[1]))
    print('({},{})'.format(vetor_tmp2[0],vetor_tmp2[1]))
    #x1 = 6  y1 = 6
    #1 (10,2)
    #2 (6,6)
    Dy = vetor_tmp2[1] - vetor_tmp1[1]
    Dx = vetor_tmp2[0] - vetor_tmp1[0]
    
    if(Dx == 0):
        for i in range(vetor_tmp1[1],vetor_tmp2[1]):
            print('({},{})'.format(vetor_tmp1[0],i))
        
    else:      
        m = Dy/Dx
        print(m)
        ajuste = 1
        offset = 0 
        if m <= 1 and m > 0 :        
            delta = Dy*2
            limiar = Dx
            limiarInc= Dx*2
            y = vetor_tmp1[1]
            x = vetor_tmp1[0]
            while(x <= vetor_tmp2[0]):
                print('(',x,',',y,')')
                offset+=delta
                if(offset >=limiar):
                    y += ajuste
                    limiar += limiarInc
                x += 1
        elif(m > 1):
            delta = Dx*2
            limiar = Dy
            limiarInc= Dy*2
            x = vetor_tmp1[0]
            y = vetor_tmp1[1]
            while(y <= vetor_tmp2[1]):
                print('(',x,',',y,')')
                offset+=delta
                if(offset >=limiar):
                    x += ajuste
                    limiar += limiarInc
                y += 1
        elif m >= -1  and m < 0 :
            print("angulo menor que 45 e m <-1")
            delta = Dy*2
            limiar = Dx * -1
            limiarInc= (Dx*2) * -1
            y = vetor_tmp1[1]
            x = vetor_tmp1[0]
            while(x <= vetor_tmp2[0]):
                print('(',x,',',y,')')
                offset += delta
                if(offset <= limiar):
                    y -= ajuste
                    limiar += limiarInc
                x += 1

        elif m < -1:
            print("angulo maior que 45 e m >-1")
            delta = Dx*2
            limiar = Dy  * -1
            limiarInc= (Dy*2) * -1 
            y = vetor_tmp1[1]
            x = vetor_tmp1[0]
            while(y >= vetor_tmp2[1]):
                print('(',x,',',y,')')
                offset += delta
                if(offset <= limiar):
                    x += ajuste
                    limiar += limiarInc
                y -= 1

        

vet_1 = gerarVetor()
vet_2 = gerarVetor()
vet_3 = gerarVetor()


gerarPontos(vet_1,vet_2)
gerarPontos(vet_1,vet_3)
gerarPontos(vet_2,vet_3)
