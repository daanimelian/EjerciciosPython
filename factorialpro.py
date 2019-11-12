def factorial():
	cantidad=int(input("A cuantos numeros le quiere calcular el factorial?: "))
	
	for j in range (1, cantidad+1):
		n=int(input("Cual es el numero al que le quiere calcular su factorial?: "))
		fact = 1
		for i in range (1, n + 1):
			fact *= i
			
		print (j, "-", fact)
