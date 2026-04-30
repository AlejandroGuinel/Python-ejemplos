from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula
        self.cursos = []

    def inscribirse(self, curso):
        self.cursos.append(curso)

    # Polimorfismo (sobrescritura)
    def mostrar_info(self):
        return f"Estudiante: {self.nombre}, Matrícula: {self.matricula}"