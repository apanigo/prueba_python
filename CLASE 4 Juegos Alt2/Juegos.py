import hangman
import reverse
import tictactoe

ok = True
while ok:
    print("""SELECCIONE EL JUEGO QUE DESEA JUGAR: 
    1. Hangman 
    2. Reverse 
    3. Tic Tac Toe
    4. Salir del juego""")
    eleccion = int(input('__'))
    if eleccion == 1:
        hangman.start()
    elif eleccion == 2:
        reverse.start()
    elif eleccion == 3:
        tictactoe.start()
    else:
        ok = False