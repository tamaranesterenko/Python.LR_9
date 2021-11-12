# Вариант № 3

# Использовать словарь, содержащий следующие ключи: фамилия и инициалы; номер
# группы; успеваемость (список из пяти элементов). Написать программу, выполняющую
# следующие действия: ввод с клавиатуры данных в список, состоящий из словарей заданной
# структуры; записи должны быть упорядочены по алфавиту; вывод на дисплей фамилий и
# номеров групп для всех студентов, имеющих хотя бы одну оценку 2; если таких студентов
# нет, вывести соответствующее сообщение.

#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    students = []

    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'add':
            surname_n_p = input("Фамилия и инициалы: ")
            number_group = int(input("Номер группы: "))
            academic_performance = list(map(int, input("Успеваемость: ").split()))

            student = {
                'surname_n_p': surname_n_p,
                'number_group': number_group,
                'academic_performance': academic_performance
            }

            students.append(student)

            if len(students) > 1:
                students.sort(key=lambda item: item.get('surname_n_p', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "№",
                    "Фамилия И.О.",
                    "Номер группы",
                    "Успеваемость"
                )
            )
            print(line)
            pop = 0
            for idx, student in enumerate(students, 1):
                if student.get('academic_performance').count(2) > 0:
                    pop = pop + 1

                    print(
                        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                            pop,
                            student.get('surname_n_p'),
                            student.get('number_group'),
                            ''.join(str(elem) + " " for elem in student.get('academic_performance'))
                        )
                    )
                elif pop == 0 and idx != 1:
                    print("Таких студентов нет")

            print(line)
