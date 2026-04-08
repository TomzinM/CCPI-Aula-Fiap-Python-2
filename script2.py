import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('charliekirk.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0)


# Exercicio 2

def par_ou_impar(num):
    resultado = num % 2
    if resultado == 0:
        print("Par")
    else: print("Impar")

par_ou_impar(5)

# Exercicio 3

def num_compare(num1, num2):
    if num1 == num2:
        print("São iguais.")
    else: print(max(num1, num2))

num_compare(input("Numero 1: "),input("Numero 2: "))

# Exercicio 4

def nota_aprovar(nota):
    if nota < 5:
        print("Reprovado.")
    elif 5 <= nota < 7:
        print("Em recuperação.")
    else: print("Aprovado")

nota_aprovar(4)

# Exercicio 5

def multiplos(num1, num2):
    resultante = num2 % num1

    if resultante == 0:
        print("São multiplos.")

    else: print("Não São Multiplos.")

multiplos(2, 4)

# Exercicio 6

def calculo(num1, num2, operador):
    if operador == "*":
        print(num1 * num2)
    elif operador == "+":
        print(num1 + num2)
    elif operador == "-":
        print(num1 - num2)
    elif operador == "/":
        print(num1 / num2)
    else: print("Invalido.")

calculo(1, 4, "+")

# Exercicio 7

def determinar_voto(anoNasc, anoAtual):

    idade = anoAtual - anoNasc

    if idade < 16:
        print("Voto restrito.")
    elif 16 >= idade < 18:
        print("Voto opcional.")
    else: print("Voto obrigatorio.")

determinar_voto(2008, 2026)

# Exercicio 8

def salario_reajuste(salario):

    print(f"Seu salario atual é de {salario} reais.")

    if salario <= 280:
        print("Sera aplicado um reajuste de aumento de 20%.")
        salario *= 1.2
        print(salario)
    elif 280 > salario < 700:
        print("Sera aplicado um reajuste de aumento de 15%.")
        salario *= 1.15
        print(salario)
    elif 700 > salario < 1500:
        print("Sera aplicado um reajuste de aumento de 10%.")
        salario *= 1.10
        print(salario)
    else:
        print("Sera aplicado um reajuste de aumento de 5%.")
        salario *= 1.05
        print(salario)

salario_reajuste(400)

# Exercicio 9

def caminhao_calculo(peso,origem,codigo):

    caminhao = True

    while caminhao is True:
        if 1 >= origem <= 5:
            pass
        else:
            print("Erro, origem fora dos parametros.")
            break

        if 10 >= codigo <= 40:
            pass
        else:
            print("Erro, codigo fora dos parametros.")
            break

        peso *= 1000

        if origem == 1:
            imposto = 1.35
        elif origem == 2:
            imposto = 1.25
        elif origem == 3:
            imposto = 1.15
        elif origem == 4:
            imposto = 1.05
        else: imposto = 1.00

        if 10 >= codigo <= 20:
            preco_produto = 100
        elif 21 >= codigo <= 30:
            preco_produto = 250
        elif 31 >= codigo <= 40:
            preco_produto = 340

        preco_bruto = preco_produto * peso
        preco_taxado = preco_bruto * imposto

        print(f"O preço bruto foi de {preco_bruto}, e após imposto é de {preco_taxado}.")

        caminhao = False

# Exercicio 10

def triangulo(cat_a,cat_b,cat_c):

    if cat_a >= cat_b + cat_c:
        print("Não forma triangulo.")
    elif cat_a == cat_b == cat_c:
        print("Triangulo Equilatero.")
    elif cat_a == cat_b or cat_a == cat_c or cat_b == cat_c:
        print("Triangulo Isosceles")
    elif cat_a ** 2 < cat_b ** 2 + cat_c ** 2:
        print("Triangulo Acutangulo.")
    elif cat_a ** 2 == cat_b ** 2 + cat_c ** 2:
        print("Triangulo Retangulo.")
    elif cat_a ** 2 > cat_b ** 2 + cat_c ** 2:
        print("Triangulo Obsutangulo.")

triangulo(4, 3, 2)