#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите строку: ")
    n, m = 0, 0
    print("Правильно ли расставлены круглые скобки?")
    for i, item in enumerate(s):
        if item == "(":
            n = n + 1
            if m > n:
                print("Скобка ')' стоит раньше чем '('")
        if item == ")":
            m = m + 1
            if n < m:
                print("нет")
                print(f"Обнаружена лишняя правая скобка в позиции: {i}")
                if n == 0:
                    print("Скобка ')' стоит раньше чем '('")
                break
    if n > m:
        print(f"нет\nОбнаружено {n - m} лишних левых скобок")
    if n == m:
        print("да\nСкобки расставлены правильно")
