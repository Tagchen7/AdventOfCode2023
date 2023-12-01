def main():
    lines = get_input_str("input.txt")
    numbers = []
    for line in lines:
        numbers.append(int("".join(get_first_num(line), get_first_num(line[::-1]))))
    return sum(numbers)


def get_first_num(line):
    for char in line:
        if char.isnumeric():
            return char
    return None

def get_input_str(filename):
    # open file in readmode
    with open(filename, "r") as file:
        lines = []
        for line in file:
            lines.append(line)
    file.close()
    return lines

print(main())