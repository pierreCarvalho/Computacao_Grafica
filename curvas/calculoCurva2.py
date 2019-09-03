'''
Modifique o exercício anterior, de modo que as curvas fiquem o mais suaves possíveis.
Você pode utilizar tanto curvas de Bézier quanto Hermite para resolver esse exercício.
'''
import random as randint
def gerarPontos():
    vetor = []
    for i in range(2):
        valor = randint.randint(0,20)
        vetor.append(valor)
    print(vetor)
    return vetor

def criarCurvas(pontoIni,pontoFim,m1,m2):
    t = 0
    
    while t < 1:
        part1 = (2*t*t*t - 3*t*t + 1)*pontoIni[0]
        part2 = (t*t*t - 2*t*t + t)*m1[0]
        part3 = (-2*t*t*t + 3*t*t)*pontoFim[0]
        part4 = (t*t*t* - t*t)*m2[0]
        x = part1+part2+part3+part4

        part1 = (2*t*t*t - 3*t*t + 1)*pontoIni[1]
        part2 = (t*t*t - 2*t*t + t)*m1[1]
        part3 = (-2*t*t*t + 3*t*t)*pontoFim[1]
        part4 = (t*t*t* - t*t)*m2[1]
        y = part1+part2+part3+part4
        print("({},{})".format(x,y))
        t = t + 0.01

p0 = gerarPontos()
p1 = gerarPontos()
p2 = gerarPontos()

m1 = [60,-60]
m2 = [-60,40]
m3 = [60,-40]
criarCurvas(p0,p1,m1,m2)
criarCurvas(p1,p2,m2,m3)


