from typing import List
import re

number_rgx = re.compile("[0-9]+")

def get_winning_races(race_time: int, record_distance: int) -> List[int]:
    hold_times = []
    for speed in range(1, race_time):
        travel_time = race_time - speed
        if travel_time * speed > record_distance:
            hold_times.append(speed)
    return hold_times
