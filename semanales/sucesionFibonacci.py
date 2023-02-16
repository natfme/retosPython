"""
Reto #2
 * LA SUCESIÓN DE FIBONACCI
 * Fecha publicación enunciado: 10/01/22
 * Fecha publicación resolución: 17/01/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
 * La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
 * 0, 1, 1, 2, 3, 5, 8, 13...
 *
"""
print("Sucesión de Fibonacci")

x = int(input("Primer número: "))
y = int(input("Segundo número: "))
n = int(input("¿Cuántos números quiere imprimir: "))
lista = [x, y]

for i in range(0,n-2):
    z = x + y
    lista.append(z)
    x = y
    y = z
    i += 1

print(lista)