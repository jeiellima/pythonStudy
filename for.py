soma = 0

for i in range(1,5):
    nota = float(input(f"Informa a nota do {i}º bimestre: "))
    soma = soma + nota


print("Sua média é:", soma/4)