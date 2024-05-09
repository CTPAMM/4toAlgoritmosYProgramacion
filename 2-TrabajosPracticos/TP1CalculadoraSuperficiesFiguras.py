"""
fecha: 8 de Mayo
curso: 4°2°
estudiante: Fabrina
"""

#1° paso: Menú de calculadora de superficie de figuras

print("***********************************")
print("  MENÚ DE CALCULOS DE SUPERFICIE DE FIGURA"  )
print("1- CUADRADO")
print("2- RECTANGULO")
print("3- TRIANGULO")
print("4- CIRCULO")
#2° paso: Pedir al usuario ingreso opción de menú

opcion = int(input("Elija una opción: "))

#3° paso: Decidir que opción trabajar

if opcion == 1:
    
    lado = int(input("ingrese el valor del lado: "))
    superficieCuadrado = lado ** 2
    
    print(f"La superficie del cuadrado de lado {lado}es: {superficieCuadrado}")
    
    
elif opcion == 2:
    
    base = int(input("ingres el valor de la base: "))
    altura = int(input("ingrese el valor de la altura: "))
    
    superficieRectangulo = base * altura
    
    print(f"La superficie del rectangulo de base {base} y altura {altura} es: {superficieRectangulo}")
    
elif opcion == 3:
   base = int(input("ingres el valor de la base: "))
   altura = int(input("ingrese el valor de la altura: "))
    
   superficieTriangulo = (base * altura)/2
    
   print(f"La superficie del rectangulo de base {base} y altura {altura} es: {superficieTriangulo}")

elif opcion == 4:
    print("Estás calculando la superficie de un circulo")
    
else:
    print("Opción incorrecta!")