import matplotlib.pyplot as plt
import section4_36 as sec36
import japanize_matplotlib

file_r = "neko.txt.mecab"
file_w = "output38"
length = 100
frequency_list = sec36.word_appearance_frequency(file_r)
words = []
freqs = []
f_lists = []
# with open(file_w, mode="w") as f_w:
#     for mapping in frequency_list:
#         f_w.write(str(mapping) + "\n")
#         words.append(mapping[0])
#         freqs.append(mapping[1])
with open(file_w, mode="w") as f_w:
    for i in range(length):
        f_w.write(str(frequency_list[i]) + "\n")
        words.append(frequency_list[i][0])
        freqs.append(frequency_list[i][1])
        f_lists.append(frequency_list[i])
plt.hist(freqs)
plt.show()
