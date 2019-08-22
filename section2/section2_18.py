file_r = "hightemp.txt"
col_list = []
with open(file_r) as f_r:
    for line in f_r:
        line_split = line.split("\t")
        col_list.append(line_split)
col_list_sorted = sorted(col_list, key=lambda x: (x[2]), reverse=True)
for col in col_list_sorted:
    print(col)
