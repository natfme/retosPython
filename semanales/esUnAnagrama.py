""" Reto #1
¿ES UN ANAGRAMA?
Fecha publicación enunciado: 03/01/22
Fecha publicación resolución: 10/01/22
Dificultad: MEDIA

Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
NO hace falta comprobar que ambas palabras existan.
Dos palabras exactamente iguales no son anagrama. """

print("Escriba la primera palabra")
word1 = input()
word1 = word1.lower()

word2 = input()
word2 = word2.lower()

word3 = word2[::-1]

result = (word1 == word3)

word1 = word1.title()
word2 = word2.title()
print(result)
print(f"Las palabras {word1} y {word2} son anagramas")