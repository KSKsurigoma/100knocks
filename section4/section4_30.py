file_r = "neko.txt.mecab"
file_w = "output"
with open(file_r) as f_r:
    with open(file_w, mode="w") as f_w:
        one_sentence_list = []
        for line in f_r:
            if line == "EOS\n":
                f_w.write(str(one_sentence_list)+"\n")
                one_sentence_list.clear()
            else:
                line_split = line.split(",")
                surface = line_split[0].split("\t")[0]
                base = line_split[6]
                pos = line_split[0].split("\t")[1]
                pos1 = line_split[1]
                dic = {"surface": surface, "base": base, "pos": pos, "pos1": pos1}
                one_sentence_list.append(dic)
