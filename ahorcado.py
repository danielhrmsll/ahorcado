#Módulos necesarios para la aplicación
import random
from colorama import Fore, Style

#Esta función se encarga de ingresar las palabras para el juego.
def ingresar_palabras():
    #Mensajes de bienvenida
    print(Fore.GREEN +  Style.BRIGHT + "¡Bienvenido al juego del Ahorcado!"+Style.RESET_ALL)
    print("Ingresa las palabras que quieres utilizar para jugar.")
    print("Escribe 'listo' cuando hayas terminado." + Style.RESET_ALL)
    #Creamos una lista vacia donde se guardaran las palabras a adivinar.
    palabras = []
    #Ingresamos las palabras a adivinar por teclado
    palabra = input("Ingresa una palabra: ").lower()
    #Ciclo while que se ejecuta hasta que el jugador introduzca listo.
    while palabra != "listo":
        if palabra.strip() != "":
            palabras.append(palabra)
        palabra = input("Ingresa otra palabra (o escribe 'listo' para terminar): ").lower()
    #Condicion if, si no se ingresan palabras, se empezará el juego con palabras predeterminadas.
    if not palabras:
        print(Fore.YELLOW + "No ingresaste ninguna palabra. Se utilizarán palabras por defecto." + Style.RESET_ALL)
        palabras = ["python", "programacion", "diversion", "juego", "computadora", "estudiante", "aprender", "desarrollador"]
    return palabras

#Funcion que selecciona aleatoriamente una palabra de las ingresadas
def seleccionar_palabra(palabras):
    return random.choice(palabras)

#Función que se encarga de mostrar la palabra oculta (con guiones) y actualizarlos por letras cuando se adivina.
def mostrar_palabra(palabra, letras_adivinadas):
    # Inicializamos una variable para almacenar la palabra mostrada al jugador
    palabra_mostrada = ""
    # Recorremos cada letra en la palabra que el jugador debe adivinar
    for letra in palabra:
        # Verificamos si la letra actual está en la lista de letras adivinadas
        if letra in letras_adivinadas:
            # Si la letra está en letras_adivinadas, la agregamos a palabra_mostrada
            palabra_mostrada += letra
        else:
            # Si la letra no está en letras_adivinadas, agregamos un guion bajo (_) a palabra_mostrada
            palabra_mostrada += "_"
    # Devolvemos la palabra mostrada al jugador, con las letras adivinadas y guiones bajos
    return palabra_mostrada

#Función que imprime la "imagen" del ahorcado para cada intento.
def mostrar_ahorcado(intentos):
    ahorcado = [
        [
            Style.BRIGHT+Fore.WHITE + "    ________     ",
            Style.BRIGHT+Fore.WHITE + "   |/      |    ",
            Style.BRIGHT+Fore.WHITE + "   |            ",
            Style.BRIGHT+Fore.WHITE + "   |            ",
            Style.BRIGHT+Fore.WHITE + "   |            ",
            Style.BRIGHT+Fore.WHITE + "   |            ",
            Style.BRIGHT+Fore.WHITE + "_ _|___         " + Style.RESET_ALL
        ],
        [
            Style.BRIGHT+Fore.WHITE + "    ________     ",
            Style.BRIGHT+Fore.WHITE + "   |/      |    ",
            Style.BRIGHT+Fore.WHITE + "   |      " + (Fore.RED + "O" if intentos > 0 else ""),
            Style.BRIGHT+Fore.WHITE + "   |            ",
            Style.BRIGHT+Fore.WHITE + "   |            ",
            Style.BRIGHT+Fore.WHITE + "   |            ",
            Style.BRIGHT+Fore.WHITE + "_ _|___         " + Style.RESET_ALL
        ],
        [
            Style.BRIGHT+Fore.WHITE + "    ________     ",
            Style.BRIGHT+Fore.WHITE + "   |/      |    ",
            Style.BRIGHT+Fore.WHITE + "   |      " + (Fore.RED + "O" if intentos > 0 else ""),
            Style.BRIGHT+Fore.WHITE + "   |      " + (Fore.RED + "|" if intentos > 1 else ""),
            Style.BRIGHT+Fore.WHITE + "   |            ",
            Style.BRIGHT+Fore.WHITE + "   |            ",
            Style.BRIGHT+Fore.WHITE + "_ _|___         " + Style.RESET_ALL
        ],
        [
            Style.BRIGHT+Fore.WHITE + "    ________     ",
            Style.BRIGHT+Fore.WHITE + "   |/      |    ",
            Style.BRIGHT+Fore.WHITE + "   |      " + (Fore.RED + "O" if intentos > 0 else ""),
            Style.BRIGHT+Fore.WHITE + "   |     " + (Fore.RED + "/|" if intentos > 1 else ""),
            Style.BRIGHT+Fore.WHITE + "   |            ",
            Style.BRIGHT+Fore.WHITE + "   |            ",
            Style.BRIGHT+Fore.WHITE + "_ _|___         " + Style.RESET_ALL
        ],
        [
            Style.BRIGHT+Fore.WHITE + "    ________     ",
            Style.BRIGHT+Fore.WHITE + "   |/      |    ",
            Style.BRIGHT+Fore.WHITE + "   |      " + (Fore.RED + "O" if intentos > 0 else ""),
            Style.BRIGHT+Fore.WHITE + "   |     " + (Fore.RED + "/|\\" if intentos > 1 else ""),
            Style.BRIGHT+Fore.WHITE + "   |            ",
            Style.BRIGHT+Fore.WHITE + "   |            ",
            Style.BRIGHT+Fore.WHITE + "_ _|___         " + Style.RESET_ALL
        ],
        [
            Style.BRIGHT+Fore.WHITE + "    ________     ",
            Style.BRIGHT+Fore.WHITE + "   |/      |    ",
            Style.BRIGHT+Fore.WHITE + "   |      " + (Fore.RED + "O" if intentos > 0 else ""),
            Style.BRIGHT+Fore.WHITE + "   |     " + (Fore.RED + "/|\\" if intentos > 1 else ""),
            Style.BRIGHT+Fore.WHITE + "   |     " + (Fore.RED + "/" if intentos > 2 else ""),
            Style.BRIGHT+Fore.WHITE + "   |            ",
            Style.BRIGHT+Fore.WHITE + "_ _|___         " + Style.RESET_ALL
        ],
        [
            Style.BRIGHT+Fore.WHITE + "    ________     ",
            Style.BRIGHT+Fore.WHITE + "   |/      |    ",
            Style.BRIGHT+Fore.WHITE + "   |      " + (Fore.RED + "O" if intentos > 0 else ""),
            Style.BRIGHT+Fore.WHITE + "   |     " + (Fore.RED + "/|\\" if intentos > 1 else ""),
            Style.BRIGHT+Fore.WHITE + "   |     " + (Fore.RED + "/ \\" if intentos > 2 else ""),
            Style.BRIGHT+Fore.WHITE + "   |            ",
            Style.BRIGHT+Fore.WHITE + "_ _|___         " + Style.RESET_ALL
        ]
    ]

    for parte in ahorcado[intentos]:
        print(parte)

