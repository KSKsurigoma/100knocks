# -*- coding: utf-8 -*-
s1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s2 = s1.split()
print(s2)
list1 = []
for s in s2:
    l = len(s)
    if s.endswith(',') or s.endswith('.'):
        l -= 1
    list1.append(l)
print(list1)
