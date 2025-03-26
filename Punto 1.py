#Crea un programa haciendo uso de la clase, objeto, atributo y método mencionados en el parcial escrito, 
#sobre la tarjeta débito, usando también encapsulamiento

class Tarjeta:
    def __init__(self, balance):
        self.__balance = balance #Aquí encapsulamos la variable balance

    def revisar_saldo(self):
        print("Tu saldo actual es: ", self.__balance)

    def depositar(self, cantidad):
        self.__balance += cantidad
        print("Consignación completa, el nuevo saldo es: ", self.__balance)

    def retirar(self, cantidad):
        if self.__balance >= cantidad:
            self.__balance -= cantidad
            print("Retiro completo, el nuevo saldo es: ", self.__balance)
        else:
            print("Saldo insuficiente para esta transacción.")

#Crea una tarjeta con 1000 de saldo
tarjeta1 = Tarjeta(1000)

#Revisa el saldo
tarjeta1.revisar_saldo()

#Deposita 500
tarjeta1.depositar(500)

#Retira 200
#tarjeta1.retirar(200)

#Retira 2000, esperando el mensaje de error
tarjeta1.retirar(2000)