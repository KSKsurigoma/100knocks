# -*- coding: utf-8 -*-
import importlib


def gram_search(s, ngram, name):
    if s in ngram:
        print("'{0}'は{1}に含まれる".format(s, name))
    else:
        print("'{0}'は{1}に含まれない".format(s, name))


s1 = "paraparaparadise"
s2 = "paragraph"
ngram_module = importlib.import_module("section1_05")
X = set(ngram_module.char_ngram(s1, 2))
Y = set(ngram_module.char_ngram(s2, 2))
union = X | Y
intersection = X & Y
difference = X - Y
print("XとYの和集合 : {}".format(union))
print("XとYの差集合 : {}".format(difference))
print("XとYの積集合 : {}".format(intersection))
gram_search("se", list(X), "X")
gram_search("se", list(Y), "Y")
