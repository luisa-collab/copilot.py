# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes que o usuário informou.

# Solicita uma string e um número inteiro como entrada
texto = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

# Retorna a string repetida o número de vezes informado
resultado = texto * numero
print("Resultado:"," ".join( resultado))
