# 1
#solicitar edad 
edad = int(input("ingresar edad: "))
#evaludar la edad 
if edad >= 18 :
    print("eres mayor de edad")
else:
    print("eres menor de edad") 
    
 
#2 decicion con elif 
calificacion = int(input("ingresar calificacion: "))

if calificacion == 7:
    print("Excelente")
elif calificacion == 6:
    print("Muy bien")
elif calificacion == 5:
    print("Bien")
elif calificacion == 4:
    print("Suficiente")
elif calificacion < 4:
    print("Insuficiente")
else:
    print("Calificación inválida")

 #3 
numero = int(input("ingresar numero: "))

if numero >= 0: 
    if numero == 0:
        print("El número es cero")
    else:
        print("El número es positivo")
else:    print("El número es negativo")

#4
numero_rango = int(input("ingresar número en rango: "))
if 1 <= numero_rango <= 100:
    if numero_rango == 1 or numero_rango == 100:
        print("Estás en un límite permitido")
    else:
        print("Dentro del rango")
else:
    print("Fuera del rango")