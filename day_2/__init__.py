from typing import List, NamedTuple
import re

class GameSet(NamedTuple):
    red: int = 0
    green: int = 0
    blue: int = 0

    def __ge__(self, other):
        return self.red   >= other.red   and \
               self.green >= other.green and \
               self.blue  >= other.blue

    def __le__(self, other):
        return not self >= other

    def power(self):
        return self.red * self.green * self.blue

class Game:
    index_rgx = re.compile("^Game ([0-9]+):")
    colour_rgx = re.compile("([0-9]+) (blue|green|red)")

    def __init__(self, line: str):
        index_match = Game.index_rgx.match(line)
        self.index = int(index_match[1])

        self.sets: List[GameSet] = []
        for section in line.split(';'):
            mapping = {
                colour: int(count)
                for count, colour in Game.colour_rgx.findall(section)
            }
            self.sets.append(GameSet(**mapping))

    def possible(self, bag: GameSet):
        return all(bag >= game_set for game_set in self.sets)

    def minimum(self):
        r, g, b = 0, 0, 0
        for game_set in self.sets:
            if game_set.red > r:
                r = game_set.red
            if game_set.green > g:
                g = game_set.green
            if game_set.blue > b:
                b = game_set.blue
        return GameSet(r, g, b)
