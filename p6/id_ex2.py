#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    n = 0
    for i in s:
        if i == s[0]:
            n += 1
        else:
            print("Последовательность прервана")
            print(f"Число вхождений {n}")
            break
    if n == len(s):
        print("Последовательность состоит только из одного символа")
        print(f"Число вхождений {n}")
