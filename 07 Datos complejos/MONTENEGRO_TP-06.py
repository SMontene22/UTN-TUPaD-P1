# Trabajo Práctico 6
# Programación I
# Alumno: Montenegro Sergio
# Comisión 17

# Práctico 6: Estructuras de datos complejas   

# Ejercicio 1
# Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios: 
#   ● Naranja = 1200 
#   ● Manzana = 1500 
#   ● Pera = 2300 
# 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
precios_frutas['Manzana']= 1500
precios_frutas['Pera']= 2300

# Ejercicio 2
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
#   ● Banana = 1330 
#   ● Manzana = 1700 
#   ● Melón = 2800

precios_frutas['Banana']= 1300
precios_frutas['Manzana']= 1700
precios_frutas['Melón']= 2800

# Ejercicio 3
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios. 

frutas=list(precios_frutas.keys())

# Ejercicio 4
# Escribí un programa que permita almacenar y consultar números telefónicos. 
#   • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#   • Luego, pedí un nombre y mostrale el número asociado, si existe. 
# Ejemplo: 
#       contactos = {"Juan": "123456", "Ana":"987654"}
#       Consultar: "Juan" -> Muestra "123456"

contactos ={}
for i in range (5):
    nombre=input("Ingrese nombre: ")
    tel=input("Ingrese telefono: ")
    contactos[nombre] = tel

consulta = input("Ingrese el nombre del contacto: ")
if consulta in contactos:
    print(f"El telefono de {consulta} es {contactos[consulta]}")
else: 
    print("El contacto no existe...")    

# Ejercicio 5
#   Solicita al usuario una frase e imprime: 
#   • Las palabras únicas (usando un set). 
#   • Un diccionario con la cantidad de veces que aparece cada palabra. 
#  Ejemplo:     
# Entrada -> "hola mundo hola"
# salidas:
# Palabras_únicas:{"hola","mundo"}
# Recuento:{"hola":2,"mundo":1}

frase=input("Ingrese una frase: ")
palabras=frase.split()
set_frase=set(frase.split())

recuento={}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) +1


print(f"Palabras_únicas: {set_frase}")
print("Frecuencia de palabras:", recuento)

# Ejercicio 6
# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno. 
# Ejemplo: 
#   alunmos ={
#           "Sofía": (10,9,8),
#           "Luis":(6,7,7)}

alumnos = {}
for i in range (3):
    nombre = input("Ingrese el nombre del alumno: ")
    n1 = (int(input(f"Ingrese notas 1 de {nombre}: ")))
    n2 = (int(input(f"Ingrese notas 2 de {nombre}: ")))
    n3 = (int(input(f"Ingrese notas 3 de {nombre}: ")))
    notas=(n1,n2,n3)
    alumnos[nombre] = notas


print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")


# Ejercicio 7
# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2: 
#   • Mostrá los que aprobaron ambos parciales. 
#   • Mostrá los que aprobaron solo uno de los dos. 
#   • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).    

# Represento a los estudiantes con el numero de legajo
parcial1={1001,1003,1004,1005,1008,1010}
parcial2={1001,1002,1003,1006,1008,1009,1010}

#interseccion
aprobados_ambos = parcial1 & parcial2
#diferencia simétrica
aprobados_solo_uno = parcial1 ^ parcial2
#unión
total_aprobados = parcial1 | parcial2

print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)
print("Estudiantes que aprobaron solo uno de los dos:", aprobados_solo_uno)
print("Lista total de estudiantes que aprobaron al menos un parcial:", total_aprobados)

# Ejercicio 8
# Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario: 
#   • Consultar el stock de un producto ingresado. 
#   • Agregar unidades al stock si el producto ya existe. 
#   • Agregar un nuevo producto si no existe. 

productos = {"gpu": 5,"cpu":3,"ram":1,"ssd":0}

consulta = input("Ingrese el producto buscado: ")

if consulta in productos:
    opcion = input("1.- Ver el stock\n"
                   "2.- Actualizar el stock\n")
    
    if opcion == "1":
        print(f"Stock disponible de {consulta}: {productos[consulta]}")
    elif opcion == "2":
        cantidad = int(input("Ingrese la cantidad de productos para incorporar: "))
        productos[consulta] += cantidad
        print(f"El stock actualizado de {consulta} es {productos[consulta]}")  
    else:
        print("Opcion no válida.")
else:
    cantidad=int(input("El producto no existe, ingrese cantidad: "))
    productos[consulta] = cantidad          
    print(f"Stock actualizado - {consulta} : {cantidad}")

# Ejercicio 9    
# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Ejemplo: 
#       agenda={
#           ("lunes","10:00"): "Reunión",
#           ("martes","15:00"): "Clase de inglés"}
# Permití consultar qué actividad hay en cierto día y hora. 

agenda={
       ("lunes","10:00"): "Reunión",
       ("martes","15:00"): "Clase de inglés"}


# Solicitar datos al usuario
dia_consulta = input("Ingrese el día: ").lower()
hora_consulta = input("Ingrese la hora (formato HH:MM): ")
evento = agenda.get((dia_consulta, hora_consulta), "No hay eventos programados en este horario.")

print(f"\nEvento programado: {evento}")

# Ejercicio 10
# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
#   • Las capitales sean las claves. 
#   • Los países sean los valores. 
#   Ejemplo:
#   original = {"Argentina:"Buenos Aires","Chile": "Santiago"}
#   invertido = {"Buenos Aires":"Argentina","Santiago":"Chile"} 
 
original = {"Argentina":"Buenos Aires","Chile": "Santiago"}
print(original)

paises=list(original.keys())
capital = list(original.values())

invertido={}
for i in range(len(paises)):
    invertido[capital[i]]=paises[i]

print(invertido)
