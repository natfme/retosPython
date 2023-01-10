""" Juego piedra, papel y tijera

¿Cómo se juega a “Piedra, papel, tijera”?: Dos personas esconden la mano detrás de la espalda y a la vez dicen
“¡1, 2, 3, ya!”. En este momento, las dos personas muestran la mano que tenían escondida con la forma de:
• Piedra (Puño cerrado)
• Papel (mano abierta y extendida)
• Tijera (mano cerrada con los dedos índice y corazón extendidos y abiertos –como si se hiciera el
símbolo de la victoria-)

El papel gana a la piedra envolviéndola; la piedra gana a la tijera golpeándola; y la tijera gana al
papel cortándolo """

from random import randint, random

print("Piedra es 1")
print("Papel es 2")
print("Tijera es 3")

#Combate
def combate(num1):
    num2 = randint(1,3) #genera números aleatorios en Python entre el 1 y el 3

    if num2 == 1:
        print("Máquina: Piedra")
    elif num2 == 2:
        print("Máquina: Papel")
    elif num2 == 3:
        print("Máquina: Tijeras")
    else:
        print("La máquina se ha revelado")
        
    if num1 == num2:
        print("Es un empate")
    elif num1 == 1 and num2 == 2:  # usuario elegio Piedra, máquina eligió Papel
        print("USted pierde, vuelva a intentar")
    elif num1 == 2 and num2 == 1: # usuario elegio Papel, máquina eligió Piedra
        print("USted gana")
    elif num1 == 3 and num2 == 1: # usuario elegio Tijaras, máquina eligió Piedra
        print("USted pierde, vuelva a intentar")
    elif num1 == 1 and num2 == 3: # usuario elegio Piedra, máquina eligió Tijeras
        print("USted gana")
    elif num1 == 2 and num2 == 3: # usuario elegio Papel, máquina eligió Tijeras
        print("USted pierde, vuelva a intentar")
    elif num1 == 3 and num2 == 1: # usuario elegio Tijeras, máquina eligió Papel
        print("USted gana")

print("Ingrese un número de 1 a 3")
num1 = int(input())

if num1 == 1:
    print("Usted eligió Piedra")
    combate(num1)
elif num1 == 2:
    print("Usted eligió Papel")
    combate(num1)
elif num1 == 3:
    print("Usted eligió Tijeras")
    combate(num1)
else:
    print("Usted eligió un número diferente a 1, 2 o 3")