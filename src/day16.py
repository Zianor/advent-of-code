from helper import get_data

data = open(get_data(16), 'r').read().split('\n\n')

"""
--- Day 16: Ticket Translation ---

As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up
is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should
probably figure out what it says before you get to the train station after the next flight.

Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you figure
out the fields these tickets must have and the valid ranges for values in those fields.

You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for the
same train service (via the airport security cameras) together into a single document you can reference (your puzzle
input).

The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of values
for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields in every ticket is named class
and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).

Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the
order they appear; every ticket has the same format. For example, consider this ticket:

.--------------------------------------------------------.
| ????: 101    ?????: 102   ??????????: 103     ???: 104 |
|                                                        |
| ??: 301  ??: 302             ???????: 303      ??????? |
| ??: 401  ??: 402           ???? ????: 403    ????????? |
'--------------------------------------------------------'
Here, ? represents text in a language you don't understand. This ticket might be represented as 101,102,103,104,301,302,
303,401,402,403; of course, the actual train tickets you're looking at are much more complicated. In any case, you've
extracted just the numbers in such a way that the first number is always the same specific field, the second number is
always a different specific field, and so on - you just don't know what each position actually means!

Start by determining which tickets are completely invalid; these are tickets that contain values which aren't valid for
any field. Ignore your ticket for now.

For example, suppose you have the following notes:

class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets by considering
only whether tickets contain values that are not valid for any field. In this example, the values on the first nearby
ticket are all valid for at least one field. This is not true of the other three nearby tickets: the values 4, 55, and
12 are are not valid for any field. Adding together all of the invalid values produces your ticket scanning error rate:
4 + 55 + 12 = 71.

Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?
"""


def check_rules(number, rules):
    for rule in rules.values():
        if check_rule(number, rule):
            return True
    return False


def check_rule(number, rule):
    if int(rule[0].split("-")[0]) <= number <= int(rule[0].split("-")[1]):
        return True
    if int(rule[1].split("-")[0]) <= number <= int(rule[1].split("-")[1]):
        return True
    return False


rules = data[0].split("\n")
rule_names = [rule.split(": ")[0] for rule in rules]
rules = {rule.split(": ")[0]: rule.split(": ")[1].split(" or ") for rule in rules}

ticket = data[1].replace("your ticket:\n", "").split(",")

nearby = data[2].split("\n")
nearby = [ticket.split(",") for ticket in nearby[1:]]


def get_error_rate(tickets, rules):
    error_rate = 0

    for ticket in tickets:
        for number in ticket:
            if not check_rules(int(number), rules):
                error_rate += int(number)

    return error_rate


print(f"The error rate of the nearby tickets is {get_error_rate(nearby, rules)}")

"""
--- Part Two ---

Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the remaining 
valid tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent 
between all tickets: if seat is the third field, it is the third field on every ticket, including your ticket.

For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
Based on the nearby tickets in the above example, the first position must be row, the second position must be class, 
and the third position must be seat; you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

Once you work out which field is which, look for the six fields on your ticket that start with the word departure. What 
do you get if you multiply those six values together?
"""


def ticket_valid(ticket, rules):
    for number in ticket:
        if not check_rules(int(number), rules):
            return False
    return True


def get_rule_order(tickets, rules):
    rules_valid = {}
    rules_not_valid = {}
    for ticket in tickets:
        for i, number in enumerate(ticket):
            for rule in rules.keys():
                if not rules_not_valid.get(rule):
                    rules_not_valid[rule] = set()
                if not rules_valid.get(rule):
                    rules_valid[rule] = set()
                if check_rule(int(number), rules.get(rule)) and i not in rules_not_valid.get(rule):
                    rules_valid[rule].add(i)
                else:
                    rules_not_valid[rule].add(i)
                    if rules_valid.get(rule) and i in rules_valid[rule]:
                        rules_valid[rule].remove(i)
    rules_with_pos = ["" for key in rules.keys()]
    while "" in rules_with_pos:
        for rule in rules_valid.keys():
            if len(rules_valid.get(rule)) == 1:
                pos = rules_valid.get(rule).pop()
                rules_valid.pop(rule, None)
                rules_with_pos[pos] = rule
                for rule_to_remove in rules_valid.keys():
                    if rule_to_remove != rule and pos in rules_valid.get(rule_to_remove):
                        rules_valid[rule_to_remove].remove(pos)
                break
    return rules_with_pos


valid_tickets = [ticket for ticket in nearby if ticket_valid(ticket, rules)]
rule_order = get_rule_order(valid_tickets, rules)
positions = [pos for pos, rule in enumerate(rule_order) if rule.startswith("departure")]

product = 1
for position in positions:
    product *= int(ticket[position])

print(f"The product is {product}")
