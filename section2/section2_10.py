text_data = open("hightemp.txt", "r")
count = 0
for line in text_data:
    count += 1
text_data.close()
print(count)
