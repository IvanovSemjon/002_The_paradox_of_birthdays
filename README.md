# 002_The_paradox_of_birthdays
Парадокс дней рождения, также известный как задача о днях рождения, заключается в удивительно высокой вероятности того, что у двух человек совпадает день рождения даже в относительно небольшой группе людей. В группе из 70 человек вероятность совпадения дней рождения у двух людей составляет 99,9 %. Но даже в группе всего лишь из 23 человек вероятность совпадения дней рождения составляет 50 %. Приведенная программа производит несколько вероятностных экспериментов, чтобы определить процентные соотношения для групп различного размера. Подобные эксперименты с определением возможных исходов с помощью множества случайных испытаний называются экспериментами Монте-Карло.

# Программа в действии
Результат выполнения birthdayparadox.py выглядит следующим образом:
Birthday Paradox, by Al Sweigart al@inventwithpython.com
--сокращено--
How many birthdays shall I generate? (Max 100)
# Описание работы
Here are 23 birthdays:
Oct 9, Sep 1, May 28, Jul 29, Feb 17, Jan 8, Aug 18, Feb 19, Dec 1, Jan 22,
May 16, Sep 25, Oct 6, May 6, May 26, Oct 11, Dec 19, Jun 28, Jul 29, Dec 6,
Nov 26, Aug 18, Mar 18
In this simulation, multiple people have a birthday on Jul 29
Generating 23 random birthdays 100,000 times...
Press Enter to begin...
Let's run another 100,000 simulations.
0 simulations run...
10000 simulations run...
--сокращено--
90000 simulations run...
100000 simulations run.
Out of 100,000 simulations of 23 people, there was a
matching birthday in that group 50955 times. This means
that 23 people have a 50.95 % chance of
having a matching birthday in their group.
That's probably more than you would think!

Для запуска программы не требуется дополнительных пакетов. 
