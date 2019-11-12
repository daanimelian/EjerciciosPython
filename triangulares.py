def numeros_triangulares():
	suma = 0
	n=int(input("Hasta que numero quiere saber cuales son triangulares?: "))
	for i in range(1, n+1):
		suma += i
		print(i, "-", suma)