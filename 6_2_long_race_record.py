import math
import os

from day_6 import get_winning_races, number_rgx

def main():
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "./day_6_data/input.txt")

    with open(input_path, "r") as f:
        times_line = f.readline().replace(' ', '')
        distances_line = f.readline().replace(' ', '')

    race_time = int(number_rgx.search(times_line)[0])
    record_distance = int(number_rgx.search(distances_line)[0])
    total = len(get_winning_races(race_time, record_distance))

    print(f"Ways to beat one long race: {total}")

if __name__ == "__main__":
    main()
