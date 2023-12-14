import os


def main(option):
    input = get_input("input.txt")
    info = [line.split() for line in input]
    hands = [[Hand(h, option), int(bet)] for [h, bet] in info]
    hands.sort()
    print([str(h) for [h,_] in hands])
    total = 0
    for i, hand in enumerate(hands):
        total += (i+1)*hand[1]
    return total

class Hand:
    def __init__(self, cards, option=1) -> None:
        self.option = option
        self.cards = list(cards)
        if option == 1:
            self.best = self.cards
        else:
            self.best = []
            joker = []
            for card in self.cards:
                if card != "J":
                    self.best.append(card)
                else:
                    joker.append("J")
            num = 0
            unique = set(self.best)
            bestcard = ""
            for card in unique:
                if num == self.best.count(card):
                    if value(bestcard, self.option) < value(card, self.option):
                        bestcard = card
                if num < self.best.count(card):
                    num = self.best.count(card)
                    bestcard = card
            if num == 0:
                self.best = self.cards
            else:
                for card in joker:
                    self.best.append(bestcard)

    def __str__(self):
        return "".join(self.cards)

    def __eq__(self, other):
        return sorted(self.cards) == sorted(other.cards)
    
    def __gt__(self, other):
        if self.handtype() > other.handtype():
            return True
        if self.handtype() < other.handtype():
            return False
        for i in range(len(self.cards)):
            if value(self.cards[i], self.option) > value(other.cards[i], self.option):
                return True
            if value(self.cards[i], self.option) < value(other.cards[i], self.option):
                return False
        return False

    def handtype(self):
        order = [self.is_five(),
                 self.is_four(),
                 self.is_full_house(),
                 self.is_three(),
                 self.is_two_pair(),
                 self.is_pair(),
                 ]
        for i, item in enumerate(order):
            if item:
                return len(order)-i
        return 0

    def is_five(self):
        num = self.best.count(self.best[0])
        return num == 5
    
    def is_four(self):
        unique = set(self.best)
        num = 0
        for card in unique:
            num = max(self.best.count(card), num)
        return num == 4

    def is_full_house(self):
        unique = set(self.best)
        num = []
        for item in unique:
            num.append(self.best.count(item))
        num.sort()
        return num == [2, 3]

    def is_three(self):
        unique = set(self.best)
        num = 0
        for card in unique:
            num = max(self.best.count(card), num)
        return num == 3

    def is_two_pair(self):
        unique = set(self.best)
        num = []
        for item in unique:
            num.append(self.best.count(item))
        num.sort()
        return num == [1, 2, 2]

    def is_pair(self):
        unique = set(self.best)
        num = 0
        for card in unique:
            num = max(self.best.count(card), num)
        return num == 2

def value(card, option):
    if card == "T":
        return 10
    if card == "J":
        if option == 1:
            return 11
        return 1
    if card == "Q":
        return 12
    if card == "K":
        return 13
    if card == "A":
        return 14
    return(int(card))

def get_input(file_name):
    # find filepath of txt file from this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    # open file in readmode
    with open(file_path, "r") as file:
        return [x.strip() for x in file]
    
print(main(2))