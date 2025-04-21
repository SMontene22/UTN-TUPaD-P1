# Trabajo Práctico 5 
# Programación I
# Alumno: Montenegro Sergio
# Comisión 17

# Práctico 5: Funciones en Python 

# Ejercicio 1
# Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

# programa principal

imprimir_hola_mundo()

# Ejercicio 2
# Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}")

# programa principal

saludar_usuario(input("Ingrese su nombre: "))    

# Ejercicio 3
# Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
# dir los datos al usuario y llamar a esta función con los valores in
# gresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# programa principal

nombre=input("Ingrese su nombre: ")    
apellido=input("Ingrese su apellido: ")
edad=input("Ingrese su edad: ")
residencia=input("Ingrese su residencia: ")
informacion_personal(nombre,apellido,edad,residencia)

# Ejerdicio 4
# Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.

import math

def calcular_area_circulo(radio):
    print(f"El area de un circulo de radio {radio} es {round(math.pi * (radio)**2, 2)}")

def calcular_perimetro_circulo(radio):
    print(f"El perimetro de un circulo de radio {radio} es {round(math.pi * (radio)**2, 2)}")

# programa principal

radio=float(input("Ingrese el radio: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

# Ejerdicio 5
# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.

def segundos_a_horas(segundos):
    print(f"{segundos} segundos equivalen a {round(segundos / 3600, 2)} horas") 

# Programa principal

segundos = int(input("Ingrese los segundos a convertir en horas: "))
segundos_a_horas(segundos)

# Ejercicio 6
# Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{i} x {numero} = {i*numero}")

# Programa principal

numero=int(input("Ingrese un numero para mostrar su tabla de multiplicar: "))
tabla_multiplicar(numero)    

# Ejercicio 7
# Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

def operaciones_basicas(a,b):
    print(f"""
        La suma entre {a} y {b}: {a+b}
        La división entre {a} y {b}: {a/b}
        La multiplicación entre {a} y {b}: {a*b}
        La resta entre {a} y {b}: {a-b}
        """)

# Programa principal

num1 = float(input("Por favor, ingrese un número distinto de 0: "))
num2 = float(input("Por favor, ingrese otro número distinto de 0: "))
operaciones_basicas(num1,num2)

# Ejercicio 8
# Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    print(f"Su IMC es de: {round(peso / altura**2, 2)}")

# Programa principal

peso = float(input("Por favor, ingrese su peso en kilogramos: "))
altura = float(input("Por favor, ingrese su altura en metros: "))
calcular_imc(peso,altura)

# Ejercicio 9
# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius): 
    print(f"{celsius} °C equivalen a {round((9/5)*celsius+32, 2)} °F.")

# Programa principal

celsius = float(input("Por favor, una temperatura en °C: "))
celsius_a_fahrenheit(celsius)

# Ejercicio 10
# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a,b,c):
    print(f"El promedio de los números ingresados es {round((a+b+c)/3, 2)}")


# Programa principal
 
numero_a = float(input("Por favor, ingrese el primer número: "))
numero_b = float(input("Por favor, ingrese el segundo número: "))
numero_c = float(input("Por favor, ingrese el tercer número: "))   
calcular_promedio(numero_a, numero_b, numero_c) 