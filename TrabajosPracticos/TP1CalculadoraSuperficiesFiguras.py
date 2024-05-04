# 1° paso: Menú de cálculo de superficies de figuras

print("*********************************")
print("  MENÚ DE CÁLCULOS DE SUPERFICIES DE FIGURAS"  )
print("1- CUADRADO")
print("2- RECTÁNGULO")
print("3- TRIÁNGULO")

# 2° paso: Pedir al usuario ingresar opción de menú

opcion = int(input("Elija una opción: "))

# 3° paso: Decidir qué opción trabajar

if opcion == 1:
    print("Estás calculando la superficie de un cuadrado")
    
elif opcion == 2:
    print("Estás calculando la superficie de un rectángulo")
    
elif opcion == 3:
    print("Estás calculando la superficie de un triángulo")

else:
    print("Opción incorrecta!") 
