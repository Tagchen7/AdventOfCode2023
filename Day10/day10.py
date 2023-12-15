import os

def main(option):
    input = get_input("test2.txt")
    board = Board(input)
    cnt = 1
    current = board.get_start().connected
    loop = [board.get_start()]
    while current[0] != current[1]:
        cnt += 1
        nextfields = []
        for field in current:
            for connection in field.connected:
                if connection not in loop:
                    nextfields.append(connection)
        loop.extend(current)
        current = [*nextfields]
    loop.extend(current)
    if option == 1:
        return cnt
    
    # TODO ~ test2 result should be 10
    cnt = 0
    for y in range(len(input)):
        is_in_loop = False
        prev = Field()
        for x in range(len(input[0])):
            if board.fields[(x, y)] not in loop and is_in_loop:
                cnt += 1
            elif prev not in board.fields[(x, y)].connected:
                is_in_loop = not is_in_loop
            prev = board.fields[(x, y)]
    return cnt




class Board():
    def __init__(self, input):
        self.fields = {}
        for y, line in enumerate(input):
            for x, char in enumerate(line):
                self.fields[(x, y)] = (Field(char))
        for key1 in self.fields.keys():
            self.fields[key1].add_connection(self.fields.get((key1[0], key1[1]-1), Field()), "up")
            self.fields[key1].add_connection(self.fields.get((key1[0]-1, key1[1]), Field()), "left")
            self.fields[key1].add_connection(self.fields.get((key1[0]+1, key1[1]), Field()), "right")
            self.fields[key1].add_connection(self.fields.get((key1[0], key1[1]+1), Field()), "down")

    def get_start(self):
        for field in self.fields.values():
            if field.char == "S":
                return field
        return Field()

class Field():
    def __init__(self, char=" ", connected=[]):
        self.char = char
        self.connected = [*connected]

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(char={self.char}, connected={[str(field) for field in self.connected]})'
    
    def __str__(self):
        return f'{self.char}'

    def add_connection(self, other, direction):
        # direction (self -> other) can be up, down, left or right
        if direction in self.possible_directions() and invert(direction) in other.possible_directions():
            if other not in self.connected:
                self.connected.append(other)
                other.add_connection(self, invert(direction))

    def possible_directions(self):
        if self.char == "|":
            return ["up", "down"]
        if self.char == "-":
            return ["left", "right"]
        if self.char == "L":
            return ["up", "right"]
        if self.char == "J":
            return ["up", "left"]
        if self.char == "7":
            return ["left", "down"]
        if self.char == "F":
            return ["right", "down"]
        if self.char == ".":
            return []
        if self.char == "S":
            return ["up", "left", "right", "down"]
        return []

def invert(direction):
    if direction == "up":
        return "down"
    if direction == "down":
        return "up"
    if direction == "left":
        return "right"
    if direction == "right":
        return "left"
    return None

def get_input(file_name):
    # find filepath of txt file from this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    # open file in readmode
    with open(file_path, "r") as file:
        return [x.strip() for x in file]
    
print(main(2))