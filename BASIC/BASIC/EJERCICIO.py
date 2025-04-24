print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")
nombre = "Carlos"
ciudad = "Buenos Aires"
print(nombre)
print(ciudad)
print("--------------")
print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None
print("Tipo de a:", type(a))
print("Tipo de b:", type(b))
print("Tipo de c:", type(c))
print("Tipo de d:", type(d))
print("Tipo de e:", type(e))
print("--------------")
print("\nEjercicio 3: Casting de tipos")
cadena = "12345"
numero_entero = int(cadena)
numero_float = float(numero_entero)
print("Número entero:", numero_entero)
print("Número como float:", numero_float)
float_num = 3.99
entero_convertido = int(float_num)
print("Float original:", float_num)
print("Float convertido a entero (se trunca la parte decimal):", entero_convertido)
print("--------------")
print("\nEjercicio 4: Variables")
nombre = "midudev"
edad = 18
altura = 1.90
print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros")
print("--------------")
print("\nEjercicio 5: Números")
resultado = int(round(3.1416) / 2)
print("Valor de PI (aproximado):", 3.1416)
print("PI redondeado:", round(3.1416))
print("División entera de PI redondeado entre 2:", resultado)