#Lista 1 (adicional) ex 3

numero =(input("Digite um número inteiro:"))
inteiro = int(numero)
if 10 > inteiro >= 0:
	print("O dígito das dezenas é 0")
else:
	print("O dígito das dezenas é", numero[-2])