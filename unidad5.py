#ej1 idk 

def promedio():
	""" Calcul el promedio de los números ingresados. """
	suma = 0
	cantidad = 0
	while True:
		numero = int(input("Ingrese una calificación: "))
		if numero < 0:
			break
			cantidad += 1
		if cantidad > 0:
			suma += 1
			return suma / cantidad
		
#Ej2

def fact(k):
	""" Recibe enteros y devuelve string y enteros.
	Calcula la descomposición del número ingresado en números primos. """
	i = 2
	while i <= k:
		if k % i == 0:
			while k % i == 0:
				print("Factor:", i)
				k = k // 2
		i = i + 1
	
#Ej3 A

def manejar_contrasenia():
	""" Permite al usuario ingresar una cantidad ilimitada de contraseñas, pidiendola otra vez de no ser correcta. """
	contrasenia = "hola"
	while True:
		cont_ingresada = input("Ingrese la contraseña: ")
		if cont_ingresada == "*":
			break
		elif contrasenia != cont_ingresada:
			print("Contraseña incorrecta.")
		else:
			return "Contraseña correcta!"
			
#B

def contrasenia_limitada():
		""" Permite al usuario 3 intentos al introducir la contraseña, de no ser ésta correcta. """
		contrasenia = "buenosdias"
		for x in range(3):
			contrasenia_ingresada = input("Ingrese la contraseña: ")
			if contrasenia_ingresada == "*":
				break
			elif contrasenia_ingresada != contrasenia:
				print("Contraseña incorrecta.")
			else:
				print("Contraseña correcta!")

#D

def contrasenia_limitada():
		""" Permite al usuario 3 intentos al introducir la contraseña, de no ser ésta correcta. """
		contrasenia = "buenosdias"
		for x in range(3):
			contrasenia_ingresada = input("Ingrese la contraseña: ")
			if contrasenia_ingresada == "*":
				break
			elif contrasenia_ingresada != contrasenia:
				print(False)
			else:
				print(True)

#Ej6 A

def es_potencia_de_dos(numero):
	while True:
		if numero >= 0:
			if numero % 2 != 0:
				return False
			else:
				return True
		else:
			break
			
#B

def pot_2(i,j):
	for x in range(i,j+1):
		if es_potencia_de_dos(x):
			print(x)
			
#Ej7 A

def sum_divisores(n):
	""" Recibe y devulve numeros enteros.
	Calcula la suma de los divisores del número ingresado. """
	for x in range(n):
		if x % n == 0:
			return sum(x)