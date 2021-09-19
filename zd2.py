#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    m = (input("введите элемент - "))
    k = (input("введите элемент 2- "))
    m = set(m)
    k = set(k)
    c = k.intersection(m)
    print("Общие элементы", c)
