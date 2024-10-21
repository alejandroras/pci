
# Juego de Adivinanza de Números

Este proyecto implementa un juego interactivo en el que el usuario intenta adivinar un número aleatorio generado por la computadora. El jugador recibe retroalimentación sobre si su adivinanza es más alta, más baja o correcta. El juego incluye diferentes niveles de dificultad, un número limitado de intentos y estadísticas del rendimiento de cada partida.

## Características
- Niveles de dificultad: El juego ofrece varios niveles de dificultad predefinidos (fácil, intermedio, difícil) y una opción para que el usuario personalice el rango de números y la cantidad de intentos permitidos.
- Retroalimentación instantánea: El programa informa si la adivinanza del usuario es mayor o menor que el número objetivo.
- Estadísticas del juego: Al final de cada partida, se registran las estadísticas de los juegos jugados, los ganados y el promedio de intentos por juego.
- Reinicio del juego: Después de cada partida, el usuario puede elegir si quiere jugar nuevamente.

## Algoritmo
1. Entrada de datos por parte del usuario:
- Nombre del usuario: El programa solicita al usuario su nombre, el cual será utilizado para personalizar los mensajes durante el juego.
- Selección de la dificultad: El usuario elige entre los niveles de dificultad predefinidos (fácil, intermedio, difícil) o puede optar por personalizar el rango y el número de intentos permitidos. Para gestionar la entrada de texto, se utiliza la librería unidecode, que permite normalizar caracteres acentuados o especiales.
2. Proceso e interacción con el usuario:
- Intentos del usuario: Dependiendo del nivel de dificultad seleccionado, el usuario tiene un número limitado de intentos.
- Adivinanza: El programa pide al usuario que introduzca un número dentro del rango definido. Si el usuario introduce un número fuera de rango o repite un número ya intentado, se le pedirá que ingrese uno nuevo.
- Comparación del número:
    - Si la adivinanza es menor que el número generado, se informa que el número es más bajo.
    - Si la adivinanza es mayor, se le dice que es demasiado alta.
    - Si la adivinanza es correcta, se felicita al usuario y se registra la victoria.
3. Resultados del juego:
- Victoria: Si el usuario adivina el número dentro del límite de intentos, el juego muestra un mensaje de felicitación, incluyendo el número de intentos realizados.
- Derrota: Si el usuario no adivina el número después de agotar todos sus intentos, el programa revela el número correcto y muestra un mensaje de despedida.
- Estadísticas: Al final de cada partida, se muestran las estadísticas acumuladas: juegos jugados, juegos ganados y el promedio de intentos por juego.

## Uso de Librerías
- random: Para generar el número aleatorio que el usuario debe adivinar.
- unidecode: Para normalizar la entrada del usuario, permitiendo manejar texto con caracteres especiales o acentos de manera consistente.