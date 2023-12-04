import os

def main():
    lines = get_input("text.txt")
    info = []
    for line in lines:
        [_, temp] = line.split(":")
        temp = temp.split("|")
        temp[0] = temp[0].split(" ")
        temp[1] = temp[1].split(" ")
        cntwin = 0
        for num in temp[1]:
            if num in temp[0]:
                cntwin += 1
        info.append(min(cntwin, 1)*2**cntwin)
    return sum(info)

def get_input(file_name):
    # find filepath of txt file from this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    # open file in readmode
    with open(file_path, "r") as file:
        return [x.strip() for x in file]
    
print(main())