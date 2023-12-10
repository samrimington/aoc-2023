import math
import os

from day_6 import get_winning_races, number_rgx

def main():
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "./day_6_data/input.txt")

    with open(input_path, "r") as f:
        times_line = f.readline()
        distances_line = f.readline()

    times = [int(x) for x in number_rgx.findall(times_line)]
    distances = [int(x) for x in number_rgx.findall(distances_line)]

    winning_races = []
    for race_time, record_distance in zip(times, distances):
        winning_races.append(
            len(get_winning_races(race_time, record_distance))
        )
    total = math.prod(winning_races)

    print(f"Ways to beat the all records product: {total}")

if __name__ == "__main__":
    main()
