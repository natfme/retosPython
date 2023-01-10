"""Reto #0
EL FAMOSO "FIZZ BUZZ"
Fecha publicación enunciado: 27/12/21
Fecha publicación resolución: 03/01/22
Dificultad: FÁCIL

Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz" """

for i in range(1, 101):  #Range incluye el 1, incrementa de 1 en uno y va hasta 100, por eso se pone hasta 101, para que me incluya el 100
    divisiblePorTres = i % 3 == 0
    divisiblePorCinco = i % 5 == 0

    if divisiblePorTres and divisiblePorCinco:
        print("FizzBuzz")
    elif divisiblePorTres:
        print("Fizz")
    elif divisiblePorCinco:
        print("Buzz")
    else:
        print(i)


