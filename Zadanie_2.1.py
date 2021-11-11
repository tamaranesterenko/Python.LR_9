#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    numbers = {1: 'one', 2: 'two', 3: 'tree'}
    numbers_rev = {}
    n = numbers.items()
    for k, v in numbers.items():
        numbers_rev[v] = k
    print(numbers_rev)
