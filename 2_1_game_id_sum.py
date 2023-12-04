import os

from day_2 import Game, GameSet

def main():
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "./day_2_data/input.txt")
    output_path = os.path.join(script_dir, "./day_2_data/output.txt")

    bag = GameSet(12, 13, 14)
    total = 0
    with open(input_path, "r") as f:
        with open(output_path, "w") as g:
            for line in f.readlines():
                game = Game(line)
                value = game.index if game.possible(bag) else 0
                g.write(f"{value}\n")
                total += value
    print(f"Game ID sum: {total}")

if __name__ == "__main__":
    main()
