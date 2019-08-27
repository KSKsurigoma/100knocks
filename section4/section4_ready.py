import MeCab

mecab = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
file_r = "neko.txt"
file_w = "neko.txt.mecab"
f_w = open(file_w, "w")
with open(file_r) as f_r:
    contents = f_r.read()
    malist = mecab.parse(contents)
with open(file_w, mode="w"):
    f_w.write(malist)
