'''
Desenvolva uma aplicação para geração de um circuíto automotivo a partir de 4 curvas de Bézier.
Para isso, inicialmente gere aleatoriamente os 13 pontos que fazem parte da curva (P0, P1, P2
 P12), sendo que P0, P3, P6, P9 e P12 são os pontos de ligação entre as curvas
(e que P0 = P12, de modo a ser um circuíto fechado),
e os demais são pontos de controle. Após, defina a quantidade de segmentos a curva terá e 
então calcule os pontos que farão parte da mesma, apresentando o resultado na tela
'''
#pontos iniciais e finais são p0,p3,p6,p9,p12
import random as randint
def gerarPontos():
    vetor = []
    for i in range(2):
        valor = randint.randint(0,30)
        vetor.append(valor)
    print(vetor)
    return vetor

def criarCurvas(pontoIni,pontoFim,pontoControle1,pontoControle2):
    t = 0
    while t < 1:
        part1 = (1-t)*(1-t)*(1-t)*pontoIni[0]
        part2 = 3*(1-t)*(1-t)*t*pontoControle1[0]
        part3 = 3*(1-t)*t*t*pontoControle2[0]
        part4 = t*t*t*pontoFim[0]
        x = part1+part2+part3+part4

        part1 = (1-t)*(1-t)*(1-t)*pontoIni[1]
        part2 = 3*(1-t)*(1-t)*t*pontoControle1[1]
        part3 = 3*(1-t)*t*t*pontoControle2[1]
        part4 = t*t*t*pontoFim[1]
        y = part1+part2+part3+part4
        print("({},{})".format(x,y))
        t = t + 0.01

p0 = gerarPontos()
p1 = gerarPontos()
p2 = gerarPontos()
p3 = gerarPontos()
p4 = gerarPontos()
p5 = gerarPontos()
p6 = gerarPontos()
p7 = gerarPontos()
p8 = gerarPontos()
p9 = gerarPontos()
p10 = gerarPontos()
p11 = gerarPontos()
p12 = gerarPontos()

criarCurvas(p0,p3,p1,p2)
criarCurvas(p3,p6,p4,p5)
criarCurvas(p6,p9,p7,p8)
criarCurvas(p9,p12,p10,p11)
criarCurvas(p12,p0,p1,p2)

'''
	for(t=0; t<1; t+=0.001){
		part1 = (1-t)*(1-t)*(1-t)*P0.x;
		part2 = 3*(1-t)*(1-t)*t*P1.x;
		part3 = 3*(1-t)*t*t*P2.x;
		part4 = t*t*t*P3.x;
		x = part1+part2+part3+part4;
		
		part1 = (1-t)*(1-t)*(1-t)*P0.y;
		part2 = 3*(1-t)*(1-t)*t*P1.y;
		part3 = 3*(1-t)*t*t*P2.y;
		part4 = t*t*t*P3.y;
		y = part1+part2+part3+part4;
		
		printf("(%f,%f)\n",x,y);
		
	}
}
'''