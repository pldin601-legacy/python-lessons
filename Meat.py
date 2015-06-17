box = dict(meat=89, apple=42, cherry=38, chees=29, cake=67, water=23, beer=56, wine=36, bread=41, suger=27, lemon=11)


def f(b):
    if not b.items():
        return 'Склад пустой'
    else:
        print('Еда на складе:', list(b.keys()), '\n')
    while True:
        a = 0
        for x in sorted(b.items()):
            if a + x[1] <= 100:
                a += x[1]
                del b[x[0]]
                print('Я съел:', x[0], '\n')
        print('Число калорий:', a, '\n')
        break
    if not b.keys():
        return 'На складе ничего не осталось'
    else:
        print('На складе осталось:', list(b))


while True:
    reply = input('Будешь кушать? "Да/Нет"')
    if reply == 'Да':
        f(box)
        if not box.keys():
            print('Это был твой последний ужин, больше кушать нечего')
            break
    else:
        print('Приходи когда захочешь')
        break