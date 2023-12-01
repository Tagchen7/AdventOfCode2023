import os

DIGITS = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def main(option=1):
    lines = get_input_str("input.txt")
    numbers = []
    i = 0
    j = 6
    for line in lines:
        if option == 2:
            line = add_letter(line)
            if i == j:
                print("changed line 1: ", line)
                print("original line 1: ", lines[i])
            i +=1
        numbers.append(int("".join([get_first_num(line), get_first_num(line[::-1])])))
    print("first 20 values: ", numbers[j])
    return sum(numbers)

def add_letter(line):
    line = line.lower()
    idx_first = -1
    first = ""
    idx_last = -1
    last = ""
    length_last = 0
    
    for key, value in DIGITS.items():
        i = line.find(key)
        if idx_first == -1 or (i != -1 and i < idx_first):
            idx_first = i
            first = value
    if idx_first != -1:
        line = "".join([line[:idx_first], first, line[idx_first:]])

    for key, value in DIGITS.items():
        j = line.rfind(key)
        if j > idx_last:
            idx_last = j
            length_last = len(key)
            last = value
    if idx_last != -1:
        line = "".join([line[:idx_last+length_last], last, line[idx_last+length_last:]])
    return line

def get_first_num(line):
    for char in line:
        if char.isnumeric():
            return char
    return None

def get_input_str(file_name):
    # find filepath of txt file from this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    # open file in readmode
    with open(file_path, "r") as file:
        lines = []
        for line in file:
            lines.append(line)
    file.close()
    return lines

print("part 1: ", main(1), "\npart 2: ", main(2))