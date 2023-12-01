from helper import get_data

"""
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a
map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by 
December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second 
puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you 
("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the 
sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a 
trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been 
amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are 
having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration
value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit 
and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, 
three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""


def part1(data: list[str]):
    sum_calibration_values = 0
    for line in data:
        numbers = [curr_char for curr_char in line if curr_char.isdigit()]
        if len(numbers) > 0:
            curr_number = f"{numbers[0]}{numbers[-1]}"
            curr_number = int(curr_number)
        else:
            curr_number = 0
        sum_calibration_values += curr_number
    return sum_calibration_values


def part2(data: list[str]):
    number_strings = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    cleaned_lines = []
    for line in data:
        curr_line = []
        curr_buffer = []
        for i in range(len(line)):
            curr_buffer.append(line[i])
            if line[i].isdigit():
                curr_line = curr_line + curr_buffer
                curr_buffer = []
            else:
                curr = "".join(curr_buffer)
                for number_string, number in number_strings.items():
                    if curr.endswith(number_string):
                        curr_line.append(str(number))
                        continue
        curr_line = curr_line + curr_buffer
        cleaned_lines.append("".join(curr_line))
    return part1(cleaned_lines)


if __name__ == "__main__":
    test_data_part1 = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
    res_part1_test = part1(test_data_part1)
    print(f"The result for part 1 with the test data is {res_part1_test}.")
    data = open(get_data(1), "r").read().split("\n")
    res_part1 = part1(data)
    print(f"The result for part 1 is {res_part1}.")

    test_data_part2 = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    res_part2_test = part2(test_data_part2)
    print(f"The result for part 2 with the test data is {res_part2_test}.")
    res_part2 = part2(data)
    print(f"The result for part 1 is {res_part2}.")
