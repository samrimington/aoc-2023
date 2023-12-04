import re

digit_rgx = re.compile("^[^0-9]*([0-9])|([0-9])[^0-9]*$")

word_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

rv_word_to_digit = {k[::-1]: v for k, v in word_to_digit.items()}

word_rgx = re.compile("|".join(word_to_digit))

rv_word_rgx = re.compile("|".join(rv_word_to_digit))

def get_calibration_value(line: str) -> int:
    results = digit_rgx.findall(line)
    if not results:
        return 0
    elif len(results) == 1:
        return int(results[0][0] + results[0][0])
    else:
        return int(results[0][0] + results[-1][-1])

def get_real_calibration_value(line: str) -> int:
    first_result = word_rgx.search(line)
    if first_result:
        digit = word_to_digit[first_result.group()]
        mutable = list(line)
        mutable[first_result.start()] = digit
        line = "".join(mutable)
    del first_result

    rv_line = line[::-1]
    last_result = rv_word_rgx.search(rv_line)
    if last_result:
        digit = rv_word_to_digit[last_result.group()]
        mutable = list(rv_line)
        mutable[last_result.start()] = digit
        rv_line = "".join(mutable)
        line = rv_line[::-1]
    del last_result
    del rv_line

    return get_calibration_value(line)
