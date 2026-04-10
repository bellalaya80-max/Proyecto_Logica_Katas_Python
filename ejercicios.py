# PROYECTO LÓGICA: KATAS DE PYTHON - DATA ANALYTICS
# Alumna: [BELLA LAYA]
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 1: Escribe una función que reciba una cadena de texto como parámetro
# y devuelva un diccionario con las frecuencias de cada letra en la cadena.
# Los espacios no deben ser considerados.

def contar_frecuencias(cadena):
    # Utilizo un diccionario porque me permite organizar los datos en pares (letra: cantidad)
    # y buscar si una letra ya existe de forma mucho más eficiente que en una lista.
    frecuencias = {}

    # Recorremos la cadena letra por letra
    for letra in cadena:
        # Si encontramos un espacio, lo ignoramos
        if letra == " ":
            continue

        # Esta parte fue clave entenderla: paso todo a minúscula para que Python no cuente la 'A' y la 'a' como dos letras distintas.
        letra = letra.lower()

        # Si la letra ya está en el diccionario, sumamos 1
        if letra in frecuencias:
            frecuencias[letra] += 1
        # Si no está, la agregamos con valor 1
        else:
            frecuencias[letra] = 1

    # Devolvemos el diccionario final
    return frecuencias


texto_prueba = "hola mundo"
resultado = contar_frecuencias(texto_prueba)
print(resultado)
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 2: Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map() 

numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros)) # lambda x: x * 2 toma cada elemento 'x' y lo multiplica por 2
print(dobles)
# Al principio la sintaxis de map() y lambda parecía compleja, pero entiendo que 
# sustituyen a un bucle 'for' entero. map() aplica una regla a cada elemento de la lista.
# La regla aquí es 'lambda x: x * 2', una función anónima que toma un número y lo duplica.

# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 3: Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
#devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def filtrar_palabras(palabras, objetivo):
    # Utilizo una lista por su capacidad de almacenar múltiples elementos y mantener el orden.
    resultado = []

    # Recorremos cada palabra en la lista de palabras
    for palabra in palabras:
        # Si la palabra objetivo está dentro de la palabra actual, la agregamos al resultado
        if objetivo in palabra:
            resultado.append(palabra)

    # Devolvemos la lista con las palabras filtradas
    return resultado

palabras = ["manzana", "banana", "cereza", "manzana verde", "pera"]
objetivo = "manzana"

print(filtrar_palabras(palabras, objetivo))
# En este ejercicio, la función filtrar_palabras busca dentro de cada palabra de la lista
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 4: Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
def diferencia_listas(lista1, lista2):
    # Utilizo map() para aplicar una función que reste cada elemento de lista2 a su correspondiente en lista1
    return list(map(lambda x, y: x - y, lista1, lista2)) # La operación x - y calcula la diferencia, y list() empaqueta todos los resultados en una nueva lista.
# Prueba del código
numeros = [10, 20, 30, 40]
numeros2 = [1, 2, 3, 4]
print(diferencia_listas(numeros, numeros2)) # Llamamos a la función y le pedimos a Python que imprima lo que nos devuelve
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 5: Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
#defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
#que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
#una tupla que contenga la media y el estado.
def evaluar_rendimiento(numeros, nota_aprobado=5):
    # Entiendo que al poner '=5' en el parámetro, estoy definiendo un valor por defecto.
    # Si quien usa la función no proporciona este dato, Python usará el 5 automáticamente.

    media = sum(numeros) / len(numeros)  # Calculamos la media sumando todos los números y dividiendo por la cantidad de números

    # Determinamos el estado comparando la media con la nota de aprobado
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    # Finalmente, devuelvo los dos valores agrupados en una tupla usando paréntesis ().
    return (media, estado)

notas_estudiante_1 = [4, 6, 5, 5]
print(evaluar_rendimiento(notas_estudiante_1)) # Llamamos a la función con una lista de notas y dejamos que use el valor por defecto de nota_aprobado
# ------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 6: Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(numero):
    # Si el número es 0 o 1, devolvemos 1 porque ahí termina la recursividad
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)  # Si no, multiplicamos el número actual por el factorial del número anterior
    
print(factorial(5)) # Llamamos a la función para calcular el factorial de 5
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 7: Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def convertir_tuplas_a_strings(lista_tuplas):
    return list(map(lambda tupla: f"{tupla[0]} - {tupla[1]}", lista_tuplas))

tuplas = [("Paola", 25), ("Luis", 30), ("Marta", 22)]
print(convertir_tuplas_a_strings(tuplas))
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 8: Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.
def dividir_numeros():
    # Entiendo que al interactuar con el usuario, los datos ingresados pueden ser erróneos.
    # Utilizo el bloque 'try' para indicarle a Python que intente ejecutar estas líneas, 
    # pero sabiendo que podrían fallar.
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        resultado = num1 / num2

    except ValueError:
        print("Error: Por favor, ingresa un valor numérico válido.")
    # Este except previene el colapso matemático que ocurre al intentar dividir por cero.
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    else:
        print(f"¡División exitosa! El resultado es: {resultado}")

dividir_numeros() # Llamamos a la función para iniciar el proceso de división
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 9: Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
def filtrar_mascotas(mascotas): #Defino la función que recibe una lista de mascotas como parámetro
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, mascotas)) # filter() aplica la función lambda a cada elemento de la lista 'mascotas' 
#y solo devuelve aquellos que no están en 'mascotas_prohibidas'

