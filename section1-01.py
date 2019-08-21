# -*- coding: utf-8 -*-
s1 = 'パタトクカシーー'
s2 = ""
for i in range(1, 8):
        if(i % 2 == 1):
                n = 3*i-2
                s2 += s1[n-1] + s1[n] + s1[n+1]
print(s2)