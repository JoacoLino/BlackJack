import random

def cards():
    cards_value = {
        "a":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "10":10,
        "j":10,
        "q":10,
        "k":10
    }
    key_value =  random.choice(list(cards_value.keys()))
    value = cards_value[key_value]
    return value

def bet(money):
    tiene = True
    cuanto_apostar = int(input(f"Cuanto queres apostar, tene en cuenta que tenes {money} dolares: "))
    if money < cuanto_apostar:
        tiene = False
        while tiene == False:
            cuanto_apostar = int(input(f"El monto ingresado supera la plata que tiene por favor ingresar menos, usted tiene {money} dolares: "))
            if cuanto_apostar <= money:
                tiene = True
        
    return cuanto_apostar

def juego(money, cuanto_aposto):
    rta = "si"
    perdio_crupier = False
    perdio_jugador = False
    cartas_jugador = 0
    cartas_crupier = 0
    posible_blackjack = False
    blackjack = False

    cartas_crupier = cartas_crupier + cards()
    print(f"El crupier muestra su primer carta y sale con un valor de {cartas_crupier}")
    print("El crupier te reparte dos cartas...")
    cartas_jugador = cartas_jugador + cards()
    if cartas_jugador == 1 or cartas_jugador == 10:
        posible_blackjack = True
    print(cartas_jugador)
    print("Saca otra y suma un valor de...")
    cartas_jugador = cartas_jugador + cards()
    print(cartas_jugador)
    if posible_blackjack == True and (cartas_jugador == 21 or cartas_jugador == 11):
        blackjack = True
        print("BLACKJACK")



    if cartas_jugador > 21:
        perdio_jugador = True
    else:
        while perdio_jugador == False and rta == "si" and blackjack == False:
            rta = str(input(f"Queres que el crupier saque otra carta, tenes el valor de {cartas_jugador}, si respondes no u otra cosa el crupier no te dara mas cartas: "))
            if rta == "si":
                cartas_jugador = cartas_jugador + cards()
                print(f"La suma de las cartas da un valor de {cartas_jugador}")
                if cartas_jugador > 21:
                    perdio_jugador = True
            else:
                rta == "no"
                print(f"Tus cartas suman {cartas_jugador}")
    
    cartas_crupier = cartas_crupier + cards()
    print(f"El crupier saco otra carta y la suma dio {cartas_crupier}")

    while cartas_crupier < 17:
        cartas_crupier = cartas_crupier + cards()
        print(f"El crupier sumo otra carta y ahora tiene un valor de {cartas_crupier}")
        if cartas_crupier > 21:
            perdio_crupier = True

    if cartas_crupier == 21:
        blackjack = False
        print("El crupier tambien sumo 21, por lo cual hay empate")
        resto = money
    if blackjack == True:
        resto = money + (cuanto_aposto*4)
    if (cartas_crupier > cartas_jugador and perdio_crupier == False) or (perdio_jugador == True and perdio_crupier == False):
        print(f"Perdiste {cuanto_aposto}")
        resto = money - cuanto_aposto
    elif (cartas_jugador > cartas_crupier and perdio_jugador == False) or (perdio_jugador == False and perdio_crupier == True):
        resto = money + (cuanto_aposto * 2)
        print(f"Ganaste un total de {cuanto_aposto*2}")
    elif perdio_crupier and perdio_jugador:
        print("Ambos superaron los 21")
        resto = money
    return resto


def main():
    money = 500
    quiera_jugar = True
    while quiera_jugar:
        cuanto_aposto = bet(money)
        resto = juego(money, cuanto_aposto)
        money = resto
        print(f"Tenes {money} dolares")

        if money <= 0:
            quiera_jugar = False
            print("Te quedaste sin plata")        
        else:
            seguir = str(input("Queres seguir jugando(cualquier respuesta diferente a no va a ser si): "))
            if seguir == "no":
                quiera_jugar = False
    print(f"Te retiraste con {money} dolares")

main()
