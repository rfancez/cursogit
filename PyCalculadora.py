finalizar = 0

while finalizar != 1:

    menu = int(input('Digite a operação (1)Para Adição, (2)Subtração, (3)Divisão, (4) multiplicação:  '))


    if menu == 1:
        somar1 = float(input('Digite o primeiro numero: '))
        somar2 = float(input('Digite o segundo numero: '))
        total = somar1 + somar2
        print(total)

    elif menu == 2:
        sub1 = float(input('Digite o primeiro numero: '))
        sub2 = float(input('Digite o segundo numero: '))
        total = sub1 - sub2
        print(total)
    elif menu == 3:
        div1 = float(input('Digite o primeiro numero: '))
        div2 = float(input('Digite o segundo numero: '))
        total = div1 / div2
        print(total)
    elif menu == 4:
        mult1 = float(input('Digite o primeiro numero: '))
        mult2 = float(input('Digite o segundo numero: '))
        total = mult1 * mult2
        print(total)
    else:
        print("Valor incorreto")

    finalizar = int(input("Digite 0 para outra operação ou 1 para finalizar:   "))