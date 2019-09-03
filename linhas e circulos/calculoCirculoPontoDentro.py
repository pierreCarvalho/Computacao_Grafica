'''
Implemente uma aplicação que leia pelo teclado o raio de um círculo (r) e um ponto (x,y),
e apresente na tela se o ponto está dentro ou fora do círculo.
Considere que o ponto central do círculo está na origem.
'''
def calcularCirculo(raio,ponto):
	print(raio)
	p = 1 - raio
	x = 0
	y = raio
	diferenca = []
	while(x < y):
		if (p<0):
			x = x+1
			p = p + (2*x) + 1
		elif p >=0:
			x = x+1
			y = y - 1 
			p = p + ((2*x) - (2*y)) + 1
		print("({},{})".format(x,y))
		print("({},{})".format(y,x))
		print("({},{})".format(y,-x))
		print("({},{})".format(x,-y))
		print("({},{})".format(-x,-y))
		print("({},{})".format(-y,-x))
		print("({},{})".format(-y,x))
		print("({},{})".format(-x,y))	
	difx = ponto[0] - 0
	dify = ponto[1] - 0
	diferenca = [difx,dify]
	if diferenca[0] < raio and diferenca[1]<raio:
			print("o ponto ({},{}) Ta dentro".format(ponto[0],ponto[1]))

	else:
		print("o ponto ({},{}) Ta fora".format(ponto[0],ponto[1]))





raio = int(input("Informe o raio: "))
x = int(input("Informe o x de um ponto: "))
y = int(input("Informe o y de um ponto: "))

ponto = [x,y]
calcularCirculo(raio,ponto)