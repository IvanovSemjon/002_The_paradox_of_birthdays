import datetime
import random
import pprint

def get_birthdays(number_of_birthdays):
    """ Возвращаем список объектов дат для случайных дней рождения."""
    birthdays = []
    for _ in range(number_of_birthdays):
        #  Год в нашем имитационном моделировании роли не играет.
        #  Лишь бы в объектах дней рождения он был одинаков.
        start_of_year = datetime.date(2001, 1, 1)
        #  Получаем рандомный день года
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays


def get_math(birthdays):
    """ Возвращаем объект даты дня рождения, встречающегося несколько раз в списке дней рождения."""
    if len(birthdays) == len(set(birthdays)):
        #  Все объекты различны, возвращаем None.
        return None

    #  Сравниваем друг с другом дни рождения попарно.
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1:]):
            if birthday_a == birthday_b:
                return birthday_a


print("""
"Парадокс дня рождения", автор Эл Свейгарт al@inventwithpython.com
 
    Парадокс дня рождения показывает нам, что в группе из N человек вероятность
того, что у двоих из них совпадут дни рождения, на удивление велика.
    Эта программа выполняет моделирование методом Монте-Карло (то есть повторяет случайные
симуляции), чтобы исследовать эту концепцию.
 
 (На самом деле это не парадокс, а просто неожиданный результат.)
    """)

#  Создаем кортеж месяцев по порядку.
MONTHS = ('Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня',
          'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря')

#  Запрашиваем, пока пользователь не введет допустимое значение.
while True:
    print('Сколько дней рождения я должен сгенерировать ? (максимум - 100)')
    response = input('>...')
    if response.isdecimal() and 0 < int(response) <= 100:
        num_birthdays = int(response)
        #   Пользователь ввел допустимое значение.
        break

print()

#  Генерируем и отображаем дни рождения.
print('Вот список: Дата и месяц ')
birthdays = get_birthdays(num_birthdays)
for i, birthday in enumerate(birthdays):
    month_name = MONTHS[birthday.month - 1]
    dateText = f'{birthday.day} {month_name};'
    pprint.pprint(dateText)

print()
print()

#  Выясняем встречаются ли два совпадающих дня рождения.
match = get_math(birthdays)

#  Отображаем результаты.
print('В этой симуляции, ', end='')

if match is not None:
    month_name = MONTHS[match.month - 1]
    dateText = f'{match.day} {month_name} '
    print('У многих день рождения приходится на:', dateText)
else:
    print('Совпадающих дней рождений не существует')

print()

#  Производим 100 000 операций имитационного моделирования.
print('Давайте проведем еще 100 000 симуляций')
print('Генерация', num_birthdays, 'случайных дней рождения 100 000 раз.')
input('Нажмите Enter Что бы начать...')

sim_match = 0
for i in range(100_000):
    #  Отображаем о ходе операции каждые 10_000.
    if i % 10_000 == 0:
        print(f'{i} симуляций выполнено...')
        birthdays = get_birthdays(num_birthdays)
    if get_math(birthdays) is not None:
        sim_match = sim_match + 1
print(sim_match)
print('100_000 симуляций выполнено.')

#  результаты имитационного моделирования.
probability = round(sim_match / 100_000 * 100, 2)
print(f'Из 100 000 симуляций с {num_birthdays}, днями рождения людей, ')
print(f'совпадающих дней в этой группе было {sim_match}, а это значит')
print(f'что у {num_birthdays} людей есть шанс в {probability} % что')
print('они отмечают дни рождения в своей группе одновременно')
print('Это наверняка больше чем вы думали :-) ')
