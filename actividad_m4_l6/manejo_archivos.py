# 1. Escribir en un archivo
archivo = open("datos.txt", "w")

archivo.write("Primera línea de texto\n")
archivo.write("Segunda línea de texto\n")
archivo.write("Tercera línea de texto\n")

archivo.close()

# 2. Leer el archivo completo
archivo = open("datos.txt", "r")

contenido = archivo.read()

print("Contenido completo del archivo:")
print(contenido)

archivo.close()

# 3. Leer línea por línea
archivo = open("datos.txt", "r")

# Leer primera línea
primera_linea = archivo.readline()

print("Primera línea:")
print(primera_linea)

# Leer el resto línea por línea
print("Resto del archivo:")

for linea in archivo:
    print(linea)

archivo.close()

# 4. Añadir contenido (modo append)
archivo = open("datos.txt", "a")

archivo.write("Cuarta línea agregada con append\n")

archivo.close()

# Verificar contenido actualizado
archivo = open("datos.txt", "r")

print("Contenido actualizado:")
print(archivo.read())

archivo.close()

# 5. Atributos y cierre
archivo = open("datos.txt", "r")

print("Nombre del archivo:", archivo.name)
print("Modo de apertura:", archivo.mode)
print("¿Está cerrado?:", archivo.closed)

archivo.close()

print("¿Está cerrado después de close()?:", archivo.closed)