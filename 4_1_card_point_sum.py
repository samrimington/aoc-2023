import os

from day_4 import Card

def main():
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "./day_4_data/input.txt")
    output_path = os.path.join(script_dir, "./day_4_data/output.txt")

    total = 0
    with open(input_path, "r") as f:
        with open(output_path, "w") as g:
            for line in f.readlines():
                card = Card(line)
                value = card.points()
                g.write(f"{value}\n")
                total += value
    print(f"Card point sum: {total}")

if __name__ == "__main__":
    main()
