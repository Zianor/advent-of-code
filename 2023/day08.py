"""
--- Day 8: Haunted Wasteland ---

You're still riding a camel across Desert Island when you spot a sandstorm quickly approaching. When you turn to warn
the Elf, she disappears before your eyes! To be fair, she had just finished warning you about ghosts a few minutes ago.

One of the camel's pouches is labeled "maps" - sure enough, it's full of documents (your puzzle input) about how to
navigate the desert. At least, you're pretty sure that's what they are; one of the documents contains a list of
left/right instructions, and the rest of the documents seem to describe some kind of network of labeled nodes.

It seems like you're meant to use the left/right instructions to navigate the network. Perhaps if you have the camel
follow the same instructions, you can escape the haunted wasteland!

After examining the maps for a bit, two nodes stick out: AAA and ZZZ. You feel like AAA is where you are now, and you
have to follow the left/right instructions until you reach ZZZ.

This format defines each node of the network individually. For example:

RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. In this
example, start with AAA and go right (R) by choosing the right element of AAA, CCC. Then, L means to choose the left
element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2 steps.

Of course, you might not find ZZZ right away. If you run out of left/right instructions, repeat the whole sequence of
instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on. For example, here is a situation that takes
6 steps to reach ZZZ:

LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)

Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?

--- Part Two ---

The sandstorm is upon you and you aren't any closer to escaping the wasteland. You had the camel follow the
instructions, but you've barely left your starting position. It's going to take significantly more steps to escape!

What if the map isn't for people - what if the map is for ghosts? Are ghosts even bound by the laws of spacetime? Only
one way to find out.

After examining the maps a bit longer, your attention is drawn to a curious fact: the number of nodes with names ending
in A is equal to the number ending in Z! If you were a ghost, you'd probably just start at every node that ends with A
and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z.

For example:

LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each
left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on. Repeat
this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z,
they act like any other node and you continue as normal.) In this example, you would proceed as follows:

Step 0: You are at 11A and 22A.
Step 1: You choose all of the left paths, leading you to 11B and 22B.
Step 2: You choose all of the right paths, leading you to 11Z and 22C.
Step 3: You choose all of the left paths, leading you to 11B and 22Z.
Step 4: You choose all of the right paths, leading you to 11Z and 22B.
Step 5: You choose all of the left paths, leading you to 11B and 22C.
Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
So, in this example, you end up entirely on nodes that end in Z after 6 steps.

Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end
with Z?
"""
from math import gcd

from helper import get_data


def get_parsed_puzzle_input(puzzle_input):
    instructions = puzzle_input.split("\n\n")[0]
    network = {}

    for line in puzzle_input.split("\n\n")[1].split("\n"):
        curr_key = line[:3]
        left = line.split("(")[1].split(", ")[0]
        right = line.split("(")[1].split(", ")[1].split(")")[0]
        network[curr_key] = {"L": left, "R": right}
    return instructions, network


def part1(puzzle_input):
    instructions, network = get_parsed_puzzle_input(puzzle_input)
    found = False
    position = 0
    curr_pos = "AAA"
    while not found:
        curr_pos = network[curr_pos][instructions[position % len(instructions)]]
        position += 1
        if curr_pos == "ZZZ":
            found = True
    return position


def part2(puzzle_input):
    instructions, network = get_parsed_puzzle_input(puzzle_input)
    found = False
    position = 0
    starting_nodes = [node for node in network.keys() if node.endswith("A")]
    current_nodes = starting_nodes.copy()
    known_steps_to_end = {}
    while not found:
        curr_instruction = instructions[position % len(instructions)]
        for i, node in enumerate(current_nodes):
            if known_steps_to_end.get(starting_nodes[i]):
                continue
            new_pos = network[node][curr_instruction]
            current_nodes[i] = new_pos
            if new_pos.endswith("Z"):
                known_steps_to_end[starting_nodes[i]] = position + 1
        position += 1
        if len(known_steps_to_end.keys()) == len(starting_nodes):
            found = True
    # calculate lcm
    lcm = 1
    for pos in [known_steps_to_end[curr_key] for curr_key in known_steps_to_end.keys()]:
        lcm = lcm * pos // gcd(lcm, pos)
    return lcm


test_data = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

test_data_part2 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

if __name__ == "__main__":
    res_part1_test = part1(test_data)
    print(f"The result for part 1 with the test data is {res_part1_test}.")
    assert res_part1_test == 6
    data = open(get_data(8), "r").read()
    res_part1 = part1(data)
    print(f"The result for part 1 is {res_part1}.")
    res_part2_test = part2(test_data_part2)
    print(f"The result for part 2 with the test data is {res_part2_test}.")
    assert res_part2_test == 6
    res_part2 = part2(data)
    print(f"The result for part 2 is {res_part2}.")
    # 18625484023687
