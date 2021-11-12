#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime

if __name__ == '__main__':
    people = []

    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'add':
            surname = input("Фамилия: ")
            name = input("Имя: ")
            zodiac = input("Знак зодиака: ")
            dateString = input("Дата: ")


            human = {
                'surname': surname,
                'name': name,
                'zodiac': zodiac,
                'date': datetime.strptime(dateString, "%Y-%m-%d")
            }

            people.append(human)

            if len(people) > 1:
                people.sort(key=lambda item: item.get('zodiac', ''))

        elif command == 'list':
            date_input = int(input("Введите месяц для вывода данных: "))
            line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} | {:^15} |'.format(
                    "№",
                    "Фамилия",
                    "Имя",
                    "Знак зодиака",
                    "Дата рождения"
                )
            )
            print(line)
            pop = 0
            for idx, human in enumerate(people, 1):
                if human.get('date').month == date_input:
                    pop = pop + 1
                    print(
                        '| {:^4} | {:^30} | {:^20} | {:^15} | {:^15} |'.format(
                            pop,
                            human.get('surname'),
                            human.get('name'),
                            human.get('zodiac'),
                            dateString
                        )
                    )
            if pop == 0:
                print('| {:^96} |'.format('Таких людей нет'))

            print(line)