lista_mascotas = ["Perro", "Gato", "Mapache", "Tigre", "Hamster", "Serpiente Pitón"]
print(filtrar_mascotas(lista_mascotas)) # Llamamos a la función con una lista de mascotas para ver el resultado filtrado
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 10: Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.
def calcular_promedio(lista_numeros): 
    if len(lista_numeros) == 0: 
        raise ValueError("Cuidado: La lista está vacía. No se puede calcular el promedio.") # Aquí lanzo una excepción personalizada con un mensaje específico
    else:
        return sum(lista_numeros) / len(lista_numeros) # Si la lista no está vacía, calculo el promedio normalmente
# Prueba del código
try:
    lista_prueba = [] # Aquí creo una lista vacía para probar la excepción
    resultado = calcular_promedio(lista_prueba) # Intento calcular el promedio de la lista vacía
    print(f"El promedio es: {resultado} ") # Si no se lanza la excepción, imprimo el resultado
except ValueError as error_personalizado: # Capturo la excepción específica que lancé en la función
    print(error_personalizado) # Si se lanza la excepción, imprimo el mensaje personalizado que definí en la función
# ------------------------------------------------------------------------------------------------------------------------------ 
# EJERCICIO 11: Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.
def validar_edad():  
    try: 
        edad = int(input("Por favor, ingresa tu edad: ")) # Intento convertir la entrada del usuario a un número entero
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120. Por favor, ingresa un número válido.") # Si la edad está fuera del rango, lanzo una excepción personalizada
        else:
            print(f"¡Gracias! Tu edad es {edad} años.") # Si la edad es válida, imprimo un mensaje de agradecimiento con la edad ingresada
    except ValueError as error_detectado: # Capturo cualquier ValueError que pueda ocurrir, ya sea por la conversión a entero o por la validación del rango
        print(f"Error: {error_detectado}") # Imprimo el mensaje de error específico que se haya generado
        
validar_edad() # Llamo a la función para iniciar el proceso de validación de edad
# ------------------------------------------------------------------------------------------------------------------------------ 
# EJERCICIO 12: Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def longitud_palabras(palabras):

    palabras_separadas = palabras.split() # Primero, separo la frase en palabras usando el método split(), que crea una lista de palabras a partir de la cadena original.
    return list(map(lambda palabra: len(palabra), palabras_separadas)) # Utilizo map() para aplicar la función lambda que calcula la longitud de cada palabra en la lista 'palabras'

lista_palabras = "Python Data Analytics Katas" # Aquí creo una lista con una frase para probar la función
print(longitud_palabras(lista_palabras)) # Llamo a la función con una lista de palabras para obtener sus longitudes
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 13: Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
def letras_mayus_minus(frase):
    caracteres_unicos = set(frase) # Utilizo un conjunto (set) para obtener solo los caracteres únicos de la frase, eliminando cualquier repetición.
    return list(map(lambda letra: (letra.upper(), letra.lower()), caracteres_unicos)) # Uso map() para crear una tupla con la letra en mayúscula y minúscula para cada carácter único.
frase_prueba = "Bienvenidos a Python"
print(letras_mayus_minus(frase_prueba)) # Llamo a la función con una frase para obtener la lista de tuplas con las letras en mayúscula y minúscula
# ------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 14: Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
# función filter()
def palabras_especificas(frase, letra_objetivo):
    palabras_separadas = frase.split() # Primero, separo la frase en palabras usando el método split(), que crea una lista de palabras a partir de la cadena original.
    return list(filter(lambda palabra: palabra.lower().startswith(letra_objetivo), palabras_separadas)) # Utilizo filter() para crear una nueva lista que solo incluya las palabras que comienzan con la palabra objetivo.
frase_prueba = "El análisis de datos es fundamental en Python"
letra = "d" # Aquí defino la letra específica con la que deben comenzar las palabras que quiero filtrar
print(palabras_especificas(frase_prueba, letra)) # Llamo a la función con una frase y una palabra objetivo para obtener la lista de palabras que contienen esa palabra
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 15: Crea una función lambda que sume 3 a cada número de una lista dada.
numeros_suma = lambda lista: list(map(lambda x: x + 3, lista)) # Aquí defino una función lambda que toma una lista y utiliza map() para sumar 3 a cada elemento de la lista
numeros = [50,60, 70, 80] # Aquí creo una lista de números para probar la función lambda
print(numeros_suma(numeros)) # Llamo a la función lambda con la lista de números para obtener una nueva lista con cada número incrementado en 3
# ------------------------------------------------------------------------------------------------------------------------------    
# EJERCICIO 16: Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter()
def filtrar_palabras(palabras, longitud_objetivo):
    return list(filter(lambda palabra: len(palabra) > longitud_objetivo, palabras)) # Utilizo filter() para crear una nueva lista que solo incluya las palabras que tienen la longitud específica.
texto = "El gato y el perro corren tras el elefante" # Aquí creo una cadena de texto con varias palabras para probar la función
palabras = texto.split() # Primero, separo la cadena de texto en palabras usando el método split(), que crea una lista de palabras a partir de la cadena original.
longitud = 4 # Aquí defino la longitud específica que deben tener las palabras que quiero filtrar
print(filtrar_palabras(palabras, longitud)) # Llamo a la función con la lista de palabras y la longitud objetivo para obtener la lista de palabras que tienen esa longitud
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 17: Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()
from functools import reduce # Importo la función reduce del módulo functools para poder usarla en el siguiente ejercicio

def convertir_numero(lista):
    return reduce(lambda acumulado, actual: acumulado * 10 + actual, lista) # Utilizo reduce() para aplicar una función lambda que toma un acumulado y el número actual, 
# multiplicando el acumulado por 10 y sumando el número actual. Esto construye el número final a partir de la lista de dígitos.

