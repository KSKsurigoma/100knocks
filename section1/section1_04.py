# -*- coding: utf-8 -*-
s1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. " + \
    "New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s2 = s1.split()
print(s2)
dict1 = {}
# 1, 5, 6, 7, 8, 9, 15, 16, 19
for i, s in enumerate(s2, 1):
    print(s)
    if i in (1, 5, 6, 7, 8, 9, 15, 16, 19):
        dict1[s[0]] = i
    else:
        dict1[s[0]+s[1]] = i
print(dict1)
