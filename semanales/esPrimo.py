"""
 * Reto #3
 * ¿ES UN NÚMERO PRIMO?
 * Fecha publicación enunciado: 17/01/22
 * Fecha publicación resolución: 24/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.

 * Un número primo: tiene 2 divisores y sólo se puede dividir exactamente por sí mismo y por 1.
"""

#n = int(input("Escriba el número que sea comprobar si es primo: "))
listaPrimos = []

for n in range(1,101):
    lista = []
    for i in range(1,n+1):
        if n%(i) == 0:
            lista.append(i)
        i += 1

    #print(lista)
    if len(lista) == 2:
        print(f"El número {n} es primo")
        listaPrimos.append(n)
    else:
        print(f"El número {n} no es primo")

print(listaPrimos)