print("--------------------------------")
print ("Bienvenidos a la calculadora ")
print("--------------------------------")
print("Alumno: *BITSCH FEDERICO* ")
suma = 1
resta = 2
multiplicacion = 3
division = 4
potencia = 5
salir = 6
eleccion = 0
while True: 

    #----------------------------------------------------
    print("""
Indique la operacion a realizar :
*Suma (1) 
*Resta (2)
*Multiplicacion (3) 
*Division (4) 
*Potencia (5) 
*Salir (6)
    """)


    usu = int(input("Ingrese  una OPCION : "))
    #Que el usuario eliga los numeros para hacer la operacion 

    if usu ==1: #SUMA (1)
        num_uno = int(input("Ingresa el primer numero: "))
        num_dos = int(input("Ingresa el segundo numero: "))
        print("La suma de los numeros es: ",num_uno + num_dos)
        
    elif usu ==2: #RESTA (2)
        num_uno = int(input("Ingresa el primer numero: "))
        num_dos = int(input("Ingresa el segundo numero: "))
        print("la resta de los dos numeros es: ",num_uno - num_dos)

    elif usu ==3:#MULTIPLICACION (3)
        num_uno = int(input("Ingresa el primer numero: "))
        num_dos = int(input("Ingresa el segundo numero: "))
        print("La multiplicacion de los dos numeros es : ",num_uno * num_dos)

    elif usu ==4: #DIVISION (4)
        num_uno = int(input("Ingresa el primer numero: "))
        num_dos = int(input("Ingresa el segundo numero: "))
        print("La division de los numeros es : ",num_uno / num_dos)

    elif usu ==5: #POTENCIA (5)
        num_uno = int(input("Ingresa el primer numero: "))
        num_dos = int(input("Ingresa el segundo numero: "))
        print("La potencia de los dos numeros es: ",num_uno ** num_dos)

    elif usu==6: #SALIR (6)
        print("-----CHAU HASTA LUEGO-----")
        break
    #CUANDO PONE UN NUMERO QUE NO ESTE EN EL MENU!
    else:
        print('-'*30,'*OPCION INVALIDA* ' + '-'*30)

        
        
