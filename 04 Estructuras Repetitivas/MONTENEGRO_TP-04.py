# Trabajo Práctico 4 
# Programación I
# Alumno: Montenegro Sergio
# Comisión 17

# Práctico 4: Estructuras repetitivas  

# Ejercicio 1
# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for i in range (101):
    print(i)

# Ejercicio 2
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene.

numero = int(input("Ingrese un número entero: "))
cifras = 0
while numero > 0:
    numero = numero // 10
    cifras += 1 
print(f"El número ingresado tiene {cifras} dígitos.")

# Ejericio 3
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))
# En caso de que el segundo entero sea menor que el primero, los invierto para evitar error en el bucle.
if num1 > num2:
    num3 = num1
    num1 = num2
    num2 = num3
suma = 0
for i in range (num1+1, num2):
    suma += i

print(f"La suma de los números enteros comprendidos entre {num1} y {num2} es igual a {suma}")

# Ejercicio 4
# Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 

numero = int(input("Ingrese un número entero: "))
suma = 0
while numero!= 0:
    suma += numero
    numero = int(input("Ingrese un número entero: "))

print(f"La suma total de los números ingresados es {suma}")

# Ejercicio 5
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

from random import randint

aleatorio = randint(0,9)
numero = int(input("Adivine el número entre 0 y 9: "))
intentos = 1
while numero!= aleatorio:
    numero=int(input("Sin acierto! Elige otro número: "))
    intentos += 1

if intentos == 1:
    print("Felicitaciones!! Acertaste en la primera!!")
else: print(f"Muy bien!! Acertaste en {intentos} intentos!")

# Ejercicio 6
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

for num in range(100, -1, -2):
    print(num)

# Ejercicio 7
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 
 
numero = int(input("Ingrese un número entero positivo :"))
suma = 0
if numero < 0:
    print("Error! Ingreso un número no valido")
else:
    for i in range (1,numero+1):
        suma += i
    print(f"La suma de los números comprendidos entre 0 y {numero} es {suma}")

# Ejercicio 8
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).     

pares = 0
impares = 0
positvos = 0
negativos = 0
tope = 100 # Para pruebas modificar a un valor pequeño
print("Ingrese 100 números enteros...")
for i in range(tope):
    num = int(input("Ingrese un número: "))
    if num%2==0:
        pares +=1
    else:
        impares +=1
    if num>0:
        positvos +=1        
    elif num<0: 
        negativos +=1  

print(f"Se ingresaron {pares} pares")
print(f"Se ingresaron {impares} impares")
print(f"Se ingresaron {positvos} positivos")
print(f"Se ingresaron {negativos} negativos")   

# Ejercicio 9
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor). 

tope = 100 # para pruebas utilizar un valor pequeño
suma = 0
print("Ingrese 100 números enteros...")
for i in range(tope):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero

media = suma / tope
print(f"La media de los 100 números ingresados es: {media}")

# Ejercicio 10
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 


numero = int(input("Ingrese un número: "))
numero_invertido = 0

while numero != 0:
    digito = numero % 10  # Obtiene el último dígito
    numero_invertido = numero_invertido * 10 + digito  
    numero = numero // 10  # Elimina el último dígito del número original

print(f"El número invertido es: {numero_invertido}")