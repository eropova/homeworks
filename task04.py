def song():
    """Программа генерирует текст песенки"""

    list_heroes = ['курочку', 'уточку', 'индюшонка', 'кисоньку',
                   'собачонку', 'коровёнку', 'поросёнка']

    list_talks = ['Курочка по зёрнышку кудах-тах-тах.',
                  'Уточка та-ти-та-та.',
                  'Индюшонок фалды-балды.',
                  'А кисуня мяу-мяу.',
                  'Собачонка гав-гав.',
                  'Коровёнка муки-муки.',
                  'Поросёнок хрюки-хрюки.']

    begining = 'Бабушка, бабушка, купим {}!\n'

    ending = 'Бабушка, бабушка, купим телевизор! \n' \
             'Бабушка, бабушка, купим телевизор! \n' \
             'Телевизор надо, надо, ведь у нас такое стадо!'

    final_ver = []
    for i in range(len(list_heroes)):
        int_ver = ''
        int_ver += begining.format(list_heroes[i]) * 2
        int_ver += "\n".join(list_talks[:i+1])
        final_ver.append(int_ver)
    final_ver.append(ending)
    #print(final_ver)
    return "\n\n".join(final_ver)
print(song())