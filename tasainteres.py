def interes():
	c=int(input("Cual es su capital inicial en pesos?: "))
	n=int(input("Cual es su taza de interes inicial?: "))
	a=int(input("Por cuantos años?: "))
	monto = ((1+(n/100)** a))*c
	print("El monto final es de: ", monto, "pesos")

	
