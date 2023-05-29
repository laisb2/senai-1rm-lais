valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

opcao = input("Escolha uma opção (multiplicar/maior): ")

if opcao == "multiplicar":
    resultado = valor1 * valor2
    print("O resultado da multiplicação é:", resultado)
elif opcao == "maior":
    maior = max(valor1, valor2)
    print("O maior valor é:", maior)
else:
    print("Opção inválida.")
