import collections


file_r = "hightemp.txt"
col1_list = []
with open(file_r) as f_r:
    for line in f_r:
        line_split = line.split("\t")
        col1_list.append(line_split[0])
col1_counter = collections.Counter(col1_list)
col1_list_sorted = col1_counter.most_common()
for col1 in col1_list_sorted:
    print('{0} : {1}'.format(col1[0], col1[1]))
