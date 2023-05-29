valor_reais = float(input("Digite o valor em reais (R$): "))

taxa_cambio = 4.98
valor_dolares = valor_reais / taxa_cambio

valor_dolares_formatado = "{:.2f}".format(valor_dolares)

print("O valor em dólares é: $", valor_dolares_formatado)