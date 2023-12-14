import os

# Time = t = th + tt, d = th*tt goal: d > do7
# Bruteforced this, maybe instead use p-q- formula to get one side, best is t/2*t/2
def main(option):
    if option == 1:
        [times, distances] = get_info1("input.txt")
    else:
        [times, distances] = get_info2("input.txt")
    print("times:", times, "distances:", distances)
    amounts = []
    for i, time in enumerate(times):
        amount = 0
        for j in range(time):
            th = j
            tt = times[i]-th
            if distances[i] < th*tt:
                amount += 1
        amounts.append(amount)
    mul = 1
    print("amounts:", amounts)
    for amount in amounts:
        mul *= amount
    return mul

def get_info2(filename):
    input = get_input(filename)
    [_, times] = input[0].split(":")
    times = times.replace(" ", "")
    [_, distances] = input[1].split(":")
    distances = distances.replace(" ", "")
    return [[int(times)], [int(distances)]]

def get_info1(filename):
    input = get_input(filename)
    [_, times] = input[0].split(":")
    times = times.split()
    mytimes = []
    for time in times:
        time = time.strip()
        if time != "":
            mytimes.append(int(time))
    [_, distances] = input[1].split(":")
    distances = distances.split()
    mydistances = []
    for distance in distances:
        distance = distance.strip()
        if distance != "":
            mydistances.append(int(distance))
    return [mytimes, mydistances]


def get_input(file_name):
    # find filepath of txt file from this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    # open file in readmode
    with open(file_path, "r") as file:
        return [x.strip() for x in file]
    
print("amount multiplied:", main(2))