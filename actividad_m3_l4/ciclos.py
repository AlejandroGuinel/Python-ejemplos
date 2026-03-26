
# 1 Uso básico de while

contador = 1

while contador <= 5:
    print(contador)
    contador += 1



# 2 Uso básico de for

#

frutas = ["manzana", "plátano", "naranja"]

for fruta in frutas:
    print(fruta)


# 3 Condición en un ciclo


for numero in range(1, 11):
    if numero % 2 == 0:
        print(numero, "Par")
    else:
        print(numero, "Impar")



# 4 Ciclo infinito controlado con break

while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    
    if numero == 0:
        print("Fin del programa")
        break
    else:
        print("Ingresaste:", numero)



# 5 Ciclo anidado

for i in range(1, 4):
    print(f"\nTabla del {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")



# 6 Uso de continue


nombres = ["Pedro", "Juan", "María", "Luis"]

for nombre in nombres:
    if nombre == "Juan":
        continue
    print(nombre)