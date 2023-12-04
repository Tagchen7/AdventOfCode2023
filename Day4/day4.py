import os

def main(option):
    lines = get_input("input.txt")
    info = {}
    amount = {}
    for line in lines:
        [game, temp] = line.split(":")
        game = int(game.split(" ")[-1])
        temp = temp.split("|")
        temp[0] = temp[0].split(" ")
        temp[1] = temp[1].split(" ")
        for t in temp[0]:
            t = t.strip()
        for t in temp[1]:
            t = t.strip()

        cntwin = 0
        for num in temp[1]:
            if num != "" and num in temp[0]:
                if option == 1:
                    cntwin = max(cntwin+1, cntwin*2)
                else:
                    cntwin += 1
        info[game] = cntwin
        amount[game] = 1
    
    for key, value in info.items():
        cnt = value
        while cnt != 0:
            amount[key+cnt] += amount[key]
            cnt -= 1

    if option == 1:
        return sum(info.values())
    return sum(amount.values())

def get_input(file_name):
    # find filepath of txt file from this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    # open file in readmode
    with open(file_path, "r") as file:
        return [x.strip() for x in file]
    
print(main(2))