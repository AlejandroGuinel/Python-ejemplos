class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    # "Sobrecarga" simulada usando parámetros opcionales
    def agregar_estudiante(self, estudiante=None, lista_estudiantes=None):
        if estudiante:
            self.estudiantes.append(estudiante)
        elif lista_estudiantes:
            self.estudiantes.extend(lista_estudiantes)

    def mostrar_estudiantes(self):
        return [e.nombre for e in self.estudiantes]
