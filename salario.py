salario=float (input ("Digite salario do funcionario SENAI:"))

if salario > 8250:
    novosalario =  salario + salario * 0.10
else:
    novosalario= salario + salario * 0.15

print ("O novo salario do funcionario Senai é:",novosalario)
