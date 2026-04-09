#ejercicio 1 



while True:
    numero = int(input("Ingrese un número: "))

    if numero <= 0 or numero > 100:
        print("No es posible realizarlo. Intente nuevamente.\n")
        continue

    # Número par
    if numero % 2 == 0:
        print("Usted ha ingresado un número par y los números pares siguientes son:")
        for i in range(numero + 2, 101, 2):
            print(i, end=" ")

    # Número impar
    else:
        print("Usted ha ingresado un número impar y los números impares siguientes son:")
        for i in range(numero + 2, 100, 2):
            print(i, end=" ")

    break

#ejercicio 2

notas = []

for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1} (0 a 10): "))
    
    while nota < 0 or nota > 10:
        nota = float(input("Nota inválida. Ingrese nuevamente (0 a 10): "))
    
    notas.append(nota)

print("\nNotas ingresadas:", notas)

promedio = sum(notas) / len(notas)
print("Nota media:", promedio)

print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

#ejercicio 3 


meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

numero = int(input("Ingrese un número de mes (1-12): "))

if numero < 1 or numero > 12:
    print("Mes inválido")
else:
    print(f"El mes es {meses[numero-1]} y tiene {dias[numero-1]} días.")