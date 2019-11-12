def matriz(n):
	n = int(n)
	M = []
	for i in range(n):
		fila = []
		for j in range(n):
			val = 1 if i==j else 0
			fila.append(val)
		M.append(fila)
	print (M)
