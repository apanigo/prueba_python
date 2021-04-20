ok = True
while ok:
    print("""SELECCIONE EL JUEGO QUE DESEA JUGAR: 
    1. Hangman 
    2. Reverse 
    3. Tic Tac Toe
    4. Salir del juego""")
    eleccion = int(input('__'))
    if eleccion == 1:
        import hangman
    elif eleccion == 2:
        import reverse
    elif eleccion == 3:
        import tictactoe
    else:
        ok = False

# Se puede hacer esto pero es mala practica