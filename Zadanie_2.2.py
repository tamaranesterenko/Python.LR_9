#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    numbers = {1: 'one', 2: 'two', 3: 'tree'}
    numbers_rev = dict(map(reversed, numbers.items()))
    print(numbers_rev)
