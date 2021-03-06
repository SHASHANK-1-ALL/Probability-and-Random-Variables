# -*- coding: utf-8 -*-
"""Assignment5.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MzQdmEl7CSoygU2R49KyCLZ6nzxMXmX7
"""

import random as rd

len = 100000
count_x1 = count_x2 = 0 
count_x3 = count_x4 = count_x5 = 0
count_x6 = count_x7 = count_x8 = count_x9 =0

#2 washers represented by 1 and 2
#3 nuts represented by 3, 4 and 5
#4 bolts represented by 6, 7, 8 and 9

for i in range(len):
          a = rd.randint(1,9)
          if (a == 1 or a == 2):
            count_x1 += 1
          b = rd.randint(2,9)
          if  b == 2 :
            count_x2 += 1
          c = rd.randint(3,9)
          if (c == 3 or c == 4 or c == 5 ):
            count_x3 += 1
          d = rd.randint(4,9)
          if (d == 4 or d == 5 ):
            count_x4 += 1
          e = rd.randint(5,9)
          if ( e == 5 ):
            count_x5 += 1
          f = rd.randint(6,9)
          if (f == 6 or f == 7 or f == 8 or f == 9):
            count_x6 += 1
          g = rd.randint(7,9)
          if ( g == 7 or g == 8 or g == 9):
            count_x7 += 1
          h = rd.randint(8,9)
          if ( h == 8 or h == 9):
            count_x8 += 1
          i = rd.randint(9,9)
          if (i == 9):
            count_x9 += 1  

num = (count_x1 * count_x2 * count_x3 * count_x4 * count_x5 * count_x6 * count_x7 * count_x8 * count_x9)
denom = pow(len,9)
prob = num / denom
print("Simulated value = ",prob)
print("Which is very very close to")
print("Theoritical value = ", 0.0007936508)