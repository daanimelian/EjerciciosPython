class MiCadena:

	def __init__(self,cadena):
		"""Constructor de la clase MiCadena"""
		self.__cadena = cadena

	def es_mayuscula(self):
		"""Devuelve si la cadena es una letra mayuscula"""
		if not self.__cadena.isalpha():
			return False
		return self.__cadena.upper() == self.__cadena		

	def __str__(self):
		"""Devuelve la representacion en cadena de mi objeto"""
		return self.__cadena

	def __repr__(self):
		"""Devuelve la representacion del objeto"""
		return str(self)


	def __lt__(self,otra):
		"""En 'MiCadena', los elementos se ordenan:
			* Primero las letras mayusculas
			* Segundo las letras minusculas
			* Tercero los numeros pares
			* Cuarto los numeros impares
			* Ultimos los simbolos
		"""

		if not otra.__cadena.isalnum():
			if  self.__cadena.isalnum():
				return True

			return self.__cadena < otra.__cadena

		if  not self.__cadena.isalnum():
			return False
	
		if otra.__cadena.isdigit():
			if not self.__cadena.isdigit():
				return True

			numero_self = int(self.__cadena)
			numero_otra = int(otra.__cadena)


			if numero_self % 2 == numero_otra % 2:
				return numero_self < numero_otra
			return numero_self % 2 == 0

		if self.__cadena.isdigit():
			return False

		return self.__cadena < otra.__cadena


import random

def probar_cmp_objeto():
	lista = ["A","b","c","d","1","2","3","4","5","+","-","&","%"]

	random.shuffle(lista)

	print("Lista original")
	print(lista)

	for i in range(len(lista)):
		lista[i] = MiCadena(lista[i])

	lista_nueva = sorted(lista)


	for i in range(len(lista_nueva)):
		lista_nueva[i] = str(lista_nueva[i])

	print("Lista ordenada")
	print(lista_nueva)

######################################################################
######################Version usando key##############################
######################################################################

def my_key(item):
	if not item.isalnum():
		return (2,item)

	if item.isdigit():
		return (int(item)%2,item)

	return(-1,item)


def probar_ordenar_key():
	lista = ["A","b","c","d","1","2","3","4","5","+","-","&","%"]

	random.shuffle(lista)

	print("Lista original")
	print(lista)

	print("Lista ordenada")
	print(sorted(lista,key=my_key))


######################################################################
###################Herencia (no usar, solo para ver)##################
######################################################################

class MyString(str):


	def __transformar_en_key(self):
		if not self.isalnum():
			return (2,str(self))

		if self.isdigit():
			return (int(self)%2,str(self))

		return(-1,str(self))

	def __lt__(self,another):
		return self.__transformar_en_key() < another.__transformar_en_key()


def probar_lt_herencia():
	lista = ["A","b","c","d","1","2","3","4","5","+","-","&","%"]

	random.shuffle(lista)

	print("Lista original")
	print(lista)

	for i in range(len(lista)):
		lista[i] = MyString(lista[i])

	lista_nueva = sorted(lista)

	print("Lista ordenada")
	print(lista_nueva)