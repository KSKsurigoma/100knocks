# -*- coding: utf-8 -*-
import re


def cipner(s1):
    list1 = list(s1)
    for i, s in enumerate(list1):
        if re.match(r"[a-z]", s):
            list1[i] = chr(219-ord(s))
    s_out = ''.join(list1)
    return s_out


s1 = "abzDeFgHijkLmNOpQrstUVWxyzhWopTc0"
print('暗号化前 : {}'.format(s1))
s2 = cipner(s1)
print('暗号化後 : {}'.format(s2))
s3 = cipner(s2)
print('複合化後 : {}'.format(s3))
