import random

opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]

jugar = True

print("***Bienvenido al juego de Piedra, Papel, Tijera, Lagarto y Spock***") 

while jugar:

    usuario = input("Elige una opcion: ").lower()

    if usuario not in opciones:
        print("Eleccion no valida")
        jugar = False
    else:
        ordenador = random.choice(opciones)
        print(f"El ordenador ha elegido {ordenador}")

        if usuario == ordenador:
            print("Empate")

        elif usuario == "piedra" and (ordenador == "tijera" or ordenador == "lagarto"):
            if ordenador == "tijera":
                print("Ha ganado la piedra ya que aplasta a la tijera")
            else:
                print("Ha ganado la piedra ya que aplasta al lagarto")

        elif usuario == "papel" and (ordenador == "piedra" or ordenador == "spock"):
                if ordenador == "piedra":
                    print("Ha ganado el papel ya que cubre la piedra")
                else:
                    print("Ha ganado el papel ya que desautoriza a spock")

        elif usuario == "tijera" and (ordenador == "papel" or ordenador == "lagarto"):
                if ordenador == "papel":
                    print("Ha ganado la tijera ya que corta al papel")
                else:
                    print("Ha ganado la tijera ya decapita al lagarto")

        elif usuario == "lagarto" and (ordenador == "papel" or ordenador == "spock"):
                if ordenador == "papel":
                    print("Ha ganado el lagarto ya que se come el papel")
                else:
                    print("Ha ganado el el lagarto ya que envenena a spock")

        elif usuario == "spock" and (ordenador == "piedra" or ordenador == "tijera"):
                if ordenador == "piedra":
                    print("Ha ganado el spock ya que vaporiza la piedra")
                else:
                    print("Ha ganado el spock ya que rompe las tijeras")

        else:
            if ordenador == "piedra" and (usuario == "tijera" or usuario == "lagarto"):
                if usuario == "tijera":
                    print("Ha ganado la piedra ya que aplasta a la tijera")
                else:
                    print("Ha ganado la piedra ya que aplasta al lagarto")

            elif ordenador == "papel" and (usuario == "piedra" or usuario == "spock"):
                    if usuario == "piedra":
                        print("Ha ganado el papel ya que cubre la piedra")
                    else:
                        print("Ha ganado el papel ya que desautoriza a spock")

            elif ordenador == "tijera" and (usuario == "papel" or usuario == "lagarto"):
                    if usuario == "papel":
                        print("Ha ganado la tijera ya que corta al papel")
                    else:
                        print("Ha ganado la tijera ya decapita al lagarto")

            elif ordenador == "lagarto" and (usuario == "papel" or usuario == "spock"):
                    if usuario == "papel":
                        print("Ha ganado el lagarto ya que se come el papel")
                    else:
                        print("Ha ganado el el lagarto ya que envenena a spock")

            elif ordenador == "spock" and (usuario == "piedra" or usuario == "tijera"):
                    if usuario == "piedra":
                        print("Ha ganado el spock ya que vaporiza la piedra")
                    else:
                        print("Ha ganado el spock ya que rompe las tijeras")

        seguir_jugando = input("¿Deseas seguir jugando? (s/n): ").lower()
        if seguir_jugando == "s":
            jugar = True
        else:
             jugar = False
            
                

print("Hasta la proxima")