lista_digitos = [5, 7, 2] # Aquí creo una lista de dígitos para probar la función reduce
resultado = convertir_numero(lista_digitos) # Llamo a la función con la lista de dígitos para obtener el número correspondiente
print(f"La lista {lista_digitos} corresponde al número: {resultado}") # Muestro el resultado
# ------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 18: Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
# 90. Usa la función filter()
estudiantes = [
    {"nombre": "Juana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 85},
    {"nombre": "Paola", "edad": 19, "calificacion": 92},
    {"nombre": "Carlos", "edad": 21, "calificacion": 90}
] # Aquí creo una lista de diccionarios, donde cada diccionario representa a un estudiante con su nombre, edad y calificación
estudiantes_aprobados = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes)) # Utilizo filter() para crear una nueva lista que solo incluya 
# a los estudiantes con calificación mayor o igual a 90
print("Estudiantes con calificación mayor o igual a 90:") # Imprimo un mensaje para indicar qué estudiantes fueron filtrados
for estudiante in estudiantes_aprobados: # Recorro la lista de estudiantes aprobados para mostrar su información
    print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Calificación: {estudiante['calificacion']}") # Imprimo el nombre, edad y calificación de cada estudiante aprobado   
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 19: Crea una función lambda que filtre los números impares de una lista dada
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista)) # Aquí defino una función lambda que toma una lista y utiliza filter() para crear una nueva lista que solo incluya los números impares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Aquí creo una lista de números para probar la función lambda
print(filtrar_impares(numeros)) # Llamo a la función lambda con la lista de números para obtener una nueva lista que solo contenga los números impares
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 20: Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
# filter()
lista_mixed = [1, "hola", 2, "como", 3, "estas", 4] # Aquí creo una lista que contiene tanto números enteros como cadenas de texto para probar la función filter
lista_integers = list(filter(lambda x: isinstance(x, int), lista_mixed)) # Utilizo filter() para crear una nueva lista que solo incluya los valores enteros
print(f"Lista original: {lista_mixed}") # Imprimo la lista original
print(f"Lista con valores enteros: {lista_integers}") # Imprimo la nueva lista con solo los valores enteros
# Me costó deducir la función isinstance(), estaba confundida con la función type(), pero entiendo que isistance() es más adecuada para este caso porque me permite
# verificar si un elemento es de un tipo específico (en este caso, int) y devuelve True o False, lo que es perfecto para usar con filter() para filtrar los elementos de la lista.
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 21: Crea una función que calcule el cubo de un número dado mediante una función lambda
calcular_cubo = lambda x: x ** 3 # Aquí defino una función lambda que toma un número 'x' y devuelve su cubo elevándolo a la potencia de 3
numero = 3 # Aquí defino un número para probar la función lambda
print(f"El cubo de {numero} es: {calcular_cubo(numero)}") # Llamo a la función lambda con el número definido para obtener su cubo y lo imprimo
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 22: Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .
from functools import reduce # Importo la función reduce del módulo functools para poder usarla en el siguiente ejercicio
def producto_total(lista):
    return reduce(lambda x, y: x * y, lista) # Utilizo reduce() para aplicar una función lambda que multiplica dos elementos, acumulando el producto total de la lista
numeros = [2, 3, 4] # Aquí creo una lista de números para probar la función reduce
resultado = producto_total(numeros) # Llamo a la función con la lista de números para obtener el producto total
print(f"El producto total de la lista {numeros} es: {resultado}") # Imprimo el resultado del producto total
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 23: Concatena una lista de palabras.Usa la función reduce()
from functools import reduce # Importo la función reduce del módulo functools para poder usarla en el siguiente ejercicio
def concatenar_palabras(lista):
    return reduce(lambda x, y: x + " " + y, lista) # Utilizo reduce() para aplicar una función lambda que concatena dos palabras con un espacio entre ellas, acumulando la concatenación de toda la lista
palabras = ["Programando", "en", "Python", "es", "divertido"] # Aquí creo una lista de palabras para probar la función reduce
resultado = concatenar_palabras(palabras) # Llamo a la función con la lista de palabras para obtener la concatenación de todas las palabras en una sola cadena
print(f"Las palabras concatenadas son: {resultado}") # Imprimo el resultado de la concatenación de las palabras
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 24: 
# Calcula la diferencia total en los valores de una lista. Usa la función reduce(). 
from functools import reduce # Importo la función reduce del módulo functools para poder usarla en el siguiente ejercicio
def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista) # Utilizo reduce() para aplicar una función lambda que resta dos elementos, acumulando la diferencia total de la lista
numeros = [100, 200, 300] # Aquí creo una lista de números para probar la función reduce, donde el resultado será 100 - 200 - 300 = -400
resultado = diferencia_total(numeros) # Llamo a la función con la lista de números para obtener la diferencia total
print(f"La diferencia total de la lista {numeros} es: {resultado}") # Imprimo el resultado de la diferencia total
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 25: Crea una función que cuente el número de caracteres en una cadena de texto dada.
def numero_caracteres(cadena): 
    return len(cadena) # Utilizo la función len() para calcular el número de caracteres en la cadena, incluyendo espacios y signos de puntuación
