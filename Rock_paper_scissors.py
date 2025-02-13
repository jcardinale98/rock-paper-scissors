import random

movimientos = ["piedra", "papel", "tijera"]


puntos_usuario = 0
puntos_ia = 0


while puntos_usuario < 3 and puntos_ia < 3:

    movimientos_ia = random.choice(movimientos)
    movimiento_usuario = input("Introduce tu movimiento (PIEDRA\PAPEL\TIJERA): ")


    if movimiento_usuario.lower() not in movimientos:
        print("EL MOVIMIENTO NO ESTA PERMITIDO")
        quit()

    print(F"HAS SACADO {movimiento_usuario}")
    print(F"EL ORDENADOR HA SACADO {movimientos_ia}")


    if movimiento_usuario.lower() == "piedra":
        if movimientos_ia == "piedra":
            print("EMPATE")
        elif movimientos_ia == "papel":
            print("HAS PERDIDO")
            puntos_ia += 1
        elif movimientos_ia == "tijera":
            print("HAS GANADO")
            puntos_usuario += 1
    if movimiento_usuario.lower() == "papel":
        if movimientos_ia == "piedra":
            print("HAS GANADO")
            puntos_usuario += 1
        elif movimientos_ia == "papel":
            print("EMPATE")
        elif movimientos_ia == "tijera":
            print("HAS PERDIDO")
            puntos_ia += 1
    if movimiento_usuario.lower() == "tijeras":
        if movimientos_ia == "piedra":
            print("HAS PERDIDO")
            puntos_ia += 1
        elif movimientos_ia == "papel":
            print("HAS GANADO")
            puntos_usuario += 1
        elif movimientos_ia == "tijera":
            print("EMPATE")

    print(f"MARCADOR: {puntos_usuario} - {puntos_ia}")
        
if puntos_usuario > puntos_ia:
    print(f"Felicidades, eres superior a la IA en este juego: {puntos_usuario} - {puntos_ia}")
else:
    print(f"Te falta calle papi! La IA te supera en este juego: {puntos_usuario} - {puntos_ia}")


