import os

from day_3 import number_rgx, symbol_rgx

def main():
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "./day_3_data/input.txt")
    engine = []
    with open(input_path, "r") as f:
        engine = f.read().splitlines()

    total = 0
    for i, line in enumerate(engine):
        for match in number_rgx.finditer(line):
            x0, y0 = max(0, i - 1), max(0, match.start() - 1)
            x1, y1 = min(len(engine), i + 2), min(len(line), match.end() + 1)
            section = ''.join(a[y0:y1] for a in engine[x0:x1])
            if symbol_rgx.search(section):
                total += int(match.group())
    print(f"Engine schematic part number sum: {total}")

if __name__ == "__main__":
    main()