texto = "Buenos días, ¿cómo estás?" # Aquí creo una cadena de texto para probar la función
resultado = numero_caracteres(texto) # Llamo a la función con la cadena de texto para obtener el número de caracteres
print(f"La cadena '{texto}' tiene {resultado} caracteres.") # Imprimo el resultado del número de caracteres en la cadena
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 26: Crea una función lambda que calcule el resto de la división entre dos números dados.
calcular_resto = lambda x, y: x % y # Aquí defino una función lambda que toma dos números 'x' e 'y' y devuelve el resto de la división de 'x' entre 'y' utilizando el operador módulo (%)
num1 = 10 # Aquí defino el primer número para probar la función lambda
num2 = 3 # Aquí defino el segundo número para probar la función lambda
print(f"El resto de la división de {num1} entre {num2} es: {calcular_resto(num1, num2)}") # Llamo a la función lambda con los dos números para obtener el resto de su división y lo imprimo
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 27: Crea una función que calcule el promedio de una lista de números.
def calculo_promedio(lista_numeros): 
     return sum(lista_numeros) / len(lista_numeros) # Aquí agrego return para que la función devuelva el resultado del cálculo del promedio, 
# que se obtiene sumando todos los números de la lista y dividiendo por la cantidad de números en la lista. Al principio fue confuso, ya que olvidaba el return, pero entiendo que sin él, 
# la función no devuelve ningún valor y no podríamos usar el resultado fuera de la función.
numeros = [15, 30, 45, 60] # Aquí creo una lista de números para probar la función de cálculo de promedio
resultado = calculo_promedio(numeros)
print(f"El promedio es: {resultado}")
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 28: Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def duplicado_elemento(lista_dada):
    vistos = set() # Utilizo un conjunto (set) para almacenar los elementos que ya hemos visto, porque los conjuntos no permiten duplicados y tienen una búsqueda muy rápida. 
    for item in lista_dada: # Recorro cada elemento de la lista dada
        if item in vistos: 
            return item 
        # Si no está, lo añadimos a nuestra memoria y seguimos
        vistos.add(item)
    return "No se encontraron duplicados"

lista = ["Camiseta", "Sudadera", "Zapatos", "Camiseta", "Vestido", "Sudadera"]
resultado = duplicado_elemento(lista)
print(f"El primer elemento duplicado es: {resultado}")
# En este ejercicio, la función duplicado_elemento recorre la lista dada y utiliza un conjunto para recordar los elementos que ya ha visto.
# Si encuentra un elemento que ya está en el conjunto, significa que es un duplicado y lo devuelve inmediatamente. 
# Si no encuentra ningún duplicado después de revisar toda la lista, devuelve un mensaje indicando que no se encontraron duplicados.
# ------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 29: Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
def enmascarar_variable(variable):
    variable_str = str(variable) # Primero, convierto la variable a una cadena de texto utilizando la función str()
    longitud = len(variable_str) # Luego, calculo la longitud de la cadena resultante para saber cuántos caracteres hay
    if longitud <= 4: 
        return variable_str # Si la longitud es menor o igual a 4, no necesito enmascarar nada, así que devuelvo la cadena tal cual
    else:
        enmascarado = '#' * (longitud - 4) + variable_str[-4:] # Si la longitud es mayor a 4, 
        # creo una nueva cadena que consiste en '#' repetido (longitud - 4) veces seguido de los últimos 4 caracteres de la cadena original
        return enmascarado
    
variable_prueba = "1234567890" # Aquí creo una variable de prueba para convertirla a cadena y enmascararla
resultado = enmascarar_variable(variable_prueba) # Llamo a la función con la variable de prueba para obtener el resultado enmascarado
print(f"Variable original: {variable_prueba}") # Imprimo la variable original
print(f"Variable enmascarada: {resultado}") # Imprimo la variable enmascarada
# -------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 30: Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def son_anagramas(palabra1, palabra2):
    # Primero, convierto ambas palabras a minúsculas para que la comparación no sea sensible a mayúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    # Luego, ordeno las letras de cada palabra y las comparo
    return sorted(palabra1) == sorted(palabra2) # Si las listas de letras ordenadas son iguales, entonces son anagramas

palabra_a = "Amor" # Aquí defino la primera palabra para probar la función de anagramas
palabra_b = "Roma" # Aquí defino la segunda palabra para probar la función de anagramas
resultado = son_anagramas(palabra_a, palabra_b) # Llamo a la función con las dos palabras para verificar si son anagramas
if resultado: #
    print(f"{palabra_a} y {palabra_b} son anagramas.") # Si el resultado es True, imprimo un mensaje indicando que las palabras son anagramas 
else:    print(f"{palabra_a} y {palabra_b} no son anagramas.") # Si el resultado es False, imprimo un mensaje indicando que las palabras no son anagramas
#-----------------------------------------------------------------------------------------------------------------
# EJERCICIO 31: Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
def buscar_nombre():
    nombres = input("Ingresa una lista de nombres separados por comas: ").split(",") # Solicito al usuario que ingrese una lista de nombres separados por comas y los convierto en una lista utilizando split()
    nombre_buscar = input("Ingresa el nombre que deseas buscar: ") # Solicito al usuario que ingrese el nombre que desea buscar en la lista
    if nombre_buscar in nombres: 
        print(f"¡{nombre_buscar} fue encontrado en la lista!") # Si el nombre está en la lista, imprimo un mensaje indicando que fue encontrado
    else:
        raise ValueError(f"Error: {nombre_buscar} no se encuentra en la lista.") # Si el nombre no está en la lista, lanzo una excepción personalizada con un mensaje de error
try:
    buscar_nombre() # Llamo a la función para iniciar el proceso de búsqueda de nombre
except ValueError as error: # Capturo la excepción específica que lancé en la función
    print(error) # Si se lanza la excepción, imprimo el mensaje de error personalizado que definí en la función 
