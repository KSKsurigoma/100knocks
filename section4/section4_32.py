import section4_30 as sec30

file_r = "neko.txt.mecab"
file_w = "output32"
sentence_list = sec30.sentence_mapping_list(file_r)
with open(file_w, mode="w") as f_w:
    for line in sentence_list:
        for mapping in line:
            if mapping['pos'] == '動詞':
                f_w.write(str(mapping['base'])+"\n")
