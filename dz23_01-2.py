i=0
rac = 0 #RightAnswerCounter
wrongans = [] #Список неправильних відповідей(наданих користувачем)
ans = ["в","а","а","в","г","в","а","в","в","г"] #Список правильних відповідей
qlist = ["Кого вважають творцем мови програмування Python?\n"
           "a)Dennis Ritchie\n"
           "б)James Gosling\n"
           "в)Guido van Rossum\n"
           "г)Bjarne Stroustrup\n"
           "Ваша відповідь: ",

         "У якому році була створена мова програмування Python?\n"
         "a)1989\n"
         "б)1991\n"
         "в)1995\n"
         "г)2000\n"
         "Ваша відповідь: ",

         "Який з операторів використовується для перевірки чи значення є більшим або рівним за інше?\n"
         "а)>=\n"
         "б)=>\n"
         "в)>\n"
         "г)!<\n"
         "Ваша відповідь: ",

         "Який тип має значення 3.14?\n"
         "а)str\n"
         "б)int\n"
         "в)float\n"
         "г)bool\n"
         "Ваша відповідь: ",

         "Яка функція використовується для отримання вводу від користувача?\n"
         "а)enter()\n"
         "б)read()\n"
         "в)print()\n"
         "г)input()\n"
         "Ваша відповідь: ",

         "Який символ використовують щоб додати коментар в середовищі Pyton\n"
         "а)/\n"
         "б)//\n"
         "в)#\n"
         "г)##\n"
         "Ваша відповідь: ",

         "Який з рядків НЕ виведе помилки?\n"
         'а)print("Hello World")\n'
         'б)print"Hello World"\n'
         'в)print("Hello World)\n'
         'г)prnt("Hello World")\n'
         "Ваша відповідь: ",

         "Який номер цього питання?\n"
         "а)6\n"
         "б)7\n"
         "в)8\n"
         "г)9\n"
         "Ваша відповідь: ",

         "Що буде результатом запуску наступної частини коду\n"
         "a=7\n"
         "if a != 7:\n"
         '    print("'"'"'а не рівне 7'"'"'")\n'
         "а)а не рівне 7\n"
         "б)'а не рівне 7'\n"
         'в)нічого\n'
         "г)помилка\n"
         "Ваша відповідь: ",

         "як перенести рядок в print?\n"
         "а)/m\n"
         "б)/p\n"
         "в)/t\n"
         "г)/n\n"
         "Ваша відповідь: "] #список питань
#початок функціональної частини коду
print("Почнемо тестування\nВводьте букву яку вважаєте має правильну відповідь")
while i != len(qlist):
    q = input(qlist[i])
    if q == ans[i]:
        rac += 1
        print("Вірно!")
    else:
        print("Невірно")
        wrongans.append(i+1)
    i+=1
#кінець функціональної частини коду і початок завершальної
print(f"Тест завершено! \nВи набрали {rac} балів.")

if rac == 10:
    print("Ви не допустили жодної помилки!")

elif rac == 9:
    print("Ви допустили лише 1 помилку у питанні номер", *wrongans)

else:
    print("Ви допустили помилки у питаннях номер",*wrongans)