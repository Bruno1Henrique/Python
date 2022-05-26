"""
# 1
for x in range (0,16,3):
    print(x)
#2
for _ in range(3):
    for x in range(0, 100, 3):
        print(x)

num = 0

# 3
while num <= 10:
    print(num)
    num = num + 1
print('Fim')

# 4
num = 0

while num <= 100000:
    print(num)
    num = num + 1000

# 5
num = 0
soma = 0

while num <= 9:
    num = num + 1
    valor = float(input(f"Digite um valor {num} / 10 "))
    soma = soma + valor
print(f"A soma é {soma}")

# 6
media = 0

for x in range(1, 4):
    valor = int(input(f"Digite um numero {x} "))
    media = (valor + media)
conta = media / 3
print(f'{conta}')

# 7
num = 0
soma = 0

while num <= 2:
    num = num + 1
    valor = int(input(f"Digite um numero {num} "))
    if valor < 0:
        print("numero invalido")
    else:
        soma = soma + valor
print(f'{soma}')

# 8
maior = menor = 0

for x in range(1, 5):
    valor = int(input(f"Digite um valor {x}"))
    if x == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print(f"maior {maior}")
print(f"menor {menor}")

# 9

n = int(input("Digite um numero aqui"))
for x in range(1, n, 2):
    print(x)

# 10
soma = 0
for x in range(0,100,2):
    soma = soma + x
print(soma)

#11
num = int(input("Digite um numero aqui"))

if num > 0:
    for x in range(0, num):
        print(x)
else:
    print("Numero invalido")


# 12
num = int(input("Digite um numero"))

if num > 0:
    for x in range(num, 0, -2):
        print(x)
else:
    print("Numero invalido")

# 13
num = int(input("Digite um numero aqui"))

if num > 0 and num % 2 == 0:
    for x in range(0, num):
        print(x)
else:
    print("Valores invalidos")

# 14
num = int(input("Digite um numero"))

if num > 0 and num % 2 == 0:
    for x in range(num, 0, -2):
        print(x)
else:
    print("Numero invalido")

# 15
num = int(input("Digite um numero"))

if num > 0 and num % 2 != 0:
    for x in range(1, num, 2):
        print(x)
else:
    print("Valor invalido")

# 16
num = int(input("Digite um numero"))

if num > 0 and num % 2 != 0:
    for x in range(num,1, -2):
        print(x)
else:
    print("Numero invalido")
"""



