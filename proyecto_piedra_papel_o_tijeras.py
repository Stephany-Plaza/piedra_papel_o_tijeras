import random
print("Bienvenido al juego de piedra papel o tijera! ")

lista = ("piedra","papel","tijera")
user_wins = 0
computer_wins = 0
round = 0

while round <3:
    user_answer = input("Que deseas elegir? Piedra, Papel o Tijera? ").lower()
    options = ("piedra","papel","tijera")
    computer_answer = random.choice(options)
    if user_answer not in options:
        print("lo siento, elija una opcion valida")
    elif user_answer == "papel" and computer_answer == "piedra":
        print("has ganado esta vez")
        user_wins += 1
        round += 1
    elif user_answer == "tijera" and computer_answer == "papel":
        print("punto para el usuario!")
        user_wins += 1
        round += 1
    elif user_answer == "piedra" and computer_answer == "tijera":
        print("punto para el usuario!")
        user_wins +=1
        round += 1
    elif user_answer == computer_answer:
        print("es un empate, nadie gana puntos en esta ronda!")
    else:
        print("punto para la computadora, mas suerte la proxima vez :) ")
        computer_wins +=1
        round += 1
if user_wins > computer_wins:
    print(f"ha ganado el usuario {user_wins} a {computer_wins}")
else:
    print(f"ha  ganado la computadora {computer_wins} a {user_wins}")
