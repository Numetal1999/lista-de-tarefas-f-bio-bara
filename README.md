1- def verificador_de_idade(idade):
    if idade < 0 or idade > 120:
        return "Idade inválida"
    elif idade <= 11:
        return "Criança"
    elif idade <= 17:
        return "Adolescente"
    elif idade <= 59:
        return "Adulto"
    else:
        return "Idoso"


idade = int(input("Digite sua idade: "))

print(verificador_de_idade(idade))


2-- peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"IMC: {imc:.1f} - Abaixo do peso")
elif imc <= 24.9:
    print(f"IMC: {imc:.1f} - Peso normal")
elif imc <= 29.9:
    print(f"IMC: {imc:.1f} - Sobrepeso")
else:
    print(f"IMC: {imc:.1f} - Obesidade")


3- cotacoes = {
    1: ("US$", 5.15),
    2: ("€", 5.55),
    3: ("£", 6.45)
}

print("[1] Real → Dólar")
print("[2] Real → Euro")
print("[3] Real → Libra")

opcao = int(input("Escolha uma opção: "))

if opcao not in cotacoes:
    print("Opção inválida")
else:
    valor = float(input("Digite o valor em reais: "))
    if valor < 0:
        print("Valor inválido")
    else:
        simbolo, cotacao = cotacoes[opcao]
        convertido = valor / cotacao
        print(f"R$ {valor:.2f} = {simbolo} {convertido:.2f}")


4- a = float(input("Digite o lado a: "))
b = float(input("Digite o lado b: "))
c = float(input("Digite o lado c: "))

print(f"Lados: {a}, {b}, {c}")

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Não forma triângulo")
else:
    if a == b == c:
        print("Triângulo válido: Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo válido: Isósceles")
    else:
        print("Triângulo válido: Escaleno")


5- valor = float(input("Digite o valor da compra: R$ "))
vip = input("Cliente VIP? (sim/nao): ").strip().lower()

if valor <= 100:
    desconto = 0
elif valor <= 300:
    desconto = valor * 0.10
elif valor <= 500:
    desconto = valor * 0.15
else:
    desconto = valor * 0.20

desconto_vip = valor * 0.05 if vip == "sim" else 0

final = valor - desconto - desconto_vip

print(f"\nValor original: R$ {valor:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
if desconto_vip > 0:
    print(f"Desconto VIP: R$ {desconto_vip:.2f}")
print(f"Valor final: R$ {final:.2f}")

6- 
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

print(f"\nData: {dia:02d}/{mes:02d}/{ano}")

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
print("Ano bissexto:", "Sim" if bissexto else "Não")

if mes < 1 or mes > 12:
    print("Data inválida: mês inválido")
else:
  
    if mes == 2:
        max_dias = 29 if bissexto else 28
    elif mes in [4, 6, 9, 11]:
        max_dias = 30
    else:
        max_dias = 31

    if dia < 1:
        print("Data inválida: dia inválido")
    elif dia > max_dias:
        print(f"Data inválida: mês {mes} tem apenas {max_dias} dias")
    else:
        print("Data válida!")


7- print("=== CAIXA ELETRÔNICO ===")

valor = int(input("Digite o valor do saque (múltiplo de 10): R$ "))

print(f"\n=== Saque: R$ {valor} ===")

if valor <= 0:
    print("Valor inválido: deve ser positivo")
elif valor % 10 != 0:
    print("Valor inválido: deve ser múltiplo de 10")
else:
    n200 = valor // 200
    valor %= 200

    n100 = valor // 100
    valor %= 100

    n50 = valor // 50
    valor %= 50

    n20 = valor // 20
    valor %= 20

    n10 = valor // 10

    total = n200 + n100 + n50 + n20 + n10

    print(f"R$ 200: {n200} cédula(s)")
    print(f"R$ 100: {n100} cédula(s)")
    print(f"R$ 50:  {n50} cédula(s)")
    print(f"R$ 20:  {n20} cédula(s)")
    print(f"R$ 10:  {n10} cédula(s)")
    print(f"Total de cédulas: {total}")



8- print("=== CALCULO DE ESTACIONAMENTO ===")

entrada = int(input("Hora de entrada (0-23): "))
saida = int(input("Hora de saída (0-23): "))
placa = int(input("Último número da placa: "))
dia = input("Dia da semana: ").strip().lower()

print("\n=== Estacionamento ===")
print(f"Entrada: {entrada:02d}h | Saída: {saida:02d}h")

if saida >= entrada:
    horas = saida - entrada
else:
    horas = (24 - entrada) + saida

if horas == 0:
    horas = 1

print(f"Permanência: {horas} horas")

total = 10 + (horas - 1) * 5
print(f"Tarifa base: R$ {total:.2f}")

noturno = False
for h in range(horas):
    hora_atual = (entrada + h) % 24
    if hora_atual >= 22 or hora_atual < 6:
        noturno = True
        break

if noturno:
    adicional = total * 0.5
    total += adicional
    print(f"Adicional noturno (50%): R$ {adicional:.2f}")

if dia == "segunda" and placa % 2 == 0:
    desconto = total * 0.10
    total -= desconto
    print(f"Desconto (10%): R$ {desconto:.2f}")

print(f"Total: R$ {total:.2f}")

9- import random

nomes = {
    1: "Pedra",
    2: "Papel",
    3: "Tesoura",
    4: "Lagarto",
    5: "Spock"
}

regras = {
    (1, 3): "quebra",
    (1, 4): "esmaga",
    (2, 1): "cobre",
    (2, 5): "refuta",
    (3, 2): "corta",
    (3, 4): "decapita",
    (4, 2): "come",
    (4, 5): "envenena",
    (5, 1): "vaporiza",
    (5, 3): "derrete"
}

jogador = int(input("Escolha (1-Pedra, 2-Papel, 3-Tesoura, 4-Lagarto, 5-Spock): "))

if jogador < 1 or jogador > 5:
    print("Opção inválida!")
else:
    computador = random.randint(1, 5)

    print("Você:", nomes[jogador])
    print("Computador:", nomes[computador])

    if jogador == computador:
        print("Empate!")
    elif (jogador, computador) in regras:
        acao = regras[(jogador, computador)]
        print(f"{nomes[jogador]} {acao} {nomes[computador]} — Você venceu!")
    else:
        acao = regras[(computador, jogador)]
        print(f"{nomes[computador]} {acao} {nomes[jogador]} — Computador venceu!")
  

10- print("=== CÁLCULO DE IR ===")

salario = float(input("Salário bruto: R$ "))
deps = int(input("Número de dependentes: "))
pensao = float(input("Valor da pensão: R$ "))
idoso_input = input("Tem 65 anos ou mais? (s/n): ")

idoso = idoso_input.lower() == "s"

print("\n=== RESULTADO ===")

if salario > 4190.83:
    inss = salario * 0.14
elif salario > 2793.88:
    inss = salario * 0.12
elif salario > 1518:
    inss = salario * 0.09
else:
    inss = salario * 0.075

print(f"INSS: R$ {inss:.2f}")

base = salario - inss - (deps * 189.59) - pensao

if idoso:
    base -= 1903.98

if base < 0:
    base = 0

print(f"Base IR: R$ {base:.2f}")

if base <= 2259.20:
    ir = 0
elif base <= 2826.65:
    ir = base * 0.075
elif base <= 3751.05:
    ir = base * 0.15
elif base <= 4664.68:
    ir = base * 0.225
else:
    ir = base * 0.275

print(f"IR: R$ {ir:.2f}")

liquido = salario - inss - ir
print(f"Salário líquido: R$ {liquido:.2f}")
