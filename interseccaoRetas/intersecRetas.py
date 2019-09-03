'''
xi = (b2 - b1) / m1-m2
yi = ((b2*m1) - (b1*m2)) / m1 - m2

'''
vetor_p0 = []
vetor_p1 = []
vetor_p2 = []
vetor_p3 = []

def gerarPontos():
    vetor = []
    for i in range(2):
        valor = int(input("Informe o x para o ponto"))
        vetor.append(valor)
    return vetor

def intersec(vetor_p0,vetor_p1,vetor_p2,vetor_p3):

    m1 = (vetor_p1[1] - vetor_p0[1]) / (vetor_p1[0] - vetor_p0[0])
    m2 = (vetor_p3[1] - vetor_p2[1]) / (vetor_p3[0] - vetor_p2[0])
    if m1 == m2:
        print("As retas são paralelas")
    else:
        #xi = (b2 - b1) / m1 - m2
        #yi = ((b2*m1) - (b1*m2)) / m1 - m2
        #print(xi)
        #print(yi)


vetor_p0 = gerarPontos()
vetor_p1 = gerarPontos()

vetor_p2 = gerarPontos()
vetor_p3 = gerarPontos()

intersec(vetor_p0,vetor_p1,vetor_p2,vetor_p3)



#y = (m1*(x)-(m1*(xc))+yc);
#vetor_p01 = [vetor_p0,vetor_p1]
#print(vetor_p01)

#intersec(vetor_01,vetor_23)