def sentence_mapping_list(file_r: str):
    with open(file_r) as f_r:
        file_w = "output30"
        with open(file_w, mode="w") as f_w:
            sentence_list = []
            one_sentence_list = []
            for line in f_r:
                if line == "EOS\n":
                    sentence_list.append(list(one_sentence_list))
                    one_sentence_list.clear()
                else:
                    line_split = line.split(",")
                    surface = line_split[0].split("\t")[0]
                    base = line_split[6]
                    pos = line_split[0].split("\t")[1]
                    pos1 = line_split[1]
                    dic = {"surface": surface, "base": base, "pos": pos, "pos1": pos1}
                    one_sentence_list.append(dic)
            f_w.write(str(sentence_list))
    return sentence_list


if __name__ == "__main__":
    file_r = "neko.txt.mecab"
    sentence_mapping_list(file_r)
