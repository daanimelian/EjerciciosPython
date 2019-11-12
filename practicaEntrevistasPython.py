#Dar vuelta un string
def string(n):
	print (n[::-1])
	
#Contar la cantidad de letras en un string
def cantLetras(n):
	cantA = 0
	for i in n:
		if i=="a" or i=="A":
			cantA+=1
	print(cantA)
	
#Si una palabra es palindromo

def esPalindromo(n):
	if n==n[::-1]:
		return True
	else:
		return False
#factorial de un numero
def factorial(n):
	fact = 1
	for i in range (1, n+1):
		fact *= i
	print (fact)
#feedbuzz
def feedBuzzApp():
	for i in range(1, 101):
		if i%3==0 and i%5==0:
			print("feedBuzz")
		elif i%3==0:
			print("feed")
		elif i%5==0:
			print("buzz")
		else:
			print(i)
#Secuencia de fibonacci
def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

