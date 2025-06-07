# Variables
my_string_variable = "Hello, World!"
my_integer_variable = 42

print(my_string_variable)
print(my_integer_variable)


print(my_string_variable, my_integer_variable, ", ",".\n")

# Built-in functions
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/02_Day_Variables_builtin_functions/02_variables_builtin_functions.md

mi_nombre = "Juan"
mis_apellidos = "Perez"
mi_edad = 30

print("Mi nombre es", mi_nombre, "y mis apellidos son", mis_apellidos, "y tengo", mi_edad, "años.")

# Variables en una sola línea
mi_nombre, mis_apellidos, mi_edad = "Pablo", "Lopez", 23
print("Mi nombre es", mi_nombre, "y mis apellidos son", mis_apellidos, "y tengo", mi_edad, "años.")

prueba_tipo = 1
print(1 + prueba_tipo)

prueba_tipo = "1"
# print(1 + prueba_tipo)  # Esto causará un error porque no se puede sumar un entero y una cadena

# ¿forzamos el tiop de dato?
address: str = "123 Main St, Springfield, USA"
# Tipado en vsc que avisa del tipo de dato esperado, pero no lo fuerza en tiempo de ejecución
address = 123  # Esto cambiará el tipo de dato a entero, lo cual no es recomendable si se espera una cadena
print(type(address))  # Esto imprimirá <class 'int'>, ya que ahora address es un entero

#input
#user_input = input("Por favor, introduce tu nombre: ")
#print("Hola,", user_input)

# print
print ("Esto", "es", "una", "prueba", sep=" - ", end="!!!")
print("Seguimos con otra línea. pero no hay salto de línea")

print(f"Mi nombre es {mi_nombre} y tengo {mi_edad} años.")
# Formateo de cadenas
print("Mi nombre es {} y tengo {} años.".format(mi_nombre, mi_edad))
# Formateo de cadenas con f-strings
print("Mi nombre es {0} y tengo {1} años.".format(mi_nombre, mi_edad))
# Formateo de cadenas con f-strings

# Tipado en vsc que avisa del tipo de dato esperado, pero no lo fuerza en tiempo de ejecución
#age = input("Por favor, introduce tu edad: \n")
#print(f"Tu edad dentro de 20 años será {age + 20} años.") #en el input se recibe un string, por lo que no se puede sumar directamente a un entero

# Asignar múltiples variables en una sola línea desde el input
print("Obtener múltiples variables desde el input")
countr, city = input("En qué país y ciudad vives? (separados por coma): ").split(",")
print(f"Vives en {city} que está en {countr}.")


