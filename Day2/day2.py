import os

def get_info(line):
    [gamestr, result] = line.split(":")
    single = result.split(";")
    red, green, blue = 0, 0, 0
    for draw in single:
        colorstr = draw.split(",")
        for singlecolor in colorstr:
            if "green" in singlecolor:
                green = max(green, get_num(singlecolor))
            if "red" in singlecolor:
                red = max(red, get_num(singlecolor))
            if "blue" in singlecolor:
                blue = max(blue, get_num(singlecolor))

    colors = {"red":red, "green":green, "blue":blue}
    games = {get_num(gamestr):colors}
    return games
        
def get_num(string):
    numstr = ""
    for char in string:
        if char in "0123456789":
            numstr += char
    return int(numstr)

def get_input(file_name):
    # find filepath of txt file from this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    # open file in readmode
    with open(file_path, "r") as file:
        return [x.strip() for x in file]

def main(option):
    lines = get_input("input.txt")
    games = {}
    for line in lines:
        games.update(get_info(line))
        sum = 0
        for key, colordict in games.items():
            if option == 1:
              if is_valid(12, 13, 14, colordict):
                 sum += key
            else:
                sum += power(colordict)
    return sum

def power(colordict):
    mult = 1
    for color in colordict.values():
        mult *= color
    return mult

def is_valid(red, green, blue, colordict):
    if colordict["red"] > red or colordict["green"] > green or colordict["blue"] > blue:
        return False
    return True

print(str(main(2)))