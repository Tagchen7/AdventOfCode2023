import os
import math

def main(option):
    input = get_input("input.txt")
    steps = list(input[0])
    paths = {}
    for line in input[2:]:
        line = line.replace(" ", "")
        [key, values] = line.split("=")
        values = values.strip("()")
        [left, right] = values.split(",")
        paths[key] = {"L": left, "R": right}

    if option == 1:
        position = "AAA"
        cnt = 0
        while position != "ZZZ":
            position = paths[position][steps[cnt % len(steps)]]
            cnt += 1
        return cnt
    
    # cnt to find first end, cnt to find next end until first end was found again for all start positions
    # [[3, 9, 2, 4], [[1, 2], [6, 7, 8], [10], [33, 8]]]
    [counters, nextsteps] = get_counting_steps(steps, paths)
    print(nextsteps)
    cntsteps = []
    for i in nextsteps:
        cntsteps.append(0)
    print("counters", counters)
    print("nextsteps", nextsteps)
    print("cntsteps", cntsteps)
    # least common multiple, since nextsteps == counters and cntsteps == 0
    return math.lcm(*counters)

def get_next_cnt(counters, nextsteps, cntsteps):
    while len(set(counters)) != 1:
        print(counters)
        for i in range(len(counters)):
            if counters[i] < max(counters):
                counters[i] += nextsteps[i][cntsteps[i]]
                cntsteps[i] = (cntsteps[i] + 1) % len(nextsteps[i])
    return counters[0]


def get_counting_steps(steps, paths):
    positions = get_start(paths)
    firstcounts = []
    nextsteps = []
    for pos in positions:
        cnt = 0
        nextpos = pos
        endsteps = []
        firstend = ""
        firstcnt = 0
        looped = False
        nextstep = 0
        while not looped:
            if is_goal(nextpos):
                if firstend == "":
                    firstend = nextpos
                    firstcnt = cnt
                    nextstep = 0
                else:
                    endsteps.append(nextstep)
                    nextstep = 0
                    if nextpos == firstend:
                        looped = True
            nextpos = paths[nextpos][steps[cnt % len(steps)]]
            cnt += 1
            nextstep += 1
        firstcounts.append(firstcnt)
        nextsteps.append(endsteps)
    return [firstcounts, nextsteps]

def get_start(paths):
    startpos = []
    for path in paths:
        if path[-1] == "A":
            startpos.append(path)
    return startpos

def is_start(pos):
    if pos[-1] != "A":
        return False
    return True

def is_goal(pos):
    if pos[-1] != "Z":
        return False
    return True

def get_input(file_name):
    # find filepath of txt file from this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    # open file in readmode
    with open(file_path, "r") as file:
        return [x.strip() for x in file]
    
print(main(2))