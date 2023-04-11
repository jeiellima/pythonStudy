

nota1 = float(input("Digita a nota do 1ºbimestre: "))
nota2 = float(input("Digita a nota do 2ºbimestre: "))
nota3 = float(input("Digita a nota do 3ºbimestre: "))
nota4 = float(input("Digita a nota do 4ºbimestre: "))

media = (nota1 + nota2 + nota3 + nota4) / 4.0

if media == 7.0:
    print("Você passou arrastado!")
elif media == 8.0 or media == 8.5:
    print("Passou folgadinho!")
elif media == 9.0 or media == 9.5:
    print("Excelente nota!")
elif media == 10:
    print("Parabéns! Você atingiu a nota máxima!! UAU!!!")
else:
    print("Você reprovou!")