# -------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 32: Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
empleados = {
    "Jacob Black": "Lobo",
    "Michael Jackson": "Cantante",
    "Daenerys Targaryen": "Madre de dragones",
    "Harry Potter": "Mago"
} # Aquí creo un diccionario de empleados, donde cada clave es el nombre completo del empleado y el valor es su puesto o "superpoder"
# Al principio, pensé en usar una lista de tuplas para almacenar los empleados, pero luego me di cuenta de que un diccionario es más adecuado 
# para este caso porque me permite asociar cada nombre completo con su puesto de manera más directa y eficiente.

def buscar_empleado(nombre_completo, base_datos):
    if nombre_completo in base_datos: # Verifico si el nombre completo está en el diccionario de empleados
        return base_datos[nombre_completo] # Si está, devolvemos su "superpoder" (puesto)
    else:
        return "La persona no trabaja aquí"   # Si no está, damos el mensaje de error
    
persona = input("¿A quién buscas?: ")
resultado = buscar_empleado(persona, empleados)
print(f"Resultado: {resultado}") 
# --------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 33: Crea una función lambda que sume elementos correspondientes de dos listas dadas.
lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40] # Aquí primero creo dos listas de números para probar la función lambda que sumará los elementos correspondientes de ambas listas

sumar_listas = list(map(lambda x, y: x + y, lista1, lista2)) # La función lambda toma 'x' (de lista1) e 'y' (de lista2) y los suma.
# map() se encarga de ir pareja por pareja (1 con 10, 2 con 20...)

# Al principio, la sintaxis de map() y lambda parecía un poco confusa, pero ahora entiendo que map() es como un bucle que recorre ambas listas al mismo tiempo,
# aplicando la función lambda a cada par de elementos correspondientes. La función lambda es una forma rápida de definir una función anónima que realiza la suma de dos números.
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Suma de correspondientes: {sumar_listas}") 
# Finalmente, imprimo las dos listas originales y el resultado de la suma de los elementos correspondientes para verificar que la función lambda y map() funcionan correctamente.
#---------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 34: Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
# manipular la estructura del árbol. 
# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
# 6. Implementar el método
# info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
# Caso de uso:
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.

class Arbol:
    def __init__(self):
        self.tronco = 1 # Inicializo el tronco del árbol con una longitud de 1, asignando el valor 1 a self.tronco
        self.ramas = [] # Inicializo la lista de ramas como una lista vacía, asignando una lista vacía a self.ramas para almacenar las longitudes de las ramas que se vayan agregando al árbol

    def crecer_tronco(self):
        self.tronco += 1 # Incremento la longitud del tronco en una unidad sumando 1 al valor actual de self.tronco utilizando el operador += para actualizar el valor del tronco

    def nueva_rama(self):
        self.ramas.append(1) # Agrego una nueva rama de longitud 1 a la lista de ramas utilizando el método append() para añadir un nuevo elemento a la lista

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas] # Utilizo una comprensión de listas para crear una nueva lista de ramas donde cada rama es incrementada 
        # en una unidad sumando 1 a cada elemento de la lista original self.ramas

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas): # Verifico que la posición sea válida (entre 0 y la longitud de la lista de ramas menos 1) para evitar errores de índice
            self.ramas.pop(posicion) # Verifico que la posición sea válida (entre 0 y la longitud de la lista de ramas menos 1) 
            # y luego utilizo el método pop() para eliminar la rama en esa posición
        else:
            print(f"Error: No existe una rama en la posición {posicion}.") # Si la posición no es válida, imprimo un mensaje de error indicando que no existe una rama en esa posición

    def info_arbol(self):
        return (f"--- Estado del Árbol ---\n" #Utilizo un salto de línea (\n) para organizar la información en varias líneas y mejorar la legibilidad del mensaje que se devuelve
                f"Longitud del tronco: {self.tronco}\n"
                f"Cantidad de ramas: {len(self.ramas)}\n"
                f"Longitudes de las ramas: {self.ramas}") 
# Devuelvo una cadena de texto que contiene la información sobre el estado del árbol, incluyendo la longitud del tronco, la cantidad de ramas y las longitudes de cada rama en la lista self.ramas
# CASO DE USO 
# 1. Crear un árbol
mi_arbol = Arbol()
# 2. Hacer crecer el tronco una unidad (Pasa de 1 a 2)
mi_arbol.crecer_tronco()
# 3. Añadir una nueva rama (Lista: [1])
mi_arbol.nueva_rama()
# 4. Hacer crecer todas las ramas una unidad (Lista: [2])
mi_arbol.crecer_ramas()
# 5. Añadir dos nuevas ramas (Lista: [2, 1, 1])
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()
# 6. Retirar la rama situada en la posición 2 (Elimina el tercer elemento) 
mi_arbol.quitar_rama(2)
# 7. Obtener información sobre el árbol
print(mi_arbol.info_arbol()) # Imprimo la información del árbol utilizando el método info_arbol() para verificar el estado final del árbol después de realizar todas las operaciones anteriores
# Este ejercicio resultó complicado ya que no domino completamente la sintaxis de las clases en Python, pero entiendo que la clase Arbol tiene atributos para el tronco 
# y las ramas, y métodos para manipular esos atributos, según lo visto en clase. 
# Entiendo que este ejercicio es una buena práctica para aplicar los conceptos de programación orientada a objetos, como la encapsulación y la manipulación de atributos y
# métodos dentro de una clase. 
#---------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 36:Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
# Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
# 2. Agregar 20 unidades de saldo de "Bob".
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# 4. Retirar 50 unidades de saldo a "Alicia".
class UsuarioBanco:
    def __init__(self, nombre, saldo, tiene_cuenta): 
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta = tiene_cuenta # Aquí guardamos el True o False que nos den

    def retirar_dinero(self, monto): # Defino el método retirar_dinero que toma un monto como parámetro para intentar retirar esa cantidad del saldo del usuario
        if monto > self.saldo: # Verifico si el monto que se intenta retirar es mayor que el saldo actual del usuario
            raise ValueError(f"Error: Saldo insuficiente. Tienes {self.saldo} e intentas retirar {monto}.")
         # Si intenta sacar más de lo que hay, lanzamos el error con un mensaje personalizado que indique el saldo actual y el monto que se intentó retirar
        else:
            self.saldo -= monto 
