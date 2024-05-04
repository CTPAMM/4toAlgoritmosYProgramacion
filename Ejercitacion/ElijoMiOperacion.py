# Calculadora para sumar y restar

while True:
    # PASO 1: Crear un menú de opciones

    print("********* MENÚ **********")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("*************************")

    # PASO 2: Pedir al usuario ingrese una opción

    opcion = int(input("Ingrese su opción: "))

    # PASO 3: La compu tiene que decidir

    if opcion == 1:
        numero1 = 15
        numero2 = 45
        
        suma = numero1 + numero2
        
        print(f"La suma entre 15 y 45 es: {suma}")

    elif opcion == 2:
        numero1 = 15
        numero2 = 45
        
        resta = numero1 - numero2
        
        print(f"La resta entre 15 y 45 es: {resta}")

    elif opcion == 3:
        numero1 = 15
        numero2 = 45
        
        multiplica = numero1 * numero2
        
        print(f"La multiplicación entre 15 y 45 es: {multiplica}")
        
    elif opcion == 2:
        numero1 = 15
        numero2 = 45
        
        division = numero1 - numero2
        
        print(f"La resta entre 15 y 45 es: {resta}")

    else:
        print("Opción incorrecta!")
