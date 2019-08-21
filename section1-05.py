# -*- coding: utf-8 -*-
def char_ngram (s, n):
    l = []
    for i in range(len(s)-n+1):
        add = ""
        for j in range(n):
            add += s[i+j]
        l.append(add)
    return l

def word_ngram (s, n):
    s2 = s.split()
    l = []
    for i in range(len(s2)-n+1):
        add = []
        for j in range(n):
            add.append(s2[i+j])
        l.append(add)
    return l

s1 = "I am an NLPer"
print(char_ngram(s1, 2))
print(word_ngram(s1, 2))

