from persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    # Polimorfismo
    def mostrar_info(self):
        return f"Profesor: {self.nombre}, Especialidad: {self.especialidad}"
