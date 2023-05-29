nota1= float (input ("Informe a nota1:"))
nota2= float (input ("Informe a nota2:"))
nota3=float (input ("Informe a nota3:"))

media=(nota1 + nota2 + nota3)/3

if media >= 6:
    print("Aprovado")
elif media >=5:
    print ("Conselho de classe")
else:
        print ("Reprovado")

print("A sua média foi:", media)


