peso = float(input("Digite o peso dos peixes: "))

limite = 50

if peso > limite:
    excesso = peso - limite
    multa = excesso * 4
    print("Excesso:", excesso, "kg")
    print("Multa: R$", multa)
else:
    print("Não houve excesso")