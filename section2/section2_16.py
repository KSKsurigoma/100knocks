import linecache
import section2_10 as sec10
import math


file_r = "hightemp.txt"
file_w = "hightemp2_16_"
n = int(input("数字を入力 : "))
len_max = sec10.line_count()
for i in range(1, n + 1):
    with open(file_r) as f_r:
        f_w = open(file_w + str(i) + ".txt", "w")
        for j in range(
            i * math.ceil((len_max / n)) - math.ceil((len_max / n) - 1),
            min(i * math.ceil((len_max / n) + 1), len_max + 1),
        ):
            line = linecache.getline(file_r, j)
            f_w.write(line)
            print(line, end="")
        f_w.close()
