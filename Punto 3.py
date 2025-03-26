#Crea un programa que solicite dos números al usuario, y el programa debe identificar cuál es el número menor 
# ingresado y el número mayor ingresado , tras esta identificación el programa debe imprimir los números que 
# hay entre los números ingresados. El programa también debe validar si los números ingresados son iguales e
#imprimir un mensaje diciendo que son iguales y solicitar dos números nuevamente

print("Bienvenido")

def numeros(): #Pedimos los números
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))

    if num1 == num2:#Verificamos si son iguales, al serlo se repite todo
        print("Los números ingresados son iguales. Por favor ingresa dos números diferentes.")
        return numeros()

    return num1, num2

def numerosenrango(num1, num2):#Aquí encontramos los números entre los dos dados
    if num1 < num2:
        for i in range(num1 + 1, num2):#Con el for iteramos de uno en uno desde el primer numero hasta el segundo
            print(i)
    else:
        x = num2 + 2
        for i in range(x - 1, num1):
            print(i)
        
        return numeros()
    
    #return num1, num2


#Aquí creamos el objeto necesario
num1,num2 = numeros ()
numerosenrango(num1,num2)