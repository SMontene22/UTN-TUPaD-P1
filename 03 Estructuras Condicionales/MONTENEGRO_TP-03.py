# Trabajo Práctico 3 
# Programación I
# Alumno: Montenegro Sergio
# Comisión 17

# Práctico 3: Estructuras condicionales  

# Ejercicio 1
# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

# Ejercicio 2
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
# mensaje “Desaprobado”.      

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else: 
    print("Desaprobado")    

# Ejecicio 3
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
# operador de módulo (%) en Python para evaluar si un número es par o impar. 
 
numero = int(input("Ingrese un número par: "))
if (numero % 2) == 0:
    print("Ha ingresado un número par")
else: 
    print("Por favor, ingrese un número par")       

# Ejercicio 4
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece: 
#       ● Niño/a: menor de 12 años. 
#       ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#       ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#       ● Adulto/a: mayor o igual que 30 años.     

edad = int(input("Ingrese su edad: "))
if edad>= 0 and edad <12:
    print("Usted es un Niño/a")
elif edad>=12 and edad<18:
    print("Usted es un Adolescente")
elif edad>=18 and edad<30:
    print("Usted es un Adulto/a joven")
else: 
    print("Usted es un Adulto/a mayor") 

# Ejercicio 5
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
# como una lista o un string.            

password = input("Ingrese su contraseña: ")
if len(password)>= 8 and len(password)>= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres" )

# Ejercicio 6
# El paquete statistics de python contiene funciones que permiten tomar una lista de números 
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el 
# siguiente: 
# from statistics import mode, median, mean 
# mi_lista = [1,2,5,5,3] 
# mean(mi_lista) 
# En la documentación oficial se puede encontrar más información sobre este paquete: 
# https://docs.python.org/es/3.8/library/statistics.html.  
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
#       ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
#       mediana es mayor que la moda. 
#       ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
#       la mediana es menor que la moda. 
#       ● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
# Definir la lista numeros_aleatorios de la siguiente forma: 
# import random 
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
# forma aleatoria.

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
if (mean(numeros_aleatorios) > median(numeros_aleatorios)) and (median(numeros_aleatorios) > mode(numeros_aleatorios)):
    print("Hay Sesgo positivo o a la derecha") 
elif (mean(numeros_aleatorios)< median(numeros_aleatorios)) and (median(numeros_aleatorios) < mode(numeros_aleatorios)):
    print("Hay Sesgo negativo o a la izquierda")
elif mean(numeros_aleatorios) == median(numeros_aleatorios) == mode(numeros_aleatorios):
    print("sin sesgo")

# Ejercicio 7
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla.

frase = input("Ingrese una frase o palabra: ").lower
if frase[-1] in "aeiou":
    frase += "!"
print(frase)    

# Ejercicio 8
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
#       1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#       2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#       3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")
print(f"Seleccione una opción: \n"  
      "1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. \n"
      "2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. \n"
      "3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
opcion=input("Ingrese el número de la opción deseada (1, 2 o 3): ") 

if opcion=="1":
    nombre_convertido = nombre.upper()
elif opcion == "2":
    nombre_convertido = nombre.lower()
elif opcion == "3":
    nombre_convertido = nombre.title()
else:
    nombre_convertido = "Opcion no válida!" 
print(nombre_convertido)

# Ejercicio 9
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
# por pantalla: 
#   ● Menor que 3: "Muy leve" (imperceptible). 
#   ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#   ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#       generalmente no causa daños). 
#   ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#       débiles). 
#   ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#   ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

terremoto = float(input("Ingrese la magnitud del terremoto: "))
print("**Clasificación del Terremoto en la escala de Richter**\n")
if terremoto< 3:
    print('"Muy leve" (imperceptible)')
elif terremoto >=3 and terremoto < 4:
    print('"Leve" (ligeramente perceptible)')
elif terremoto >=4 and terremoto < 5:
    print('"Moderado" (sentido por personas, pero generalmente no causa daños)')
elif terremoto >=5 and terremoto < 6:
    print('"Fuerte" (puede causar daños en estructuras débiles)')
elif terremoto >=6 and terremoto < 7:
    print('"Muy Fuerte" (puede causar daños significativos)')
elif terremoto >=7: 
    print('"Extremo" (puede causar graves daños a gran escala).')
   
# Ejercicio 10
# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
# Periodo del año                               Estación en el                          Estación en el
#                                               hemisferio norte                        hemisferio sur 
#                                                                                   
# Desde el 21 de diciembre hasta el 20 de       Invierno                                Verano
# marzo (incluidos) 
# Desde el 21 de marzo hasta el 20 de junio     Primavera                               Otoño
# (incluidos) 
# Desde el 21 de junio hasta el 20 de           Verano                                  Invierno
# septiembre (incluidos) 
# Desde el 21 de septiembre hasta el 20 de      Otoño                                   Primavera
# diciembre (incluidos) 

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese en que hemisferio se encuentra (N/S)").upper()
mes = int(input("Ingrese en que mes se encuentra: "))
dia = int(input("Ingrese en que día se encuenta: "))


if dia < 21:
    if mes>9 and mes<=12:
        if hemisferio=="S":
            print("Estas en Primavera.")
        else:
            print("Estas en Otoño.")    
    elif mes>6 and mes<=9:
            if hemisferio=="S":
                print("Estas en Invierno.")
            else:
                print("Estas en Verano.") 
    elif mes>3 and mes<=6:
            if hemisferio=="S":
                print("Estas en Otoño.")
            else:
                print("Estas en Primavera.")       
    elif mes>1 and mes<=3:
            if hemisferio=="S":
                print("Estas en Verano.")
            else:
                print("Estas en Invierno.")
else:
    if (mes==12) or (mes>=1 and mes<3):
            if hemisferio=="S":
                print("Estas en Verano.")
            else:
                print("Estas en Invierno.")
    elif mes>=3 and mes<6:
            if hemisferio=="S":
                print("Estas en Otoño.")
            else:
                print("Estas en Primavera.")  
    elif mes>=6 and mes<9:
            if hemisferio=="S":
                print("Estas en Invierno.")
            else:
                print("Estas en Verano.") 
    elif mes>=9 and mes<12:
        if hemisferio=="S":
            print("Estas en Primavera.")
        else:
            print("Estas en Otoño.")   