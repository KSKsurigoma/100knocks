# -*- coding: utf-8 -*-
import importlib


def gram_search(s, ngram, name):
    for i in range(len(ngram)):
        if s == ngram[i]:
            print('\'{0}\'は{1}に含まれる'.format(s, name))
            break
    else:
        print('\'{0}\'は{1}に含まれない'.format(s, name))


s1 = "paraparaparadise"
s2 = "paragraph"
ngram_module = importlib.import_module('section1_05')
X = set(ngram_module.char_ngram(s1, 2))
Y = set(ngram_module.char_ngram(s2, 2))
intersection = X & Y
difference = X - Y
print('XとYの和集合 : {}'.format(intersection))
print('XとYの差集合 : {}'.format(difference))
gram_search('se', list(X), 'X')
gram_search('se', list(Y), 'Y')
