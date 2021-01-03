from helper import get_data

data = open(get_data(18), 'r').read().split('\n')

"""
--- Day 18: Operation Order ---

As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted 
by the child sitting next to you. They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*), 
and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated before
it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator,
and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, the
operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                 71
Parentheses can override this order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) + 
(4 * (5 + 6)):

1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51
Here are a few more examples:

2 * 3 + (4 * 5) becomes 26.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.

Before you can help with the homework, you need to understand it yourself. Evaluate the expression on each line of the 
homework; what is the sum of the resulting values?
"""


def solve_equation(equation_string):
    result = 0
    last_operator = None
    pos = 0
    while pos < len(equation_string):
        part = equation_string[pos]
        if part.isnumeric():
            number = int(part)
            pos += 2
        elif '(' in part:
            subequation = get_closing_bracket(equation_string[pos + 1:])
            number = solve_equation(subequation)
            pos += len(subequation) + 3
        else:
            if part == '*' or part == '+':
                last_operator = part
                pos += 2
            else:
                pos += 3
            continue
        if last_operator == '*':
            result *= number
        else:
            result += number
    return result


def get_closing_bracket(equation_string):
    brackets = 1
    for i, part in enumerate(equation_string):
        if part == ')':
            brackets -= 1
        elif part == '(':
            brackets += 1
        if brackets == 0:
            return equation_string[:i]


results = list()
for equation in data:
    results.append(solve_equation(equation))

print(f"The sum of all results is {sum(results)}")

"""
--- Part Two ---

You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the 
next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with. 
Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231
Here are the other examples from above:

1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
2 * 3 + (4 * 5) becomes 46.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.
What do you get if you add up the results of evaluating the homework problems using these new rules?
"""


def solve_equation_2(equation_string):
    result = 1
    pos = 0
    while pos < len(equation_string):
        part = equation_string[pos]
        if part.isnumeric():
            number = int(part)
            pos += 2
        elif part == '*':
            result *= number
            pos += 2
        elif part == '+':
            number, pos_add = get_addition_part(equation_string[pos + 2:], number)
            pos += pos_add + 2
        elif '(' in part:
            subequation = get_closing_bracket(equation_string[pos + 1:])
            number = solve_equation_2(subequation)
            pos += len(subequation) + 3
    result *= number
    return result


def get_addition_part(equation_string, sum):
    pos = 0
    while pos < len(equation_string) and equation_string[pos] != '*':
        part = equation_string[pos]
        if part.isnumeric():
            sum += int(part)
            pos += 2
        elif part == '(':
            subequation = get_closing_bracket(equation_string[pos + 1:])
            sum += solve_equation_2(subequation)
            pos += len(subequation) + 3
        else:
            pos += 2
    return sum, pos


results = list()
for equation in data:
    results.append(solve_equation_2(equation))

print(f"The sum of all results in part 2 is {sum(results)}")
