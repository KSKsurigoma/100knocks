file_r = 'hightemp.txt'
length = int(input("数字を入力 : "))
with open(file_r) as f_r:
    for i, line in enumerate(f_r):
        print(line, end="")
        if i == length-1:
            break
