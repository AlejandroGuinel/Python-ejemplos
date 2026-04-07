# 1. Clase Autor
class Autor:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais


# 2. Clase Editorial (composición)
class Editorial:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad


# 3. Clase Libro
class Libro:
    def __init__(self, titulo, autor, anio_publicacion, nombre_editorial, ciudad_editorial):
        self.titulo = titulo
        self.autor = autor  # objeto Autor
        self.anio_publicacion = anio_publicacion
        
        # Composición
        self.editorial = Editorial(nombre_editorial, ciudad_editorial)

    def mostrar_info(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor.nombre)
        print("País del autor:", self.autor.pais)
        print("Año de publicación:", self.anio_publicacion)
        print("Editorial:", self.editorial.nombre)
        print("Ciudad editorial:", self.editorial.ciudad)

    # Getters y Setters
    def get_titulo(self):
        return self.titulo

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def get_anio_publicacion(self):
        return self.anio_publicacion

    def set_anio_publicacion(self, nuevo_anio):
        self.anio_publicacion = nuevo_anio

    # Sobrecarga simulada
    def resumen(self, texto=None):
        if texto is None:
            print("Libro sin resumen disponible")
        else:
            print("Resumen:", texto)


# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------

# Autor chileno
autor1 = Autor("Marcela Paz", "Chile")

# Libro Papelucho
libro1 = Libro("Papelucho", autor1, 1947, "Editorial Universitaria", "Santiago")

# Mostrar info
libro1.mostrar_info()

print("\n--- Modificando título ---")
libro1.set_titulo("Papelucho (Edición especial)")
print("Nuevo título:", libro1.get_titulo())

print("\n--- Resumen ---")
libro1.resumen()
libro1.resumen("Las aventuras de un niño chileno curioso y travieso.")