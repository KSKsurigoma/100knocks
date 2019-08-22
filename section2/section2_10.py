file_r = 'hightemp.txt'
count = 0
with open(file_r) as f_r:
    for line in f_r:
        count += 1
print(count)