# Si el monto es menor o igual al saldo, procedemos a restar el monto del saldo actual del usuario utilizando el operador -= para actualizar el saldo después de la retirada
            print(f"¡Transacción exitosa! Tu nuevo saldo es: {self.saldo}") 

    def transferir_dinero(self, monto, otro_usuario):
# Defino el método transferir_dinero que toma un monto y otro_usuario como parámetros para intentar transferir esa cantidad desde otro_usuario al usuario actual
        if not self.tiene_cuenta: # Verifico si el usuario actual no tiene cuenta corriente
            raise ValueError(f"Error: {self.nombre} no tiene cuenta corriente. No se puede realizar la transferencia.")
        elif not otro_usuario.tiene_cuenta: # Verifico si el otro usuario no tiene cuenta corriente
            raise ValueError(f"Error: {otro_usuario.nombre} no tiene cuenta corriente. No se puede realizar la transferencia.")
        elif monto > otro_usuario.saldo: # Verifico si el monto que se intenta transferir es mayor que el saldo del otro usuario
            raise ValueError(f"Error: Saldo insuficiente en la cuenta de {otro_usuario.nombre}. Tiene {otro_usuario.saldo} e intentas transferir {monto}.")
        else:
            otro_usuario.saldo -= monto 
# Si todas las condiciones anteriores se cumplen, procedemos a restar el monto del saldo del otro usuario utilizando el operador -= para actualizar su saldo después de la transferencia
            self.saldo += monto 
# Luego, sumamos el monto al saldo del usuario actual utilizando el operador += para actualizar su saldo después de recibir la transferencia
            print(f"¡Transferencia exitosa! Tu nuevo saldo es: {self.saldo}") 
# Imprimo un mensaje indicando que la transferencia fue exitosa y mostrando el nuevo saldo del usuario actual después de recibir la transferencia

    def agregar_dinero(self, monto): # Defino el método agregar_dinero que toma un monto como parámetro para agregar esa cantidad al saldo del usuario
        self.saldo += monto # Sumo el monto al saldo actual del usuario utilizando el operador += para actualizar su saldo después de agregar dinero
        print(f"¡Dinero agregado exitosamente! Tu nuevo saldo es: {self.saldo}") 

# CASO DE USO
usuario1 = UsuarioBanco("Alicia", 100, True) # Creo el primer usuario "Alicia" con un saldo inicial de 100 y cuenta corriente (True)
usuario2 = UsuarioBanco("Bob", 50, True) # Creo el segundo usuario "Bob" con un saldo inicial de 50 y cuenta corriente (True)
usuario2.agregar_dinero(20) # Agrego 20 unidades de saldo a "Bob" utilizando el método agregar_dinero
usuario2.transferir_dinero(80, usuario1) 
# Hago una transferencia de 80 unidades desde "Bob" a "Alicia" utilizando el método transferir_dinero, pasando el monto y el otro usuario como argumentos
try: 
    usuario1.retirar_dinero(50) # Retiro 50 unidades de saldo a "Alicia" utilizando el método retirar_dinero, pasando el monto a retirar como argumento
except ValueError as error: # Capturo la excepción ValueError que podría ser lanzada por el método retirar_dinero si el saldo es insuficiente
    print(f"Aviso del Banco: {error}")
# Este ejercicio me ayudó a entender mejor cómo funcionan las clases en Python, cómo definir atributos y métodos, y cómo manejar errores utilizando excepciones.
# Las clases siguen siendo un reto para mí, pero creo que con la práctica y la repetición podré dominar estos conceptos de programación orientada a objetos. 
# Para la realización de este ejercicio, y el anterior, me basé en los ejemplos dictados en clase sobre clases y objetos, además de buscar apoyo en la documentación oficial 
# de Python sobre clases y manejo de excepciones para asegurarme de que estaba utilizando la sintaxis correcta y aplicando los conceptos de manera adecuada.
# --------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 37: Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
# reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .
# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
# que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
# que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto
def contar_palabras(texto):
    palabras = texto.split() # Primero, separo el texto en palabras utilizando el método split(), que crea una lista de palabras a partir de la cadena original
    conteo = {} # Luego, creo un diccionario vacío para almacenar el conteo de cada palabra
    for palabra in palabras: # Recorro cada palabra en la lista de palabras
        if palabra in conteo: 
            conteo[palabra] += 1 # Si la palabra ya está en el diccionario, incremento su conteo en 1
        else:
            conteo[palabra] = 1 # Si la palabra no está en el diccionario, la agrego con un conteo inicial de 1
    return conteo # Devuelvo el diccionario con el conteo de cada palabra

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva) # Utilizo el método replace() para reemplazar todas las ocurrencias de palabra_original por palabra_nueva en el texto y devuelvo el resultado


def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split() 
    resultado = [palabra for palabra in palabras if palabra != palabra_a_eliminar]
    return " ".join(resultado) # Devuelvo el texto con la palabra eliminada

