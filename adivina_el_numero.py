import random
import unidecode

juegos_jugados = []
juegos_ganados = []
intentos_por_juego = []
estadisticas_partidas = []

def registrar_estadisticas(gano, intentos):
    estadisticas_partidas.append([gano,intentos])

def estadisticas():
    total = len(estadisticas_partidas)
    ganados = 0
    for partida in estadisticas_partidas:
        if partida[0]:
            ganados += 1
    perdidos = total-ganados
    intentos_totales = []
    for partida in estadisticas_partidas:
        intentos_totales.append(partida[1])
    
    if intentos_totales:
        promedio_intentos = sum(intentos_totales) / len(intentos_totales)
    else:
        promedio_intentos = 0
    
    print("\n -- Estadísticas del juego ---")
    print(f"Total de juegos jugados: {total}")
    print(f"Juegos ganados: {ganados}")
    print(f"Juegos perdidos: {perdidos}")
    print(f"Promedio de intentos por juego: {promedio_intentos}")
    print("----------------------------------\n")

def configuración_juego():
    while True:
        
        dificultad = unidecode.unidecode(input("Selecciona el nivel de dificultad (fácil, intermedio, difícil, personalizado): ").lower())
        
        if dificultad == "facil":
            numero_min = 1
            numero_max = 10
            intentos_permitidos = 6
            break
        
        elif dificultad == "intermedio":
            numero_min = 1
            numero_max = 20
            intentos_permitidos = 5
            break
        
        elif dificultad == "dificil":
            numero_min = 1
            numero_max = 50
            intentos_permitidos = 4
            break
        
        elif dificultad == "personalizado":
            while True:
                try:
                    numero_min = int(input("Ingresa el número mínimo del rango a adivinar: "))
                    break
                except ValueError:
                    print("Selección inválida. Por favor ingresa un número entero.")
            while True:
                try:
                    numero_max = int(input("Ingresa el número máximo del rango a adivinar: "))
                    break
                except ValueError:
                    print("Selección inválida. Por favor ingresa un número entero.")
            while True:
                try:
                    intentos_permitidos = int(input("Ingresa el número de intentos permitidos: "))
                    break
                except ValueError:
                    print("Selección inválida. Por favor ingresa un número entero.")
            break
        else:
            print("Selección inválida. Elige entre fácil, intermedio ,difícil o personalizado")
    
    return username, numero_min, numero_max, intentos_permitidos

def obtener_adivinanza(intentos_ya_realizados, numero_min, numero_max):
    while True:
        try:
            adivina = int(input("¿En qué número estoy pensando?: "))
            if adivina in intentos_ya_realizados:
                print("Ya habías intentado con ese número. Prueba con otro.")
            elif adivina not in range(numero_min, numero_max + 1):
                print(f"Por favor, ingresa un número entre el {numero_min} y el {numero_max}.")
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
    return respuesta == "sí" or respuesta == "si"

print("Hola! Bienvenido al juego de Adivina el Número!")
username = input("¿Cuál es tu nombre?: ").title()


while True:
    username, numero_min, numero_max, intentos_permitidos = configuración_juego()
    numero_pensado = random.randint(numero_min, numero_max)
    intentos = 0
    intentos_previos = set()

    print(f"Bueno {username}, estoy pensando en un número entre el {numero_min} y el {numero_max}.")

    while intentos < intentos_permitidos:
        adivina = obtener_adivinanza(intentos_previos, numero_min, numero_max)
        
        if adivina not in intentos_previos:
            intentos += 1
            intentos_previos.add(adivina)
        
        if checar_adivinanza(adivina, numero_pensado):
            print(f"\nAdivinaste el número en {intentos} intentos.")
            registrar_estadisticas(True, intentos)
            break
    
    if adivina != numero_pensado:
        print(f"Has fallado! El número en el que estaba pensando era {numero_pensado}.\n ¡Buena suerte para la próxima!")
        registrar_estadisticas(False, intentos)
        
    if not jugar_de_nuevo():
        print("¡Gracias por jugar! Hasta la próxima.")
        estadisticas()
        break