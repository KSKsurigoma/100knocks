import section4_30 as sec30

file_r = "neko.txt.mecab"
file_w = "output34"
sentence_list = sec30.sentence_mapping_list(file_r)
with open(file_w, mode="w") as f_w:
    for line in sentence_list:
        for i, mapping in enumerate(line):
            if mapping["pos"] == "助詞" and mapping["pos1"] == "連体化":
                noun_sen = line[i - 1 : i + 2]
                output = ""
                for noun in noun_sen:
                    output += str(noun["surface"])
                output += "\n"
                f_w.write(output)
