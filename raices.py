def raices_cuadratica(a, b, c):
	if b**2 - 4*a*c >=0 and 2*a > 0:
		raiz1 = (-b+(b**2 - 4*a*c)**(1/2))/ (2*a)
		raiz2 = (-b-(b**2 - 4*a*c)**(1/2))/ (2*a)
		return raiz1, raiz2
	return "No es posible hayar la raiz"