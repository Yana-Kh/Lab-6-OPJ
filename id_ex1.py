#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите строку: ")
    n, m = 0, 0
    index = 0
    print("Правильно ли расставлены круглые скобки?")
    for i in s:
        index += 1
        if i == "(":
            n += 1
        if i == ")":
            m += 1
            if n < m:
                print("нет")
                print(f"Обнаружена лишняя правая скобка: {index}")
                exit(1)
    if n > m:
        print(f"нет\nОбнаружено {n-m} лишних левых скобок")
    if n == m:
        print("да\nСкобки расставлены правильно")
