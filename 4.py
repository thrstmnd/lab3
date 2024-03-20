chislo1=1
chislo2=2
life=3
while life >0:
    print(chislo1, "+", chislo2, "=")
    otvet=input()
    if int(otvet) == chislo1+chislo2:
        print("Правильно")
        break
    elif life==1:
        print("Неверный ответ, закончились жизни")
    else:
        print("Неверный ответ, попробуйте еще раз")
    life=life-1