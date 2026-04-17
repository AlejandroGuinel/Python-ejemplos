# manejo_errores.py

# 1
print("=== División de dos números ===")
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 / num2
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")


# 2
print("\n=== División con validación ===")
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 / num2
    print(f"El resultado es: {resultado}")
except ValueError:
    print("Error: Debes ingresar solo números.")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")

# 3
class EdadInvalidaError(Exception):
    pass

def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa.")
    else:
        print(f"Edad válida: {edad}")

print("\n=== Validación de edad ===")
try:
    edad = int(input("Ingresa tu edad: "))
    validar_edad(edad)
except EdadInvalidaError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Debes ingresar un número entero.")

# 4
print("\n=== Simulación de archivo ===")
try:
    print("Abriendo archivo...")
    # Simulamos un error
    x = 10 / 0
except ZeroDivisionError:
    print("Ocurrió un error durante el manejo del archivo.")
finally:
    print("Cerrando archivo...")