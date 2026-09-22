import random

print("Привет это калькулятор")

kluch = 1

while kluch != 0:
    list_chisla = []
    list_znaki = []

    print(f"Введите пример \nДопустим: {random.randint(1, 100)} {random.choice(['+','-','/','*','//','**','%'])} {random.randint(1, 100)} {random.choice(['+','-','/','*','//','**','%'])} {random.randint(1, 100)} {random.choice(['+','-','/','*','//','**','%'])} {random.randint(1, 100)} {random.choice(['+','-','/','*','//','**','%'])} {random.randint(1, 100)}")

    user_input = input().split()
    error = False

    try:
        for i in range(0, len(user_input), 2):
            list_chisla.append(float(user_input[i]))

        for a in range(1, len(user_input), 2):
            list_znaki.append(user_input[a])

        summ = list_chisla[0]

    except ValueError:
        print("Ошибка: Вы ввели неверный формат примера!")
        continue

    except IndexError:
        print("Ошибка: Пример введен некорректно!")
        continue

    i = 0
    while i < len(list_znaki):
        if list_znaki[i] in ['**']:
            list_chisla[i] = list_chisla[i] ** list_chisla[i + 1]

            list_chisla.pop(i + 1)
            list_znaki.pop(i)
        else:
            i += 1

    i = 0
    while i < len(list_znaki):
        if list_znaki[i] in ['*', '/', '%', '//']:
            if list_znaki[i] == '*':
                list_chisla[i] = list_chisla[i] * list_chisla[i + 1]

            elif list_znaki[i] == '/':
                if list_chisla[i + 1] != 0:
                    list_chisla[i] = list_chisla[i] / list_chisla[i + 1]
                else:
                    print("Ошибка: Деление на ноль!")
                    error = True
                    break

            elif list_znaki[i] == '%':
                if list_chisla[i + 1] != 0:
                    list_chisla[i] = list_chisla[i] % list_chisla[i + 1]
                else:
                    print("Ошибка: Деление на ноль!")
                    error = True
                    break

            elif list_znaki[i] == '//':
                if list_chisla[i + 1] != 0:
                    list_chisla[i] = list_chisla[i] // list_chisla[i + 1]
                else:
                    print("Ошибка: Деление на ноль!")
                    error = True
                    break

            list_chisla.pop(i + 1)
            list_znaki.pop(i)

        else:
            i += 1

    if error:
        continue

    i = 0

    while i < len(list_znaki):
        if list_znaki[i] == '+':
            list_chisla[i] = list_chisla[i] + list_chisla[i + 1]
            list_chisla.pop(i + 1)
            list_znaki.pop(i)

        elif list_znaki[i] == '-':
            list_chisla[i] = list_chisla[i] - list_chisla[i + 1]
            list_chisla.pop(i + 1)
            list_znaki.pop(i)

        else:
            i += 1

    summ = list_chisla[0]

    print(*user_input, '=', summ)

    print("Хотите продолжить? 1 - да, 0 - нет")

    if input() == '0':
        break

print('Программа завершена!')
