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

def configuración_juego():
    print("Hola! ¿Cuál es tu nombre?: ")
    username = input().title()

    while True:
        
        dificultad = input("Selecciona el nivel de dificultad (fácil, intermedio, difícil, personalizado): ").lower()
        
        if dificultad == "fácil":
            numero_min = 1
            numero_max = 10
            intentos_permitidos = 6
            break
        
        elif dificultad == "intermedio":
            numero_min = 1
            numero_max = 20
            intentos_permitidos = 5
            break
        
        elif dificultad == "difícil":
            numero_min = 1
            numero_max = 50
            intentos_permitidos = 4
            break
        
        elif dificultad == "personalizado":
            numero_min = int(input("Ingresa el número mínimo del rango a adivinar: "))
            numero_max = int(input("Ingresa el número máximo del rango a adivinar: "))
            intentos_permitidos = int(input("Ingresa el número de intenots permitidos: "))
            break
        
        else:
            print("Selección inválida. Elige entre fácil, medio ,difícil o personalizado")
    
    return username, numero_min, numero_max, intentos_permitidos

def obtener_adivinanza(intentos_ya_realizados):
    while True:
        try:
            adivina = int(input("¿En qué número estoy pensando?: "))
            if adivina in intentos_ya_realizados:
                print("Ya habías intentado ese número. Prueba con otro.")
            else:
                return adivina
        except ValueError:
            print("Introduce un número válido.")

def checar_adivinanza(adivina, numero_pensado):
    if adivina < numero_pensado:
        print("Tu número es menor al que estoy pensando.")
        return False
    elif adivina > numero_pensado:
        print("Tu número es mayor al que estoy pensando.")
        return False
    elif adivina == numero_pensado:
        print("Me ganaste! Adivinaste el número!")
        return True

def jugar_de_nuevo():
    respuesta = input("¿Te gustaría volver a jugar? (Sí/No): ").lower()
    return respuesta == "sí"


print("Bienvenido al juego de Adivina el Número!")

while True:
    username, numero_min, numero_max, intentos_permitidos = configuración_juego()
    numero_pensado = random.randint(numero_min, numero_max)
    intentos = 0
    intentos_previos = set()

    print(f"Bueno, {username}, estoy pensando en un número entre el {numero_min} y el {numero_max}.")

    while intentos < intentos_permitidos:
        adivina = obtener_adivinanza(intentos_previos)
        intentos += 1
        intentos_previos.add(adivina)

        if checar_adivinanza(adivina, numero_pensado):
            print(f"\nAdivinaste el número en {intentos} intentos.")
            break
    
    if adivina != numero_pensado:
        print(f"Has fallado! El número en el que estaba pensando era {numero_pensado}.\n ¡Buena suerte para la próxima!")
        
    if not jugar_de_nuevo():
        print("¡Gracias por jugar! Hasta la próxima.")
        break