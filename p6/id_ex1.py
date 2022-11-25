#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    if ',' in s:
        print("Появилась запятая")
        s = s[:s.index(',')]
    else:
        print("Запятых нет")
    print(f"Строка до первой запятой: {s}")

