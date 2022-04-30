import time
print("Essa versão do programa conta apenas com:")
print("Torricelli\nCalculadora\nBhaskara")
Formula = input("Qual a formula: ").upper()

if Formula == "TORRICELLI":
    print("Variaveis: velocidade \naceleração \nDeltaS")
    valor = input("Qual a variavel: ").upper()
    if valor == "V" or valor == "VELOCIDADE":

        V0 = float(input("Valor de V0 "))
        A = float(input("valor de A "))
        DeltaS = float(input("valor DeltaS "))
        VariavelV = (V0**2 + 2 * A * DeltaS)**(0.5)
        print("Variavel V em m/s: ", VariavelV)

    elif valor == "A" or valor == "ACELERAÇÃO":

        v0 = float(input("Valor de v0: "))
        v = float(input("Valor de v: "))
        deltaS = float(input("valor deltaS: "))

        VariavelA = (v**2 - v0**2) / (2 * deltaS)
        print("VariavelA: ", VariavelA)

    elif valor == "DELTAS" or valor == "ESPAÇO":
        v0 = float(input("valor de v0: "))
        v = float(input("valor de v: "))
        a = float(input("valor de a: "))

        VariavelDeltaS = (v**2 - v0**2) / (2 * a)
        print("VariavelDeltaS: ", VariavelDeltaS)
#Calculadora Basica
elif Formula == "CALCULADORA":
    print("Operações soma \ndivisao \nmulti")
    a = float( input("Valor 1 "))
    c = float( input("Valor 2 "))

    soma = a + c
    multiplicacao = a * c
    divisao = a / c

    operacao = input("operação desejada: ").upper()

    if operacao == "SOMA" or operacao == "+":
        print(soma)

    elif operacao == "DIVISAO" or operacao == "/":
        print(divisao)

    elif operacao == "MULTI" or operacao == "x":
        print(multiplicacao)

    else:
        print("código de erro: 2")
#Bhaskara
elif Formula == "BHASKARA":
    A = float(input("Valor de A "))
    B = float(input("Valor de B "))
    C = float(input("Valor de C "))

    Delta = B**2 -4 * A * C

    BhaskaraX1 = (-B + Delta**(0.5)) /2 * A
    BhaskaraX2 = (-B - Delta**(0.5)) /2 * A

    print("Delta: ", Delta, "\nbhaskaraX1: ", BhaskaraX1, "\nbhaskaraX2: ", BhaskaraX2)

time.sleep(20)