# Trabajo Práctico 11 
# Programación I
# Alumno: Montenegro Sergio
# Comisión 17

# Práctico 11: Aplicación de la Recursividad  

# Ejercicio 1
# Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario  

def factorial_recur(num):
    if num == 0:
        return 1
    else:
        return factorial_recur(num-1)*num
    

print("***Programa que muestra los factoriales entre el 1 y un número ingresado***")

num= int(input("Ingrese un número, entero positivo: "))    
if num<=0: 
    print("No ingreso un número entero positivo")
else:
    for i in range (1,num+1):
        print(f"El factotial de {i} es {factorial_recur(i)}")


# Ejercicio 2
# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique.

def fibonacci_recur(posicion):
    if posicion==0:
        return 0
    elif posicion== 1:
        return 1
    else:
        return fibonacci_recur(posicion-1)+fibonacci_recur(posicion-2)
    
print("***Programa que muestra la serie fibonacci completa de un numero ingresado***")

num= int(input("Ingrese la posición de la serie fibonacci que desea ver: "))    
if num<0: 
    print("No ingreso un número entero positivo")
else:
    for i in range (num+1):
        print(f"En la posicion {i} el valor de la serie fibonacci es: {fibonacci_recur(i)}")    


# Ejericio 3
# Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general. 

def potencia(num,expo):
    if expo==1:
        return num
    elif expo==0:
        return 1
    else:
        return num * potencia(num,expo-1)

print("***Programa que muestra la potencia de un número ingresado***")

num=int(input("Ingrese un número para realizar la potencia: "))
expo=int(input("Ingrese a que número quiere hacer la potencia: "))

if expo < 0:
    expo=expo*-1
    print(f"{num} elevado a -{expo} es 1/{potencia(num,expo)}")
else: 
    print(f"{num} elevado a {expo} es {potencia(num,expo)}")

# Ejercicio 4
# Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y 
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este 
# procedimiento: 
#       1. Dividir el número por 2. 
#       2. Guardar el resto (0 o 1). 
#       3. Repetir el proceso con el cociente hasta que llegue a 0. 
#       4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario. 
# Convertir el número 10 a binario: 
# 10 ÷ 2 = 5     resto: 0   
#  5 ÷ 2 = 2     resto: 1   
#  2 ÷ 2 = 1     resto: 0   
#  1 ÷ 2 = 0     resto: 1   
# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010". 

def convertir_bin_recur(num,binario):
    if num / 2 == 0:
        return binario[1:]
    else:
        binario = str(num%2)
        num = num // 2
        return (convertir_bin_recur(num,binario))+binario   

binario=""
num=34
print(convertir_bin_recur(num,binario))  

# Ejercicio 5
# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
# lo es. 
# Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


palabra=input("Ingrese una palabra para determinar si es palindromo, no debe tener espacios, ni tildes: ")

if es_palindromo(palabra):
    print(f"La palabra {palabra} es palindromo")    
else:
    print(f"La palabra {palabra} no es palindromo")


# Ejercicio 6
# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 
#   Restricciones: 
#   No se puede convertir el número a string. 
#   Usá operaciones matemáticas (%, //) y recursión. 
#   Ejemplos: 
#   suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
#   suma_digitos(9)      → 9 
#   suma_digitos(305)    → 8   (3 + 0 + 5) 

def suma_digitos(n):
    if n//10==0:
        return n
    else: 
        return (n % 10) + suma_digitos(n // 10)


num=int(input("Ingrese un numero entero positvo: "))
if num < 0:
    print("No ingreso un numero valido.")
else:
    print(suma_digitos(num))    

# Ejercicio 7
# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque. 
 
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
# pirámide. 
 
# Ejemplos: 
#   contar_bloques(1)   → 1         (1) 
#   contar_bloques(2)   → 3         (2 + 1) 
#   contar_bloques(4)   → 10        (4 + 3 + 2 + 1)    

def contar_bloques(n):
    if n==0:
        return 0
    else:
        return n + contar_bloques(n-1)


num=int(input("Ingrese la cantidad de niveles de la pirámide: "))
print(f"Para una pirámide de {num} niveles, necesita {contar_bloques(num)} bloques")

# Ejercicio 8
# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número. 
# Ejemplos: 
#   contar_digito(12233421, 2)   → 3   
#   contar_digito(5555, 5)       → 4 
#   contar_digito(123456, 7)     → 0

def contar_digito(numero, digito):
    if numero ==0:
        return 0
    else:
        if numero%10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
        

print("***Programa que cuenta los digitos que existen en un numero ingresado***")
num = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito entre 0 y 9: "))

print(contar_digito(num, digito))   
