import os

def main(option):
    lines = get_input("input.txt")
    parts = []
    for i, line in enumerate(lines):
        newpart = ""
        is_part = False
        for j, char in enumerate(line):
            if char in "0123456789":
                newpart += char
                is_part = (is_part or get_is_part(i, j, lines))
            elif newpart != "":
                if is_part:
                    parts.append(int(newpart))
                newpart = ""
                is_part = False
        if is_part:
            parts.append(int(newpart))
    return sum(parts)


def get_is_part(x_pos, y_pos, lines):
    for i in range(max(x_pos-1, 0), min(x_pos+2, len(lines))):
        for j in range(max(y_pos-1, 0), min(y_pos+2, len(lines[0]))):
            if lines[i][j] not in ".0123456789":
                return True
    return False

def get_input(file_name):
    # find filepath of txt file from this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    # open file in readmode
    with open(file_path, "r") as file:
        return [x.strip() for x in file]
    
print(str(main(1)))