idade = int(input("Olá, Digite a sua idade "))

if idade < 18:
    print("Você é menor de idade")
elif idade >= 18 and idade < 65:
    print("Você é adulto")
else :
    print("Você é idoso")