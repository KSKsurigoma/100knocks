import collections


file_r = "hightemp.txt"
col1_list = []
with open(file_r) as f_r:
    for line in f_r:
        line_split = line.split("\t")
        col1_list.append(line_split[0])
col1_counter = collections.Counter(col1_list)
print(col1_counter)