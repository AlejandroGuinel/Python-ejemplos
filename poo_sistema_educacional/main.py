from estudiante import Estudiante
from profesor import Profesor
from curso import Curso

# Interacción entre objetos

def main():
    # Crear objetos
    estudiante1 = Estudiante("Ale", 25, "A001")
    estudiante2 = Estudiante("Juan", 22, "A002")

    profesor = Profesor("Carlos", 40, "Matemáticas")

    curso = Curso("Programación")

    # Agregar estudiantes (sobrecarga)
    curso.agregar_estudiante(estudiante=estudiante1)
    curso.agregar_estudiante(lista_estudiantes=[estudiante2])

    # Inscribir estudiante en curso
    estudiante1.inscribirse(curso)
    estudiante2.inscribirse(curso)

    # Mostrar información (polimorfismo)
    print(estudiante1.mostrar_info())
    print(profesor.mostrar_info())

    # Mostrar estudiantes del curso
    print("Estudiantes en el curso:", curso.mostrar_estudiantes())


if __name__ == "__main__":
    main()