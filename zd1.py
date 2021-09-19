#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    u = set( "а, o, u, e, i, y" )
    n = int( input('Количество элементов множества? ') )
    m = set()
    for i in range(n):
        m.add(input("введите элемент - "))
    c = u.intersection(m)
    print(m)
    print("Количество гласных ", len(c))