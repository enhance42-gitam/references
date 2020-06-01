def transform(filename):
    filename_only = filename.split(".")[0]
    parts = filename_only.split("-")
    # [0] is number, rest are words
    # print(parts)
    name = parts[0] + ':' + ' [' + " ".join(parts[1:]) + ']'
    link = '(' + filename + ')'
    print(name, link, '  ', sep="")


def process_the_input():
    line = input()
    count = 1
    while (str(line) != "end"):
        # print(count, ":", str(line))
        transform(str(line))
        count += 1
        line = input()
    else:
        # print("end of input")
        pass


print("### Think Python 2e book")
print("Select the chapter:  ")
process_the_input()
