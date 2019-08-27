file_r1 = 'col1.txt'
file_r2 = 'col2.txt'
file_w = 'col_merge.txt'
f_r1 = open(file_r1, "r")
f_r2 = open(file_r2, "r")
f_w = open(file_w, "w")
for line1, line2 in zip(f_r1, f_r2):
    line1 = line1.replace("\n", "\t")
    f_w.write(line1 + line2)
f_r1.close()
f_r2.close()
f_w.close()
