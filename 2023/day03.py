"""
--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source,
but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone!
The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If
you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers
and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part
number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and
58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine
schematic?

--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the
closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone
labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a
phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit
the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is
adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which
gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio
is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because
it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""
from helper import get_data


def part1(input):
    number_sum = 0
    for i, line in enumerate(input):
        number_indices = []
        for j, character in enumerate(line):
            if character.isdigit():
                number_indices.append(j)
            if len(number_indices) > 0 and (
                not character.isdigit() or j == len(line) - 1
            ):
                adj_chars = []
                line_before = i > 0
                line_after = i < len(input) - 1
                if number_indices[0] != 0:
                    adj_chars.append(line[number_indices[0] - 1])
                if number_indices[-1] < len(line) - 1:
                    adj_chars.append(line[number_indices[-1] + 1])
                start_index = max(0, number_indices[0] - 1)
                end_index = min(len(line), number_indices[-1] + 2)
                if line_before:
                    adj_chars = adj_chars + list(input[i - 1][start_index:end_index])
                if line_after:
                    adj_chars = adj_chars + list(input[i + 1][start_index:end_index])
                if any(character != "." for character in adj_chars):
                    number_chars = line[number_indices[0] : number_indices[-1] + 1]
                    number_sum += int("".join(number_chars))
                number_indices = []
    return number_sum


def check_line_part2(line, j):
    numbers = []
    curr_number = []
    k = j - 1
    while k >= 0 and line[k].isdigit():
        curr_number = [line[k]] + curr_number
        k = k - 1
    if line[j].isdigit():
        curr_number.append(line[j])
    else:
        if curr_number:
            numbers.append(int("".join(curr_number)))
        curr_number = []
    k = j + 1
    while k < len(line) and line[k].isdigit():
        curr_number.append(line[k])
        k = k + 1
    if curr_number:
        numbers.append(int("".join(curr_number)))
    return numbers


def part2(input):
    gear_ratio_sum = 0
    for i, line in enumerate(input):
        for j, character in enumerate(line):
            if character == "*":
                # check if two numbers are adjacent
                numbers = []
                line_before = i > 0
                line_after = i < len(input) - 1
                # directly to the left of the '*'
                curr_number = []
                k = j - 1
                while k >= 0 and line[k].isdigit():
                    curr_number = [line[k]] + curr_number
                    k = k - 1
                if curr_number:
                    numbers.append(int("".join(curr_number)))
                # directly to the right of the '*'
                k = j + 1
                curr_number = []
                while k < len(line) and line[k].isdigit():
                    curr_number.append(line[k])
                    k += 1
                if curr_number:
                    numbers.append(int("".join(curr_number)))
                if line_before:  # in the line before
                    numbers = numbers + check_line_part2(input[i - 1], j)
                if line_after:
                    numbers = numbers + check_line_part2(input[i + 1], j)
                if len(numbers) == 2:
                    gear_ratio_sum = gear_ratio_sum + (numbers[0] * numbers[1])
    return gear_ratio_sum


if __name__ == "__main__":
    test_data = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    res_part1_test = part1(test_data)
    print(f"The result for part 1 with the test data is {res_part1_test}.")
    data = open(get_data(3), "r").read().split("\n")
    res_part1 = part1(data)
    # 546312
    print(f"The result for part 1 is {res_part1}.")
    res_part2_test = part2(test_data)
    print(f"The result for part 2 with the test data is {res_part2_test}.")
    res_part2 = part2(data)
    print(f"The result for part 2 is {res_part2}.")
    # 87449461