def procesar_texto(texto, opcion, *args):
    """
    Coordina qué herramienta usar según la opción del usuario.
    """
    if opcion == "contar":
        return contar_palabras(texto) # Si la opción es "contar", llamo a la función contar_palabras con el texto y devuelvo su resultado
    elif opcion == "reemplazar":
        if len(args) < 2: 
            raise ValueError("¡Faltan datos! Necesito la palabra original y la nueva.") 
        return reemplazar_palabras(texto, args[0], args[1]) # Si la opción es "reemplazar", verifico que se hayan proporcionado exactamente dos argumentos (palabra_original y palabra_nueva), 
        # luego llamo a la función reemplazar_palabras con el texto y los argumentos correspondientes, y devuelvo su resultado
    elif opcion == "eliminar":
        if len(args) < 1: 
            raise ValueError("¡Falta dato! Necesito saber qué palabra eliminar.")  
        return eliminar_palabra(texto, args[0]) # Si la opción es "eliminar", verifico que se haya proporcionado exactamente un argumento (palabra_a_eliminar), 
        # luego llamo a la función eliminar_palabra con el texto y el argumento correspondiente, y devuelvo su resultado
    else:
        raise ValueError("Error: Opción no válida. Las opciones disponibles son 'contar', 'reemplazar' o 'eliminar'.")
# Si la opción no coincide con ninguna de las opciones válidas, lanzo una excepción con un mensaje de error indicando que la opción no es válida y cuáles son las opciones disponibles
# CASO DE USO
frase = "Python es genial, porque Python es muy potente."
print("--- RESULTADOS ---")

# Prueba 1: Contar palabras, devuelve un diccionario con el conteo de cada palabra en la frase
print(f"Conteo real: {procesar_texto(frase, 'contar')}")

# Prueba 2: Reemplazar "Python" por "SQL", devuelve la frase con todas las ocurrencias de "Python" reemplazadas por "SQL"
print(f"Cambio: {procesar_texto(frase, 'reemplazar', 'Python', 'SQL')}")

# Prueba 3: Eliminar (Sin dejar espacios dobles) la palabra "genial,", devuelve la frase con la palabra "genial," eliminada, sin dejar espacios dobles.
print(f"Limpio: {procesar_texto(frase, 'eliminar', 'genial,')}")
# Este ejercicio me ayudó a practicar la creación de funciones que realizan tareas específicas y cómo coordinar su uso dentro de una función principal que maneja diferentes opciones.
# También me permitió entender mejor cómo manejar argumentos variables en funciones utilizando *args.
# # Para realizar este ejercicio, tuve que utilizar apoyo externo ya que no estaba segura de cómo manejar los argumentos variables. Se logró entender el proceso de creación de funciones y su coordinación para lograr el resultado deseado.
# ---------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 38: Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario. 
def determinar_momento_del_dia(hora):
    if 6 <= hora < 12: 
        return "Es de día." # Si la hora está entre las 6 (inclusive) y las 12 (exclusive), se considera que es de día
    elif 12 <= hora < 18: 
        return "Es de tarde." # Si la hora está entre las 12 (inclusive) y las 18 (exclusive), se considera que es de tarde
    else:
        return "Es de noche." # Si la hora no está en los rangos anteriores, se considera que es de noche
try:
    hora_usuario = int(input("Ingresa la hora del día (0-23): ")) # Solicito al usuario que ingrese la hora del día como un número entero entre 0 y 23
    if 0 <= hora_usuario < 24: 
        resultado = determinar_momento_del_dia(hora_usuario) # Si la hora ingresada es válida, llamo a la función determinar_momento_del_dia con la hora del usuario para obtener el resultado
        print(resultado) # Imprimo el resultado que indica si es de noche, de día o tarde
    else:
        print("Error: Por favor, ingresa una hora válida entre 0 y 23.") # Si la hora ingresada no es válida, imprimo un mensaje de error indicando que se debe ingresar una hora válida
except ValueError:
    print("Error: Por favor, ingresa un número entero para la hora.") # Si el usuario ingresa un valor que no se puede convertir a entero, capturo la excepción ValueError y imprimo un mensaje de error indicando que se debe ingresar un número entero para la hora
# Este ejercicio me ayudó a practicar la creación de funciones que toman decisiones basadas en condiciones (if, elif, else) y cómo manejar la entrada del usuario con validación y manejo de errores utilizando try-except.
# Usé herramientas de apoyo como IA para entender mejor cómo manejar la entrada del usuario y validar que sea un número entero dentro de un rango específico, así como para practicar la lógica de las condiciones para determinar el momento del día.
# ----------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 39:Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
#Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente
def determinar_calificacion(calificacion):
    if 0 <= calificacion < 70: 
        return "Insuficiente" # Si la calificación está entre 0 y 69 (inclusive), se considera insuficiente
    elif 70 <= calificacion < 80: 
        return "Bien" # Si la calificación está entre 70 y 79 (inclusive), se considera bien
    elif 80 <= calificacion < 90: 
        return "Muy bien" # Si la calificación está entre 80 y 89 (inclusive), se considera muy bien
    elif 90 <= calificacion <= 100: 
        return "Excelente" # Si la calificación está entre 90 y 100 (inclusive), se considera excelente
    else:
        return "Error: Calificación fuera de rango. Por favor, ingresa un número entre 0 y 100." # Si la calificación no está en el rango de 0 a 100, devuelvo un mensaje de error indicando que la calificación es inválida

try: 
    calificacion_usuario = int(input("Ingresa la calificación del alumno (0-100): ")) # Solicito al usuario que ingrese la calificación del alumno como un número entero entre 0 y 100
    resultado = determinar_calificacion(calificacion_usuario) # Llamo a la función determinar_calificacion con la calificación del usuario para obtener el resultado
    print(f"La calificación en texto es: {resultado}") # Imprimo el resultado que indica la calificación en texto correspondiente a la calificación numérica ingresada
