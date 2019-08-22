# -*- coding: utf-8 -*-
s1 = 'パタトクカシーー'
s2 = ""
for i in range(1, 8):
    if(i % 2 == 1):
        s2 += s1[i]
print(s2)
print(len(s1))
