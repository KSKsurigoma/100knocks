# -*- coding: utf-8 -*-
import random
def char_rondom_set (s1):
    l = list(range(1, len(s1)-1))
    random.shuffle(l)
    list1 = list(s1)
    list2 = list1[:]
    for idx, rdm_idx in enumerate(l, 1):
        list2[idx] = list1[rdm_idx]
    s_out = ''.join(list2)
    return s_out

def word_rondom_change (s1):
    s2 = s1.split()
    for i, s in enumerate(s2):
        if len(s) > 4:
            s2[i] = char_rondom_set(s)
    s_out = ' '.join(s2)
    return s_out

s1 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(s1)
s2 = word_rondom_change(s1)
print(s2)