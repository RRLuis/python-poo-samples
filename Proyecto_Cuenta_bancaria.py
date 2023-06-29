class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0): #balance = 0 (todas las cuentas iniciaran con $0)
        super().__init__(nombre, apellido) # Para heredar atributos de "Persona" y no asignarlos de nuevo
        self.numero_cuenta = numero_cuenta
        self.balance = balance # valor de 0 (Por defecto)
        
    def __str__(self):
        return f'\nCliente: {self.nombre} {self.apellido}\nBalance de cuenta: {self.numero_cuenta} : ${self.balance}'
        
    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print('Deposito aceptado')
        
    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print('Retiro realizado')
        else:
            print('Fondos insuficientes')
            
            
            
def crear_cliente ():
    nombre_cl = input('Ingrese su nombre: ')
    apellido_cl = input('Ingrese su apellido: ')
    numero_cuenta = input('Ingrese su numero de cuenta: ')
    cliente_1 = Cliente(nombre_cl, apellido_cl, numero_cuenta) 
    return cliente_1
    # Se crea el objeto. No pedimos balance ya que por defecto es 0


# Llamamos a la función crear_cliente
def inicio(): 
    mi_cliente = crear_cliente() # Devuelve el "Objeto" cliente_1
    print(mi_cliente)

    opcion = 0
    
    while opcion != 's': #salir
        print('Elije: Depositar(D), Retirar (R) o Salir (S)')
        
        opcion = input()
        if opcion == 'D':
            monto_dep = int(input('Monto a depositar: '))
            mi_cliente.depositar(monto_dep) # llamamos al método "depositar"
            
        elif opcion == 'R':
            monto_ret = int(input('Monto a retirar'))
            mi_cliente.retirar(monto_ret) # llamamos al método "retirar"
            
        print(mi_cliente)
    print('Gracias por operar en Banco Python')

inicio()
    
    


    



    