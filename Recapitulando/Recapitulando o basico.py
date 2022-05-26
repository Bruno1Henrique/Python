"""Secao 04

# 1
num = int(input("Digite um numero aqui: "))

print(num)

# 23
print("Vamos converter metros em jardas")
met = float(input("Digite o valor em metros"))

print(" o valor", met, "metros sao", round(met / 0.91))


# 39
vlr = 780000

conta1 = ((46 * 78000) / 100)
conta2 = ((32 * 780000) / 100)
conta3 = (780000 - (conta1 + conta2))

print("O primeiro ganhador irá ganhar", conta1, "R$, o segundo ganhador", conta2, "R$ já o terceiro irá "
                                                                                  "ganhar", conta3, "RS")
"""

"""
Secao 05


# 27
print("Digite a idade do jogador que mostraremos a categoria")

idade = int(input("Digite a idade"))

if (idade >= 5) and (idade <= 7):
    print("Infantil A")
elif (idade >= 8) and (idade <= 10):
    print("Infantil B")
elif (idade >= 11) and (idade <= 13):
    print("Juvenil A")
elif (idade >= 14) and (idade <= 17):
    print("Juvenil B")
else:
    print("Sênior")

# 39
print("Vamos mostrar seu novo salario")
sal = int(input("Qual seu salario atual?"))

if (sal > 0) and (sal <= 500):
    print("Seu novo salario é", ((sal * 25)/100 + sal), "RS e você trabalha na empresa a menos de 1 ano")
elif (sal > 500) and (sal <= 1000):
    print("Seu novo salario é", (((sal * 20) / 100) + sal + 100), "RS e você trabalha na empresa entre 1 ano e 3 anos")
elif (sal > 1000) and (sal <= 1500):
    print("Seu novo salario é", (((sal * 15) / 100) + sal + 200), "RS e voce trabalha na empresa entre 4 a 6 anos")
elif (sal > 1000) and (sal <= 2000):
    print("Seu novo salario é", (((sal * 10) / 100) + sal + 300), "RS e e voce trabalha na empresa entre 7 a 10 anos")
elif sal > 2000:
    print("Seu novo salario é", (sal + 500))
"""
