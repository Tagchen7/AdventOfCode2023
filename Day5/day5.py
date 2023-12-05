import os

def main2():
    lines = get_input("input.txt")
    [_, seeds] = lines[0].split(":")
    temp = [int(seed) for seed in seeds.split()]
    seeds = [(temp[i], temp[i+1]) for i in range(0, len(temp), 2)]
    # for test:
    # seeds = [(new, 1) for new in temp]
    lines = lines[1:]
    lines.append("")
    nextmap = []
    for line in lines:
        info = line.split()
        if not info:
            seeds = convert_seeds(seeds, nextmap)
            nextmap = []
            continue
        if info[0].isnumeric():
            nextmap.append([int(item) for item in info])
    return min(seeds)

def convert_seeds(seeds, nextmap):
    change = True
    old = seeds
    new = []
    while change:
        change = False
        for info in nextmap:
            for seed in old.copy():
                # info area can be in the middle of seed area! and seed area can be in the middle of info area!
                found = False
                if seed[0] >= info[1] and seed[0] < info[1] + info[2]:
                    start = seed[0]
                    found = True
                if info[1] >= seed[0] and info[1] < seed[0]+seed[1]:
                    start = info[1]
                    found = True
                if found:
                    length_before = start - seed[0]
                    length_found = min(seed[1] - length_before, info[2] - (start - info[1]))
                    length_after = seed[1] - length_found - length_before
                    old.remove(seed)
                    if length_before:
                        old.append((seed[0], length_before))
                        change = True
                    if length_after:
                        old.append((start + length_found, length_after))
                        change = True
                    new.append((start + info[0] - info[1], length_found))
    new.extend(old)
    return new

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

print("part 1:", main1())
print("part 2:", main2())