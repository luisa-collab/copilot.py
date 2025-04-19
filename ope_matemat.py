# Vamos solicitar dois números e depois vamos realizar ama operação simples sobre eles.

# Solicita dois números como entrada
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))   
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Realiza a operação desejada e exibe o resultado
if operacao == "+":
    resultado = numero1 + numero2
elif operacao ==  "-":
    resultado = abs (numero1 - numero2)
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisão por zero não é permitida."

        # Exibe o resultado
print("Resultado:", resultado)
