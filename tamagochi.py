class Tamagotchi:
	"""Clase que representa a una mascota virutal"""

	def __init__(self,nombre):
		self.nombre_tamagotchi = nombre.title()
		self.hambre = 50
		self.suenio = 50
		self.felicidad = 50
		self.dormido = False
		self.vivo = True

	def dormir(self):
		if self.dormido:
			return
		self.dormido = True
		self.suenio -= 20

		if self.suenio < 0:
			self.suenio = 0

	def despertar(self):
		assert(self.vivo)

		if not self.dormido:
			return
		self.dormido = False
		self.suenio -= 5

		if self.suenio < 0:
			self.suenio = 0

	def vivir(self):
		self.hambre += 5
		self.suenio += 5
		self.felicidad += 5


		if self.suenio > 100:
			self.suenio = 100

		if self.hambre >= 100:
			self.vivo = False


def probar_tamagotchi():
	tamagotchi = Tamagotchi("Pou")
	
	print(tamagotchi.suenio)

	print("Pou duerme")
	tamagotchi.dormir()
	
	print("Pou despierta")
	tamagotchi.despertar()

	print(f"Pou suenio {tamagotchi.suenio}")

	print("Seteo el hambre a 400 por fuera")
	print(f"Hambre {tamagotchi.hambre}")
	print(f"No se mantiene el invariante: Hambre? {tamagotchi.hambre} - Vivo? {tamagotchi.vivo}")

	print("Uso solo los metodos")
	tamagotchi.vivir()
	print(f"No se mantiene el invariante: Hambre? {tamagotchi.hambre} - Vivo? {tamagotchi.vivo}")

	print("Sin str/repr no se puede imprimir")
	print(tamagotchi)
