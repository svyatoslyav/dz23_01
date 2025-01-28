rac = 0 #RightAnswerCounter
ans = ["в","а","б","в","г","в","а","в","в","г"] #Список правильних відповідей
wrongans = [] #Список неправильних відповідей(наданих користувачем)
print("Почнемо тестування\nВводьте букву яку вважаєте має правильну відповідь")

q0 = input("1.Кого вважають творцем мови програмування Python?\n"
           "a)Dennis Ritchie\n"
           "б)James Gosling\n"
           "в)Guido van Rossum\n"
           "г)Bjarne Stroustrup\n"
           "Ваша відповідь: ")
if q0 == ans[0]:
    rac+=1
    print("Вірно!")
else:
    print("Невірно")
    wrongans.append(1)

q1 = input("2.У якому році була створена мова програмування Python?\n"
           "a)1989\n"
           "б)1991\n"
           "в)1995\n"
           "г)2000\n"
           "Ваша відповідь: ")
if q1 == ans[1]:
    rac+=1
    print("Вірно!")
else:
    print("Невірно")
    wrongans.append(2)

q2 = input("Який з операторів використовуєтся для перевірки чи значення є більшим або рівним за інше?\n"
           "а)>=\n"
           "б)=>\n"
           "в)>\n"
           "г)!<\n"
           "Ваша відповідь: ")
if q2 == ans[2]:
    rac+=1
    print("Вірно!")
else:
    print("Невірно")
    wrongans.append(3)

q3 = input("Який тип має значення 3.14?\n"
           "а)str\n"
           "б)int\n"
           "в)float\n"
           "г)bool\n"
           "Ваша відповідь: ")
if q3 == ans[3]:
    rac+=1
    print("Вірно!")
else:
    print("Невірно")
    wrongans.append(4)

q4 = input("Яка функція використовується для отримання вводу від користувача?\n"
           "а)enter()\n"
           "б)read()\n"
           "в)print()\n"
           "г)input()\n"
           "Ваша відповідь: ")
if q4 == ans[4]:
    rac+=1
    print("Вірно!")
else:
    print("Невірно")
    wrongans.append(5)

q5 = input("Який символ використовують щоб додати коментар в середовищі Pyton\n"
           "а)/\n"
           "б)//\n"
           "в)#\n"
           "г)##\n"
           "Ваша відповідь: ")
if q5 == ans[5]:
    rac+=1
    print("Вірно!")
else:
    print("Невірно")
    wrongans.append(6)

q6 = input("Який з рядків НЕ виведе помилки?\n"
           'а)print("Hello World")\n'
           'б)print"Hello World"\n'
           'в)print("Hello World)\n'
           'г)prnt("Hello World")\n'
           "Ваша відповідь: ")
if q6 == ans[6]:
    rac+=1
    print("Вірно!")
else:
    print("Невірно")
    wrongans.append(7)

q7 = input("Який номер цього питання?\n"
           "а)6\n"
           "б)7\n"
           "в)8\n"
           "г)9\n"
           "Ваша відповідь: ")
if q7 == ans[7]:
    rac+=1
    print("Вірно!")
else:
    print("Невірно")
    wrongans.append(8)

q8 = input("Що буде результатом запуску наступної частини коду\n"
           "a=7\n"
           "if a != 7:\n"
           '    print("'"'"'а не рівне 7'"'"'")\n'
           "а)а не рівне 7\n"
           "б)'а не рівне 7'\n"
           'в)нічого\n'
           "г)помилка\n"
           "Ваша відповідь: ")
if q8 == ans[8]:
    rac+=1
    print("Вірно!")
else:
    print("Невірно")
    wrongans.append(9)

q9 = input("як перенести рядок в print?\n"
           "а)/m\n"
           "б)/p\n"
           "в)/t\n"
           "г)/n\n"
           "Ваша відповідь: ")
if q9 == ans[9]:
    rac+=1
    print("Вірно!")
else:
    print("Невірно")
    wrongans.append(10)

print(f"Тест завершено! \nВи набрали {rac} балів.")

if rac == 10:
    print("Ви не допустили жодної помилки!")

elif rac == 9:
    print("Ви допустили лише 1 помилку у питанні номер", *wrongans)

else:
    print("Ви допустили помилки у питаннях номер",*wrongans)