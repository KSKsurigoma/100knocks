# -*- coding: utf-8 -*-
def char_ngram(s, n):
    li = []
    for i in range(len(s)-n+1):
        add = ""
        for j in range(n):
            add += s[i+j]
        li.append(add)
    return li


def gram_search(s, ngram, name):
    for i in range(len(ngram)):
        if s == ngram[i]:
            print("'" + s + "'" + " exists in " + name)
            break
    else:
        print("'" + s + "'" + " doesn't exist in " + name)


s1 = "paraparaparadise"
s2 = "paragraph"
X = set(char_ngram(s1, 2))
Y = set(char_ngram(s2, 2))
intersection = X & Y
difference = X - Y
print(intersection)
print(difference)
gram_search('se', list(X), 'X')
gram_search('se', list(Y), 'Y')
