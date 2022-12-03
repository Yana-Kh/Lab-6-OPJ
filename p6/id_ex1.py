#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    flag = s.find(',')
    if flag >= 0:
        print("Появилась запятая")
        s = s[:flag]
    else:
        print("Запятых нет")
    print(f"Строка до первой запятой: {s}")
