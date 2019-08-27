file_r = 'hightemp.txt'
file_w = 'hightemp2_11.txt'
f_w = open(file_w, "w")
with open(file_r) as f_r:
    for line in f_r:
        line = line.replace("\t", " ")
        f_w.write(line)
f_w.close()
