""" def par_impar(num):
    par = num%2 == 0
    if par:
        template = f"El número {num} es par"
        print(template)
    elif not par:
        template = f"El número {num} es impar"
        print(template)
    else:
        print("Acabas de descubrir una nueva clasificación de los números") """

""" print("Entre un número entero: ")
num = int(input())
par_impar(num) """

print("Entre un número entero: ")
number = int(input())
print(number)

def par_impar(num):
  par = num%2 == 0
  if par:
    print('Es par')
  else:
    print('Es impar')

par_impar(number)