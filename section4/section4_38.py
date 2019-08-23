import matplotlib.pyplot as plt
import section4_36 as sec36

file_r = "neko.txt.mecab"
file_w = "output38"
length = 10
frequency_list = sec36.word_appearance_frequency(file_r)
word = []
freq = []
with open(file_w, mode="w") as f_w:
    for i in range(10):
        f_w.write(str(frequency_list[i]) + "\n")
        word.append(frequency_list[i][0])
        freq.append(frequency_list[i][1])
    # for line in sentence_list:
    #     for mapping in line:
    #         noun_list.append(mapping["surface"])
    # noun_counter = collections.Counter(noun_list)
    # noun_list_sorted = noun_counter.most_common()
    # for noun in noun_list_sorted:
    #     output = "{0} : {1}".format(noun[0], noun[1])
    #     f_w.write(output + "\n")
    #     noun_list.append(output)

plt.hist(word, freq)
plt.show()
