
# 1. Exploración teórica

# ¿Qué es la programación orientada a objetos?
# Es un paradigma de programación que organiza el código en objetos,
# los cuales combinan datos (atributos) y funciones (métodos).
# ¿En qué se diferencia de la programación estructurada?
# La programación estructurada se basa en funciones y procedimientos,
# mientras que la POO organiza el código en objetos que representan
# entidades del mundo real.
# Ejemplo de la vida cotidiana:
# Un auto: tiene atributos como color, marca, velocidad,
# y métodos como acelerar o frenar.



# 2. Definición de una clase simple


class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def ladrar(self):
        print("¡Guau!")


# Crear instancia (objeto)
mi_perro = Perro("Firulais", 3, "Labrador")

# Llamar método
mi_perro.ladrar()


# 3. Diferenciar conceptos

# Clase: es el molde o plantilla (ej: Perro)
# Instancia/Objeto: es el perro creado a partir de la clase (mi_perro)
# Atributo: características del objeto (nombre, edad, raza)
# Estado: valores actuales de esos atributos (Firulais, 3, Labrador)
# Método: función dentro de la clase (ladrar)
# Comportamiento: acción que realiza el objeto (ladrar)



# 4. Principios de POO


class PerroEncapsulado:
    def __init__(self, nombre, edad, raza):
        self._nombre = nombre
        self._edad = edad
        self._raza = raza

    def ladrar(self):
        print("¡Guau!")

    def mostrar_info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Raza: {self._raza}"


# Crear objeto
perro2 = PerroEncapsulado("perro_chocolo", 5, "kiltro")

# Mostrar información
print(perro2.mostrar_info())


# Abstracción:
# Es mostrar solo la información relevante y ocultar los detalles internos.
# En este caso, usamos métodos como mostrar_info() para interactuar
# con el objeto sin acceder directamente a sus atributos.