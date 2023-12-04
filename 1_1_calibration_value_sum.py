import os

from day_1 import get_calibration_value

def main():
    script_dir = os.path.dirname(__file__)
    input_path = os.path.join(script_dir, "./day_1_data/input.txt")
    output_path = os.path.join(script_dir, "./day_1_data/output.txt")

    total = 0
    with open(input_path, "r") as f:
        with open(output_path, "w") as g:
            for line in f.readlines():
                value = get_calibration_value(line)
                g.write(f"{value}\n")
                total += value
    print(f"Calibration value sum: {total}")

if __name__ == "__main__":
    main()
