# -*- coding: utf-8 -*-
import re
def cipner (s1):
    for s in s1:
        if re.match(r"[a-z]", s):
            s1 = s1.replace(s, chr(219-ord(s)))
    return s1

s1 = "abcDeFg0"
print(s1)
s2 = cipner(s1)
print(s2)
s3 = cipner(s2)
print(s3)