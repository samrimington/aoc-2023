import math
import os

from day_3 import asterisk_rgx, number_rgx

def main():
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "./day_3_data/input.txt")
    engine = []
    with open(input_path, "r") as f:
        engine = f.read().splitlines()

    total = 0
    for idx, line in enumerate(engine):
        for match_1 in asterisk_rgx.finditer(line):
            values = []
            x0, y0 = max(0, idx - 1), max(0, match_1.start() - 1)
            x1, y1 = min(len(engine), idx + 1), min(len(line), match_1.end() + 1)
            for x, i, j in [(x0, y0, y1), (idx, y0, match_1.start()), (idx, match_1.end(), y1), (x1, y0, y1)]:
                while i > 0 and '0' <= engine[x][i] <= '9':
                    i -= 1
                while j < len(engine[x]) - 1 and '0' <= engine[x][j - 1] <= '9':
                    j += 1
                section = engine[x][i:j]
                match_2 = number_rgx.search(section)
                if match_2:
                    values.append(int(match_2.group()))
            assert(len(values) <= 2)
            if len(values) == 2:
                total += math.prod(values)
    print(f"Engine gear ratios sum: {total}")

if __name__ == "__main__":
    main()
