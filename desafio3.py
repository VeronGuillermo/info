# Pedir al usuario que ingrese su nombre.
# Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos para adivinarlo.

nombre = input("¡Bienvenido! ¿Cómo te llamas? ")

print("¡Hola, " + nombre + "! Estoy pensando en un número entre 1 y 100.")
print("Tienes 8 intentos para adivinarlo.")

# Generar aleatoriamente un número entre 1 y100.
from random import randint
numero_aleatoria = randint(1,100)

i = 8

while i > 0:
    # Informar al usuario cuántos intentos le quedan y solicita que ingrese un número 1 al 100.
    print('Te quedan ' + str(i) + ' intentos.')
    numero_ingresado = input('Ingrese un número del 1 al 100: ')

    # Verificar si el número ingresado es un número entero.
    if not numero_ingresado.isdigit():
        print('El numero ingresado debe de ser un Entero!')
        continue

    numero_ingresado = int(numero_ingresado)

    if numero_ingresado < numero_aleatoria:
        print('El número a adivinar es mayor.')
        i -= 1
        continue
    elif numero_ingresado > numero_aleatoria:
        print('El número a adivinar es menor.')
        i -= 1
        continue
    else:
        i -= 1
        print('¡Felicidades, ' + nombre + '! Adivinaste el número en el intento número ' + str(8 - i) + '!')
        break

if i == 0:
    print('Se acabaron los intentos. El número a adivinar era ' + str(numero_aleatoria)) 
        

        

    
        







