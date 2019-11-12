def imprimir_cuadrados():
	print("Se calcularan cuadrados de numeros")
	
	n1=int(input("Ingrese un numero entero: "))
	n2=int(input("Ingrese otro numero entero: "))
	
	for x in range (n1, n2):
		print("El valor de x es: ", x)
		print (x * x)
	
	print("Es todo por ahora")
imprimir_cuadrados()
