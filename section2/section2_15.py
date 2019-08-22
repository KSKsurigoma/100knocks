import linecache
import section2_10 as sec10


file_r = 'hightemp.txt'
length = int(input("数字を入力 : "))
len_max = sec10.line_count()
with open(file_r) as f_r:
    for i in range(len_max - length + 1, len_max+1):
        line = linecache.getline(file_r, i)
        print(line, end="")
