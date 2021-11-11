#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    school = {'1A': 30, '1Б': 25, '2A': 27, '2Б': 28, '3Б': 27, '3A': 25, '4A': 25, '4Б': 28, '5A': 27,
              '5Б': 25, '6A': 28, '6Б': 28, '7A': 25, '7Б': 27, '8A': 28, '8Б': 26, '9A': 27, '9Б': 30,
              '10': 25, '11': 30
              }
    # а) в одном из классов изменилось кол-во учеников
    school['5Б'] = 26
    # б) в школе появился новый класс
    school['7Г'] = 15
    # в) в школе был расформирован класс
    del school['9Б']
    # г) посчитать сумму
    n = school.items()
    sum = 0
    for key, value in school.items():
        sum = sum + value
        print(key, '=', value)
    print(f"Общее количество учеников {sum}")
