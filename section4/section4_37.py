import matplotlib.pyplot as plt
import section4_36 as sec36
import japanize_matplotlib

file_r = "neko.txt.mecab"
file_w = "output37"
length = 10
frequency_list = sec36.word_appearance_frequency(file_r)
words = []
freqs = []
with open(file_w, mode="w") as f_w:
    for i in range(10):
        f_w.write(str(frequency_list[i]) + "\n")
        words.append(frequency_list[i][0])
        freqs.append(frequency_list[i][1])
plt.bar(words, freqs)
plt.xlabel("単語")
plt.ylabel("出現頻度")
plt.show()
