n1=float(input("digite um numero"))
n2=float(input("digite o segundo numero"))
n3=float(input("digite o terceito numero"))

numero = {n1,n2,n3}

cresente = sorted (numero)
print("ordem cresente:",cresente)

decresente = sorted (numero, reverse=True)
print("ordem decresente",decresente)