def juego_ahorcado(palabra):
    # Se establece el número máximo de intentos permitidos
    intentos_maximos = 6
    # Inicializamos el contador de intentos a 0
    intentos = 0
    # Creamos una lista para almacenar las letras adivinadas por el jugador
    letras_adivinadas = []

    # Mensaje de inicio del juego en color cyan y estilo brillante
    print(Fore.CYAN + Style.BRIGHT + "¡COMENCEMOS!" + Style.RESET_ALL)

    # El bucle principal del juego, se ejecuta hasta que se alcancen los intentos máximos o se adivine la palabra
    while intentos < intentos_maximos:
        # Mostramos la palabra oculta con las letras adivinadas y guiones bajos para las no adivinadas
        palabra_mostrada = mostrar_palabra(palabra, letras_adivinadas)
        print("\nPalabra:", palabra_mostrada)

        # Comprobamos si el jugador ha adivinado todas las letras de la palabra
        if palabra_mostrada == palabra:
            # Si la palabra mostrada es igual a la palabra original, el jugador ha ganado
            print(Fore.GREEN + "\n¡Has ganado! ¡Felicidades!" + Style.RESET_ALL)
            break

        # Pedimos al jugador que ingrese una letra
        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            # Si la letra ya ha sido adivinada previamente, informamos al jugador y le pedimos otra letra
            print(Fore.YELLOW + "Ya has adivinado esa letra. Intenta otra." + Style.RESET_ALL)
        elif letra in palabra:
            # Si la letra está en la palabra original, informamos al jugador que ha adivinado correctamente
            # y agregamos la letra a la lista de letras adivinadas
            print(Fore.GREEN + "¡Correcto! Has adivinado una letra." + Style.RESET_ALL)
            letras_adivinadas.append(letra)
        else:
            # Si la letra no está en la palabra original, informamos al jugador que ha adivinado incorrectamente,
            # aumentamos el contador de intentos y agregamos la letra a la lista de letras adivinadas
            print(Fore.RED + "Incorrecto. ¡Intenta otra vez!" + Style.RESET_ALL)
            intentos += 1
            letras_adivinadas.append(letra)

        # Mostramos la representación gráfica del ahorcado según los intentos realizados
        mostrar_ahorcado(intentos)

    else:
        # Si el jugador agota todos los intentos sin adivinar la palabra, muestra un mensaje de derrota y revela la palabra
        print(Fore.RED + "\n¡Has perdido! La palabra era:", palabra + Style.RESET_ALL)

        
if __name__ == "__main__":
    while True:  # Bucle para seguir jugando
        # El jugador ingresa las palabras personalizadas o se utilizan palabras por defecto
        palabras_personalizadas = ingresar_palabras()
        # Se selecciona una palabra al azar para el juego
        palabra_seleccionada = seleccionar_palabra(palabras_personalizadas)
        # Se inicia el juego del Ahorcado con la palabra seleccionada
        juego_ahorcado(palabra_seleccionada)
        # Preguntar si el jugador quiere seguir jugando
        seguir_jugando = input("¿Quieres seguir jugando? (s/n): ").lower()
        if seguir_jugando != "s":
            # Si el jugador no quiere seguir jugando, se muestra un mensaje de despedida y se rompe el bucle
            print(Fore.CYAN + "¡Gracias por jugar! Hasta luego." + Style.RESET_ALL)
            break
