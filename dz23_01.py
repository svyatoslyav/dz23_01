#Створи цикл, який запитує у тебе числа (вводь 0 для завершення). Виводь загальну суму введених чисел.
a=0
b=1
while True:
    try:
        b = int(input("Введіть ваше число або введіть 0 для завершення\n"))
        if b == 0:
            break
        else:
            a=a+b
    except ValueError:
        print("Це не цисло")
    print("Ваша сума:", a)

print("Ваше фінальна сума - ", a)
