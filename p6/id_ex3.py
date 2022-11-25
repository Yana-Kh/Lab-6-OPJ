#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = input("Введите число: ")
    n = 0
    if s.isdigit():
        for i in s:
            n += int(i)
    else:
        print("Обнаружены не числовые символы", file=sys.stderr)
        exit(1)
    print(f"Сумма цифр числа {s}: {n}")


