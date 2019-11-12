def cambiar():
        diccionario = {'Daniela':'04/03/1998', 'Marta':'05/06/2013','Juan':'04/03/1945', 'Micaela':'05/06/2013', 'juana':'07/09/2045'}
        diccio = {}
        clave = []
        for clave, valor in diccionario.items():
                valor = valor[0:5]
                if not valor in diccio:
                        diccio[valor] = []
                diccio[valor].append(clave)
        print(diccio)


def pepito():
		l = [('Hola', 'don pepito'), ('Hola', 'don jose'), ('buenos', 'dias')]
		diccio = {}
		for saludo, persona in l:
				if not saludo in diccio:
					diccio[saludo]=[]
				diccio[saludo].append(persona)
		print(diccio)
def contar(n):
        n = str(n)
        contador = 0
        diccionario = {}
        lista = n.split(" ")
        for palabra in lista:
                if not palabra in diccionario:
                        diccionario[palabra]=[]
                elif palabra in diccionario:
                        contador +=1
                diccionario[palabra].append(contador)
                
        print(diccionario)
        
                
        

		
		
