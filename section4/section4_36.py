import collections
import section4_30 as sec30

file_r = "neko.txt.mecab"
file_w = "output36"
sentence_list = sec30.sentence_mapping_list(file_r)
noun_list = []
with open(file_w, mode="w") as f_w:
    for line in sentence_list:
        for mapping in line:
            noun_list.append(mapping["surface"])
    noun_counter = collections.Counter(noun_list)
    noun_list_sorted = noun_counter.most_common()
    for noun in noun_list_sorted:
        output = "{0} : {1}".format(noun[0], noun[1])
        f_w.write(output + "\n")
