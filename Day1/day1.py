import os

NUMBERS = {"zero":"0", "ten":"10", "eleven":"11", "twelve":"12", "thirteen":"13", "fourteen":"14", "fifteen":"15", "sixteen":"16", "seventeen":"17", "eighteen":"18", "nineteen":"19", "twenty":"20", "thirty":"30", "fourty":"40", "fifty":"50", "sixty":"60", "seventy":"70", "eighty":"80", "ninety":"90", "hundred":"100"}
DIGITS = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def main(option=1):
    lines = get_input_str("input.txt")
    numbers = []
    for line in lines:
        if option == 2:
            line = add_letter(line)
        numbers.append(int("".join([get_first_num(line), get_first_num(line[::-1])])))
    return sum(numbers)

def add_letter(line):
    line = line.lower()
    idx_first = -1
    first = ""
    idx_last = -1
    last = ""
    
    """
    for key, value in NUMBERS.items():
        i = line.find(key)
        if idx_first == -1 or (i != -1 and i < idx_first):
            idx_first = i
            first = value
        j = line.rfind(key)
        if i > idx_last:
            idx_last = j
            last = value
    """
    for key, value in DIGITS.items():
        i = line.find(key)
        if idx_first == -1 or (i != -1 and i < idx_first):
            idx_first = i
            first = value
        j = line.rfind(key)
        if i > idx_last:
            idx_last = j
            last = value
            
    line = "".join([line[:idx_first], first, line[idx_first:]])
    line = "".join([line[:idx_last], last, line[idx_last:]])
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