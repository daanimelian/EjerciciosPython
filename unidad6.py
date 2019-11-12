def ff():
	n = input("Ingrese una palabra: ")
	x = n[0 : 2]
	print(x)
	
def gg():
	m = input("Ingrese una palabra: ")
	x = m[-2 :]
	print(x)
	
def imprimir():
	c = input("Ingrese una cadena: ")
	d = input("Ingrese un separador: ")
	for i in c:
		print(i+d, end="")
	
