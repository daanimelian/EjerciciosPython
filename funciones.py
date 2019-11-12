def combinar(lista_diccionarios):
	""" Combina una lista de diccionarios en uno sólo. """
	diccionario_nuevo = {}
	for dic in lista_diccionarios:
		for keys, values in dic.items():
			diccionario_nuevo[keys] = diccionario_nuevo.get(keys, 0) + values
	return diccionario_nuevo

def calcular_distancia(dic_1, dic_2, intensidad):
	"""Calcula la distancia entre dos diccionarios como la suma de las diferencias entre los valores 
	de ambos diccionarios, en valor absoluto y  elemento a elemento, elevadas a la intensidad(que en este caso es igual a 1."""
	distancia = 0
	list_a = ()
	list_b = ()
	for a in dic_1.values():
		try:
			a = float(a)
		except ValueError:
			return 'Error. Los valores del primer diccionario no son numericos. No se puede realizar esta operacion.'
	for b in dic_2.values():
		try:
			b = float(b)
		except ValueError:
			return 'Error. Los valores del segundo diccionario no son numericos. No se puede realizar esta operacion.'
	for a in dic_1:
		if a in dic_2:
			termino = (abs(dic_1[a]-dic_2[a]))**intensidad
		else:
			termino = (abs(dic_1[a]))**intensidad
		distancia += termino
	for b in dic_2:
		if b in dic_1:
			termino = 0
		else:
			termino = (abs(dic_2[b]))**intensidad
		distancia += termino
	return distancia

def escalar_diccionario(diccionario, m):
	""" Multiplica por un número y reemplaza a los valores de un diccionario. """
	for key, value in diccionario.items():
		nuevos_valores = m * value
		diccionario[key] = nuevos_valores