# Calculadora para sumar y restar

# PASO 1: Crear un menú de opciones

print("********* MENÚ **********")
print("1- Sumar")
print("2- Restar")
print("*************************")

# PASO 2: Pedir al usuario ingrese una opción

opcion = int(input("Ingrese su opción: "))

# PASO 3: La compu tiene que decidir

if opcion == 1:
    print("El usuario sumará") 

elif opcion == 2:
    print("El usuario restará")

else:
    print("Opción incorrecta!")


