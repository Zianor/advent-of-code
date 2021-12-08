import itertools

from helper import get_data

data = open(get_data(8)).read().split('\n')

"""
--- Day 8: Seven Segment Search ---

You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate
another exit to this cave at a much greater depth, so you have no choice but to press on.

As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment displays
in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble w
ithout them, so you'd better figure out what's wrong.

Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
So, to render a 1, only segments c and f would be turned on; the rest would be off. To render a 7, only segments a, c,
and f would be turned on.

The problem is that the signals which control the segments have been mixed up on each display. The submarine is still
trying to display numbers by producing output on signal wires a through g, but those wires are connected to segments
randomly. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits
within a display use the same connections, though.)

So, you might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned on:
the only digit that uses two segments is 1, so it must mean segments c and f are meant to be on. With just that
information, you still can't tell which wire (b/g) goes to which segment (c/f). For that, you'll need to collect more
information.

For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, and
then write down a single four digit output value (your puzzle input). Using the signal patterns, you should be able to
work out which pattern corresponds to which digit.

For example, here is what you might see in a single entry in your notes:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
(The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)

Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. Within an
entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique 
signal patterns correspond to the ten different ways the submarine tries to render a digit using the current 
wire/segment connections. Because 7 is the only digit that uses three segments, dab in the above example means that to 
render a 7, signal lines d, a, and b are on. Because 4 is the only digit that uses four segments, eafb means that to 
render a 4, signal lines e, a, f, and b are on.

Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten 
digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the 
output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.

For now, focus on the easy digits. Consider this larger example:

be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce
Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of
signals correspond to those digits. Counting only digits in the output values (the part after | on each line), in the 
above example, there are 26 instances of digits that use a unique number of segments (highlighted above).

In the output values, how many times do digits 1, 4, 7, or 8 appear?

--- Part Two ---

Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example 
above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
After some careful analysis, the known_digits between signal wires and segments only make sense in the following 
configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
So, the unique signal patterns would correspond to the following digits:

acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
Then, the four digits of the output value can be decoded:

cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3
Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above, the output value of each entry can be 
determined:

fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315
Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get 
if you add up all of the output values?

"""


def how_many_times_1_4_7_8(signals):
    output_values = list(itertools.chain(*[line.split(" | ")[1].split(" ") for line in signals]))
    count = len([value for value in output_values if len(value) in [2, 4, 3, 7]])
    print(f"The digits 1, 4, 7 and 8 appear {count} times")
    return count


def sum_output_values(signals):
    output_values_numerical = []
    for signal in signals:
        patterns, output_values = signal.split(" | ")[0].split(" "), signal.split(" | ")[1].split(" ")
        known_digits = {}
        mapping = {}
        values_sorted = [''.join(sorted(value)) for value in patterns + output_values]
        output_values = [''.join(sorted(value)) for value in output_values]
        while any([mapping.get(output_value) is None for output_value in output_values]):
            for value in values_sorted:
                if mapping.get(value):
                    continue
                if len(value) == 2:
                    known_digits['1'] = value
                elif len(value) == 3:
                    known_digits['7'] = value
                elif len(value) == 4:
                    known_digits['4'] = value
                elif len(value) == 7:
                    known_digits['8'] = value
                elif len(value) == 5:  # 2, 3, 5
                    if known_digits.get('1') and all([char in value for char in known_digits['1']]):
                        known_digits['3'] = value
                    elif known_digits.get('9'):
                        if len([char for char in value if char not in known_digits['9']]) == 0:
                            known_digits['5'] = value
                        elif len([char for char in value if char not in known_digits['9']]) == 1:
                            known_digits['2'] = value
                    elif known_digits.get('6'):
                        if len([char for char in known_digits['6'] if char not in value]) == 1:
                            known_digits['5'] = value
                        elif len([char for char in known_digits['6'] if char not in value]) == 2:
                            known_digits['2'] = value
                    elif known_digits.get('3', value) != value:
                        if known_digits.get('5', value) != value:
                            known_digits['2'] = value
                        elif known_digits.get('2', value) != value:
                            known_digits['5'] = value
                elif len(value) == 6:  # 0, 6, 9
                    if known_digits.get('4') and all([char in value for char in known_digits['4']]):
                        known_digits['9'] = value
                    elif known_digits.get('1') and any([char not in value for char in known_digits['1']]):
                        known_digits['6'] = value
                    elif known_digits.get('9', value) != value and known_digits.get('6', value) != value:
                        known_digits['0'] = value
            mapping = {value: digit for digit, value in known_digits.items()}
        output_value = int(''.join([mapping[value] for value in output_values]))
        output_values_numerical.append(output_value)
    print(f"The sum of all output values is {sum(output_values_numerical)}")
    return sum(output_values_numerical)


example_part1 = ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
                 "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
                 "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
                 "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
                 "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
                 "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
                 "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
                 "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
                 "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
                 "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"]

assert how_many_times_1_4_7_8(example_part1) == 26

how_many_times_1_4_7_8(data)

assert sum_output_values(example_part1) == 61229

sum_output_values(data) == 1010472
