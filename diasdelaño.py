def que_dia_es(n):
	if n <= 0 or n>=366:
		print("ingrese un dia valido")
	else:
		
		if n % 7 == 0:
			print("Domingo")
		if n % 7 == 6:
			print("Sabado")
		if n % 7 == 5:
			print("Viernes")
		if n % 7 == 4:
			print("Jueves")
		if n % 7 == 3:
			print("Miercoles")
		if n % 7 == 2:
			print("Martes")
		if n % 7 == 1:
			print("lunes")