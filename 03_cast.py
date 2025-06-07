## conversión de tipos

print("Conversión de tipos")
print(2 + int("3"))  # Convertir cadena a entero
print(2 + float("3.5"))  # Convertir cadena a flotante
print("100" + str(200))  # Convertir entero a cadena
print(int(3.1416))  # Convertir flotante a entero (truncamiento)
print(bool(1))  # Convertir entero a booleano (1 es True, 0 es False)
print(bool(0))  # Convertir entero 0 a booleano (False) 
print(bool(-1))  # Convertir entero negativo a booleano (True)
print(bool(""))  # Convertir cadena vacía a booleano (False)
print(bool("Hello"))  # Convertir cadena no vacía a booleano (True)
