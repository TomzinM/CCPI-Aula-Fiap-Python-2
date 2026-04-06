import collections
from struct import calcsize

# Exercicio 1

resposta = "Y"

while resposta == "Y":
    print("Ola, mundo")
    resposta = input("Escreva Y se quiser continuar.").upper()

# Exercicio 2

for number in range(0, 101, 10):
    print(number)

# Exercicio 3

for n in range(0, 26):
    n *= 5
    print(n)

# Exercicio 4

calc = True
while calc is True:
    num1 = float(input("Primeiro Numero?"))
    num2 = float(input("Segundo Numero?"))
    num3 = float(input("Terceiro Numero?"))
    num4 = float(input("Quarto Numero?"))
    num5 = float(input("Quinto Numero?"))

    soma = num1 + num2 + num3 + num4 + num5
    print(soma)

# Exercicio 5

    print(max(num1, num2, num3, num4, num5))
    calc = False

# Exercicio 6

limite = int(input("Ate qual numero quer ir?"))

for numeros in range(2, limite + 1, 2):
    print(numeros)

# Exercicio 7

numeroValidacao = True

def parseInteger(item):
    resultant = None
    try:
        int(item)
    except:
        pass
    else:
        resultant = int(item)
    return resultant

numero = 0

while numeroValidacao is True:
    numero = input("Qual numero quer fazer a soma de todos anteriores?:")

    if parseInteger(numero) is None:
        print("Não é um numero valido.")
        continue

    else: numero = int(numero)

    if numero < 1:
        print("O numero é negativo.")
        continue

    numeroValidacao = False

soma = 0

for n in range(1, numero + 1):
    soma += n

print(soma)

# Exercicio 8

num = int(input("Numero positivo para achar divisores: "))
nums = 0

for n in range(0, num + 1):
    n += 1
    nums = num % n

    if nums == 0:
        print(n)

numCount = 0

# Exercicio 9

for n in range(2, 2001):
    numCount = 0

    for number in range(1, n + 1):
        if n % number == 0:
           numCount += 1

    if numCount == 2:
        print(n)
    n += 1

