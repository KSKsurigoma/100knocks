file_r = 'hightemp.txt'
file_w1 = 'col1.txt'
file_w2 = 'col2.txt'
f_w1 = open(file_w1, "w")
f_w2 = open(file_w2, "w")
count = 0
with open(file_r) as f_r:
    for line in f_r:
        line_split = line.split("\t")
        f_w1.write(line_split[0] + "\n")
        f_w2.write(line_split[1] + "\n")
f_w1.close()
f_w2.close()
