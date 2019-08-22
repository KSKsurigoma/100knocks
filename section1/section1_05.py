# -*- coding: utf-8 -*-
def char_ngram(s, n):
    li = []
    for i in range(len(s)-n+1):
        add = ""
        for j in range(n):
            add += s[i+j]
        li.append(add)
    return li


def word_ngram(s, n):
    s2 = s.split()
    li = []
    for i in range(len(s2)-n+1):
        add = []
        for j in range(n):
            add.append(s2[i+j])
        li.append(add)
    return li


s1 = "I am an NLPer"
print(char_ngram(s1, 2))
print(word_ngram(s1, 2))
