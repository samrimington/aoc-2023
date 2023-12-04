import os

from day_4 import Card

def main():
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "./day_4_data/input.txt")

    cards = []
    with open(input_path, "r") as f:
        for line in f.readlines():
            wins = Card(line).wins()
            cards.append([wins, 1])

    total = 0
    for i in range(len(cards)):
        j_min = min(len(cards), i + 1)
        j_max = min(len(cards), i + cards[i][0] + 1)
        for j in range(j_min, j_max):
            cards[j][1] += cards[i][1]
        total += cards[i][1]

    print(f"Card total sum: {total}")

if __name__ == "__main__":
    main()
