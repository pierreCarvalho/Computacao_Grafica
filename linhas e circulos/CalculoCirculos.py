'''
Escolha um dos algoritmos de rasterização de círculos. Está aplicação deverá:

Pedir para o usuário informar o valor do raio do círculo (r);
Pedir para o usuário informar o ponto central do círculo;
A partir S raio e do ponto central, gerar os pontos (x,y) que formam o círculo e apresentar os mesmos na tela.
'''

def calcularCirculo(raio,ponto):
	print(raio)
	p = 1 - raio
	x = 0
	y = raio
	while(x < y):
		if (p<0):
			x = x+1
			p = p + (2*x) + 1
		elif p >=0:
			x = x+1
			y = y - 1 
			p = p + ((2*x) - (2*y)) + 1
		print("({},{})\n".format(x +ponto[0] ,y+ponto[1]))
		print("({},{})\n".format(y+ponto[1],x+ponto[0]))
		print("({},{})\n".format(y+ponto[1],-x+ponto[0]))
		print("({},{})\n".format(x+ponto[0],-y+ponto[1]))
		print("({},{})\n".format(-x+ponto[0],-y+ponto[1]))
		print("({},{})\n".format(-y+ponto[1],-x+ponto[0]))
		print("({},{})\n".format(-y+ponto[1],x+ponto[0]))
		print("({},{})\n".format(-x+ponto[0],y+ponto[1]))


raio = int(input("Informe o raio: "))
ponto_central_x = int(input("Informe o x do ponto central: "))
ponto_central_y = int(input("Informe o y do ponto central: "))

ponto = [ponto_central_x,ponto_central_y]
calcularCirculo(raio,ponto)


