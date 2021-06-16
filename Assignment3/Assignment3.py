# -*- coding: utf-8 -*-
"""Assignment3.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jqNbZweCMaVk4SABK6RQwJemTvGHt2kb
"""

from scipy.stats import expon

len = 100000
count = 0

for i in range(len):
    Y = expon.rvs()
    Y += 0.15
    while 1: 
        X = expon.rvs()
        if X > 0.15:
            break
    if X < Y:
        count += 1

print("Simulated value of probability = ", count / len)
print(" Which is very very close to ")
print("Theoritical value of probability = 0.5")

