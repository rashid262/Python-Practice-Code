def split_and_join(line):
    new_line = line.split(" ")
    print(new_line)
    print(type(new_line))
    return "-".join(new_line)

line = input()
print(split_and_join(line))