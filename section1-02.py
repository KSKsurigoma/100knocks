# -*- coding: utf-8 -*-
def jp(s, n):
    return s[n-1] + s[n] + s[n+1]

s1 = "パトカー"
s2 = "タクシー"
s3 = ""
for i in range(1, 5):
    n = 3*i-2
    s3 += jp(s1, n) + jp(s2, n)
print(s3)