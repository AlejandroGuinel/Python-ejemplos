import math
import random


#print("hola mundo cruel!!!!")

# VARIABLES
nombre = "cristian"
edad = 19
altura = 2.00
es_profesor = True
ciudad = "valparaiso"


#TIPOS DE DATOS
str #esto es un texto
int #esto es un entero
float #esto es un flotante 
bool #esto es verdadero  o falso
list

#INPUT
#input()


#numero = int(input("escribe un numero : "))
#resultado = numero + 1
#print(resultado)
#

#INPUT
""" precio = input("escribe un precio : ")# pedir por consola un dato tipo str
precio = int(precio) #convertir a entero el str con int(precio)
resultado = precio + 10 #el precio sumado + 10 ya que ahora es numero entero
print(resultado)# imprimeme el precio en pantalla """

## CONDICIONALES


#if condicion:
#    codigo
#comparadores
""" 
== igual
!= diferente
> mayor
< menor
>= mayor o igual
<= menor o igual 
"""


edad = 20

""" if edad >= 18:
    print("puede entrar a la disco")
elif edad >= 50:
    print("demaciado antiguo!!")
else:
    print("no puede entrar a la disco")     
 """

#BUCLES

#WHILE
#while condicion:
#    codigo
# while significa mientras pase algo
contador = 0

""" while contador < 10:
    print(contador)
    contador += 1
 """
""" while True:
    texto = input("escribe para salir de bucle")

    if texto == "salir":
        break """


#FOR

#for elemento in lista
#    codigo
""" lista = ["hola","a","todos"]

for i in lista:
    print(i) """


## tipos de datos 2 

## listas
lista = [1,2,3,4,5,6]  ## corchetes son importantes
## 
diccionario = {"key":"value"}
##sets
sets={}
##tuplas
tuplas = ()



## listas
##index
frutas = ["manzana","uva","kiwi","sandia", [1,2,3,4,[5,6,7]]]
    #index   0        1      2      3           4         = posicion 
    #        -5      -4     -3     -2            -1
frutas[3] = "pera"
frutas[0] = "algo"
frutas[4] = [] #lista vacia

""" print(frutas[2])
print(frutas[1])
print(frutas[0])
print(frutas[4][4][0]) """

""" print(frutas[-4])

#print(dir(diccionario))

#append
frutas.append("naranja")  #agrega un item al final de la lista 

##remove
frutas.remove("kiwi")

print(frutas)

personas = ["cristian","esteban"]

for i in personas:
    print(i)
 """
 
""" alumnos = [] #lista vacia

while True:
    print("----------menu")
    print("opcion 1 agregar")
    print("opcion 2 borrar")
    print("opcion 3 actualizar")
    print("opcion 4 salir")
    opcion = input("ingresa la opcion :")


    if opcion == "1":
        nombre = input("ingresa el nombre alumno")
        alumnos.append(nombre)
        print(alumnos)
    elif opcion == "2":
        nombre = input("ingresa el nombre alumno")
        alumnos.remove(nombre)
        print(alumnos)
    elif opcion == 3:
        print("buscar alumno")
    else:
        break  """

alumnos = ["carlos", "manuel"]





for i in range(0):
    print(i)



#rango si le paso 4 me genera = 0,1,2,3
#10  = 0,1,2,3,4,5,6,7,8,9


numeros = [1,2,3,4,5,6,7,8,9,10,1,2,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
ordenados = sorted(numeros , reverse=True)
print(ordenados)


#slices donde corto
texto = "palabra"
palindromo = "palabra"
if palindromo == texto[::-1]:
    print("esto es un palindromo!!!!")

print(texto[::-1]) 


print(texto.count("a"))
    
    
    


       
   






















##diccionarios




















