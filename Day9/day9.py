import os

def main(option):
    input = get_input("input.txt")
    result = 0
    for line in input:
        numbers = [int(num) for num in line.split()]
        result += extrapolate(numbers, option)
    return result

def extrapolate(numbers, option):
    diff = []
    for i in range(len(numbers[:-1])):
        diff.append(numbers[i+1] - numbers[i])
    if all(d == 0 for d in diff):
        if option == 1:
            return numbers[-1]
        return numbers[0]
    if option == 1:
        return numbers[-1] + extrapolate(diff, option)
    return numbers[0] - extrapolate(diff, option)


def get_input(file_name):
    # find filepath of txt file from this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    # open file in readmode
    with open(file_path, "r") as file:
        return [x.strip() for x in file]
    
print(main(2))