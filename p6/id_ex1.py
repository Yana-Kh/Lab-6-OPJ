#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    for i in s:
        if i == ",":
            print("Появилась запятая")
            exit(1)
        else:
            print(i)
    print("Запятых нет")
