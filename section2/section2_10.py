def line_count():
    file_r = 'hightemp.txt'
    count = 0
    with open(file_r) as f_r:
        for _ in f_r:
            count += 1
    return count


if __name__ == "__main__":
    print(line_count())
