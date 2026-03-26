
# 1. Declarar estructuras de datos
lista_numeros = [10, 20, 30]

tupla_colores = ("rojo", "verde", "azul")

set_frutas = {"manzana", "plátano", "naranja"}

diccionario_persona = {
    "nombre": "Alejandro",
    "edad": 32,
    "ciudad": "Osorno"
}

print("Lista:", lista_numeros)
print("Tupla:", tupla_colores)
print("Set:", set_frutas)
print("Diccionario:", diccionario_persona)

# 2 Acceder a elementos
print("Segundo elemento de la lista:", lista_numeros[1])

print("Nombre:", diccionario_persona["nombre"])


# 3 Contar e iterar

print("Cantidad lista:", len(lista_numeros))
print("Cantidad tupla:", len(tupla_colores))
print("Cantidad set:", len(set_frutas))
print("Cantidad diccionario:", len(diccionario_persona))

print("\nRecorriendo lista:")
for numero in lista_numeros:
    print(numero)

print("\nRecorriendo tupla:")
for color in tupla_colores:
    print(color)

print("\nRecorriendo set:")
for fruta in set_frutas:
    print(fruta)

print("\nRecorriendo diccionario:")
for clave, valor in diccionario_persona.items():
    print(clave, ":", valor)

# 4 Modificar estructuras



lista_numeros.append(40)
print("Lista actualizada:", lista_numeros)

set_frutas.add("pera")
print("Set actualizado:", set_frutas)


lista_numeros.remove(20)
print("Lista después de eliminar:", lista_numeros)

diccionario_persona["profesion"] = "Programador"
print("Diccionario actualizado:", diccionario_persona)

