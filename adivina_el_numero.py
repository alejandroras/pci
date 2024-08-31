#ADIVINA EL NÚMERO
# ideas a implementar al codigo
# crear niveles de dificultad en los que se aumente el rango de números posibles a adivinar, así como el número de intentos que el usuario tiene
# crear un nivel personalizado en el que el usuario pueda escoger el rango de números a adivinar así como el número de intentos que tiene
# crear un modo multijugador
# que el usuario solamente pueda dar números cuando haga su intento de adivinar
# que el usuario no pueda volver a decir un número que ya haya dicho antes para que así no pierda intentos
# hacer una interfaz gráfica simple, puede ser con Tkinter o algo similar
# dependiendo de la dificultad seleccionada la máquina proporcionará pistas como: "Te queda un intento, aquí tienes una pista: el número es par"
# crear un sistema en el que el usuario pueda canjear pistas a cambio de intentos restantes, entre mejor sea la pista más intentos costará
# una opción de jugar nuevamente que mantenga un historial de las partidas y resultados pasados
# implementar un sistema de puntuación basado en la cantidad de intentos y dificultad seleccionada en el juego
import random

intentos = 0
numero_min = 1
numero_max = 20

print("Hola! Cuál es tu nombre?: ")
username = input().title()
numero_pensado = random.randint(numero_min, numero_max)

intentos_permitidos = 6

print("Bueno, " + username + " . Estoy pensando en un número entre el " + str(numero_min) + " y " + str(numero_max))

while intentos < intentos_permitidos:
    while True:
        try:
            adivina = int(input("Dime un número: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido.")

    intentos += 1

    if adivina < numero_pensado:
        print("Tu número es menor al que estoy pensando.")
    elif adivina > numero_pensado:
        print("Tu número es mayor al que estoy pensando.")
    elif adivina == numero_pensado:
        print(f"Me ganaste {username}! Adivinaste el número en {intentos} intentos.")
        break

if adivina != numero_pensado:
    print(f"¡Has fallado! El número en el que estaba pensando era {numero_pensado}!\n¡Buena suerte para la próxima!")


#Implementar funciones