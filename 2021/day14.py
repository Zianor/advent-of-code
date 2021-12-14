import collections
import copy

from helper import get_data

data = open(get_data(14)).read().split('\n\n')
polymer_data = data[0]
insertion_rules = data[1].split('\n')

"""
--- Day 14: Extended Polymerization ---

The incredible pressures at this depth are starting to put a strain on your submarine. The submarine has polymerization 
equipment that would produce suitable materials to reinforce the submarine, and the nearby volcanically-active caves 
should even have the necessary input elements in sufficient quantities.

The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a polymer 
template and a list of pair insertion rules (your puzzle input). You just need to work out what polymer would result 
after repeating the pair insertion process a few times.

For example:

NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
The first line is the polymer template - this is the starting point of the process.

The following section defines the pair insertion rules. A rule like AB -> C means that when elements A and B are 
immediately adjacent, element C should be inserted between them. These insertions all happen simultaneously.

So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

The first pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.
Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all 
pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.

After the first step of this process, the polymer becomes NCNBCHB.

Here are the results of a few steps using the above rules:

Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. After step 10, B occurs 
1749 times, C occurs 298 times, H occurs 161 times, and N occurs 865 times; taking the quantity of the most common 
element (B, 1749) and subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588.

Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. 
What do you get if you take the quantity of the most common element and subtract the quantity of the least common 
element?

--- Part Two ---

The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair 
insertion process; a total of 40 steps should do it.

In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H 
(occurring 3849876073 times); subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What
do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
"""


def create_rule_dict(rules):
    rule_dict = {}
    for rule in rules:
        pair, insert = rule.split(' -> ')
        rule_dict[pair] = f"{pair[0]}{insert}"
    return rule_dict


def create_rule_dict_for_faster_solution(rules):
    rule_dict = {}
    for rule in rules:
        pair, insert = rule.split(' -> ')
        rule_dict[pair] = insert
    return rule_dict


def apply_step(polymer, rules):
    new_string = []
    for i in range(len(polymer) - 1):
        curr_rule = rules.get(polymer[i: i + 2], polymer[i])
        new_string.append(curr_rule)
    new_string.append(polymer[-1])
    return ''.join(new_string)


def get_result(polymer, rules, steps):
    rules = create_rule_dict(rules)
    for i in range(steps):
        polymer = apply_step(polymer, rules)
    polymer_quantities = {char: polymer.count(char) for char in polymer}
    result = max(polymer_quantities.values()) - min(polymer_quantities.values())
    print(f"{result}")
    return result


def get_result_faster(polymer, rules, steps):
    rules = create_rule_dict_for_faster_solution(rules)
    pairs = [polymer[i:i + 2] for i in range(len(polymer) - 1)]
    pair_dict = {pair: polymer.count(pair) for pair in pairs}
    polymer_quantities = collections.defaultdict(int)
    for char in polymer:
        polymer_quantities[char] += 1
    for i in range(steps):
        new_pairs = collections.defaultdict(int)
        for pair, count in pair_dict.items():
            if rules.get(pair):
                new_pairs[f"{pair[0]}{rules.get(pair)}"] += count
                new_pairs[f"{rules.get(pair)}{pair[1]}"] += count
                polymer_quantities[rules.get(pair)] += count
            else:
                new_pairs[pair] = count
        pair_dict = copy.deepcopy(new_pairs)
    result = max(polymer_quantities.values()) - min(polymer_quantities.values())
    print(f"{result}")
    return result


get_result(polymer_data, insertion_rules, steps=10)

get_result_faster(polymer_data, insertion_rules, steps=10)

get_result_faster(polymer_data, insertion_rules, steps=40)
