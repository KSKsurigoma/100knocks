# -*- coding: utf-8 -*-
def sentence_generate (x, y, z):
    s = x + "時の" + y + "は" + z
    return s

x = 12
y = "気温"
z = 22.4
s = sentence_generate(str(x), str(y), str(z))
print(s)
