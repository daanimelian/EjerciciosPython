def dom(secuencia_dominos):
	lista_cadenas = secuencia_dominos.split()
	lista_fichas = []
	for cadena_fichas in lista_cadenas:
		ficha = cadena_fichas.split("-")
		if len(ficha)!= 2:
			return False
		if not ficha[0].isdigit()or not ficha[1].isdigit():
			return False
		ficha[0]=int(ficha[0])
		ficha[1]=int(ficha[1])
		lista_fichas.append(ficha)
		j = len(lista_fichas)
		for i in range (0, j-1):
			if lista_fichas[i][-1] != lista_fichas[i+1][0]:
				return False
			return True
			
def votar():
	nombres = input("Ingrese los nombres de los votantes: ")
	cad_nombres = nombres.split(",")
	for x in cad_nombres:
		print("Estimado", x, "vote por mi")
		
def votar1():
	lista_nombres = []
	nombres = input("Ingrese, separado por comas, la posición desde la que se saludará, la cantidad de saludos y los nombres: ")
	cad_nombres = nombres.split(",")
	p = int(cad_nombres[0])
	n = int(cad_nombres[1])
	#l = len(cad_nombres)
	#lista_nombres.append(cad_nombres[2:l]) no me devuelve 
	m = cad_nombres[p: p + n]
	for x in m:
		print("Estimado", x, "vote por mi") #Imprime desde el numero 