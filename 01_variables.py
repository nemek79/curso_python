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
address = 123  # Esto cambiará el tipo de dato a entero, lo cual no es recomendable si se espera una cadena
print(type(address))  # Esto imprimirá <class 'int'>, ya que ahora address es un entero

#input
user_input = input("Por favor, introduce tu nombre: ")
print("Hola,", user_input)


