import re

class Card:
    card_rgx = re.compile("((?:[0-9]+ +)*[0-9]+) \| +((?:[0-9]+ +)*[0-9]+)")
    number_rgx = re.compile("[0-9]+")

    def __init__(self, line: str):
        wins, scores = Card.card_rgx.search(line).groups()
        self.winning = [int(n) for n in Card.number_rgx.findall(wins)]
        self.scoring = [int(n) for n in Card.number_rgx.findall(scores)]

    def points(self) -> int:
        total = 0
        for win in self.winning:
            if win in self.scoring:
                if total:
                    total *= 2
                else:
                    total = 1
        return total

    def wins(self) -> int:
        total = 0
        for win in self.winning:
            if win in self.scoring:
                total += 1
        return total
