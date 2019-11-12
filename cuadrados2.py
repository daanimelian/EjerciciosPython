def imprimir_cuadrados():
        print("Se calcularon el cuadrado de los numeros")
        
        n1=int(input("Ingrese un  numero: "))
        n2=int(input("Ingrese otro numero: "))
        
        for x in range (n1 , n2):
                print("El numero es:", x , "Su cuadrado es:", x * x)
                
        
        print("Es todo por ahora")

imprimir_cuadrados()
                
