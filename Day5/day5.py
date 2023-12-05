import os

def main1():
    lines = get_input("input.txt")
    [_, seeds] = lines[0].split(":")
    seeds = [int(seed) for seed in seeds.split()]
    new = []
    lines = lines[1:]
    for line in lines:
        info = line.split()
        if not info:
            for seed in seeds:
                new.append(seed)
            seeds = new
            new = []
            continue
        if info[0].isnumeric():
            conv = [int(item) for item in info]
            for seed in seeds.copy():
                if seed in range(conv[1], conv[1] + conv[2]):
                    new.append(seed + conv[0] - conv[1])
                    seeds.remove(seed)                
    return min(new)

def get_input(file_name):
    # find filepath of txt file from this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    # open file in readmode
    with open(file_path, "r") as file:
        return [x.strip() for x in file]
    
print(main1())