except ValueError:
    print("Error: Por favor, ingresa un número entero para la calificación.") # Si el usuario ingresa un valor que no se puede convertir a entero, capturo la excepción ValueError y imprimo un mensaje de error indicando que se debe ingresar un número entero para la calificación
# Este ejercicio me ayudó a practicar la creación de funciones que toman decisiones basadas en rangos de valores utilizando condiciones (if, elif, else) y cómo manejar la entrada del usuario con validación y manejo de errores utilizando try-except.
# ----------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 40: Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
import math # Importo el módulo math para poder usar la constante pi en el cálculo del área del círculo
def calcular_area(figura, datos):
    if figura == "rectangulo": 
        if len(datos) != 2: 
            raise ValueError("Error: Para un rectángulo necesito dos datos: base y altura.") 
        base, altura = datos
        return base * altura # El área de un rectángulo se calcula multiplicando la base por la altura

    elif figura == "circulo": 
        if len(datos) != 1: 
            raise ValueError("Error: Para un círculo necesito un dato: el radio.") 
        radio = datos[0]
        return math.pi * radio ** 2 # El área de un círculo se calcula utilizando la fórmula A = πr², donde r es el radio del círculo

    elif figura == "triangulo": 
        if len(datos) != 2: 
            raise ValueError("Error: Para un triángulo necesito dos datos: base y altura.") 
        base, altura = datos
        return (base * altura) / 2 # El área de un triángulo se calcula utilizando la fórmula A = (base * altura) / 2

    else:
        raise ValueError("Error: Figura no válida. Las opciones son 'rectangulo', 'circulo' o 'triangulo'.")
# Si la figura no coincide con ninguna de las opciones válidas, lanzo una excepción con un mensaje de error indicando que la figura no es válida y cuáles son las opciones disponibles
# CASO DE USO
try:
    area_rectangulo = calcular_area("rectangulo", (5, 3)) # Calculo el área de un rectángulo con base 5 y altura 3
    print(f"Área del rectángulo: {area_rectangulo}")

    area_circulo = calcular_area("circulo", (4,)) # Calculo el área de un círculo con radio 4
    print(f"Área del círculo: {area_circulo}")

    area_triangulo = calcular_area("triangulo", (6, 2)) # Calculo el área de un triángulo con base 6 y altura 2
    print(f"Área del triángulo: {area_triangulo}")
except ValueError as error:
    print(error) # Si se lanza alguna excepción durante el cálculo de áreas, capturo la excepción ValueError y imprimo el mensaje de error correspondiente
# Este ejercicio me ayudó a practicar la creación de funciones que realizan cálculos específicos basados en diferentes casos utilizando condiciones (if, elif, else) y cómo manejar errores utilizando excepciones para validar los datos de entrada.
# Para realizar este ejercicio, tuve que utilizar apoyo externo (IA) para recordar las fórmulas de cálculo de áreas de diferentes figuras geométricas y para asegurarme de manejar correctamente los casos de error con excepciones.
# ----------------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 41: En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea,
#  después de aplicar un descuento. El programa debe hacer lo siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.
def calcular_precio_final():
    try:
        precio_original = float(input("Ingresa el precio original del artículo: ")) # Solicito al usuario que ingrese el precio original del artículo y lo convierto a un número flotante
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower() # Pregunto al usuario si tiene un cupón de descuento, y normalizo la respuesta para facilitar la comparación

        if tiene_cupon == "sí": 
            valor_cupon = float(input("Ingresa el valor del cupón de descuento: ")) # Si el usuario tiene un cupón, solicito que ingrese su valor y lo convierto a un número flotante
            if valor_cupon > 0: 
                precio_final = precio_original - valor_cupon # Aplico el descuento al precio original restando el valor del cupón
                print(f"Precio final después del descuento: {precio_final:.2f}€") # Muestro el precio final con el descuento aplicado, formateado a dos decimales
            else:
                print("Error: El valor del cupón debe ser mayor a cero. No se aplicará ningún descuento.") # Si el valor del cupón no es válido, imprimo un mensaje de error indicando que no se aplicará ningún descuento
                print(f"Precio final sin descuento: {precio_original:.2f}€") # Muestro el precio final sin aplicar ningún descuento, formateado a dos decimales
        elif tiene_cupon == "no": 
            print(f"Precio final sin descuento: {precio_original:.2f}€") # Si el usuario no tiene un cupón, muestro el precio final sin aplicar ningún descuento, formateado a dos decimales
        else:
            print("Error: Respuesta no válida. Por favor, responde con 'sí' o 'no'.") # Si la respuesta sobre tener un cupón no es válida, imprimo un mensaje de error indicando que la respuesta no es válida

    except ValueError:
        print("Error: Por favor, ingresa un número válido para el precio y el valor del cupón.") # Si el usuario ingresa un valor que no se puede convertir a número, capturo la excepción ValueError y 
 # imprimo un mensaje de error indicando que se debe ingresar un número válido para el precio y el valor del cupón

calcular_precio_final() # Llamo a la función para ejecutar el programa y calcular el precio final de la compra según las condiciones establecidas
# Este ejercicio fue realizado en conjunto con IA. Utilicé este apoyo para agilizar la implementación del programa y asegurarme de que la lógica de control de flujo y manejo de errores estuviera correctamente aplicada.
# Se logró entender cómo utilizar condicionales para tomar decisiones basadas en la entrada del usuario y cómo manejar posibles errores de entrada utilizando excepciones, lo que es fundamental para crear programas robustos y fáciles de usar.
