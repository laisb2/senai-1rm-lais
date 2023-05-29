def encontrar_maior(a, b, c):
    maior = max(a, b, c)
    return maior

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

maior_valor = encontrar_maior(valor1, valor2, valor3)
print("O maior valor é:", maior_valor)