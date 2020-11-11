import time
import uuid
import operator

NUMBERS = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
TERMINATE_CHAR = "!"
OPERATORS = {
    '^': operator.xor,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '+': operator.add,
    '-': operator.sub
}


def main():
    main_menu()
    equation = parse(input())
    print(equation)
    sortedEq = sort(equation)
    print(sortedEq)

    output = 0

    for eq in sortedEq:
        print(eq)
        output += evaluate(eq)

    print(output)


def main_menu():
    print("welcome to the python calculator beta")
    print("type negative NUMBERS in brackets []. input equation below\n")


def parse(eq):

    parsedEquations = []
    currentEq = ""
    skip = False

    if "()" not in eq:
        parsedEquations.append(chunk(eq))
        return parsedEquations

    # iterate over equation seperating at parentheses
    for index, char in enumerate(eq):
        if skip:
            skip = False
            continue

        # beginning parentheses case
        if char == "(":
            # skip '(' and add the number after to the current equation
            currentEq += eq[(index + 1)]
            skip = True

        # end of parentheses case
        if char == ")":
            parsedEquations.append(chunk(currentEq))
            continue

        # regular character case
        if char in NUMBERS or OPERATORS and char not in "()":
            currentEq += char

        # ignore all whitespace
        if char == " ":
            continue

    return parsedEquations


def chunk(eq):
    # workaround for there being no operator sign at the end of an equation
    eq = eq + TERMINATE_CHAR

    chunk = ""
    chunkedEquation = {}
    skip = False

    # iterate over equation, seperating at operators
    for index, char in enumerate(eq):
        if skip:
            skip = False
            continue

        # regular number case
        elif char in NUMBERS:
            chunk += char

        # negative number format case
        elif char == "[":
            # skip '[' and add the number after to the current chunk
            chunk += eq[(index + 1)]
            skip = True

        # end of negative number format case
        elif char == "]":
            continue

        # operator is detected case
        elif char in OPERATORS:
            # assign a uuid to chunk, add current chunk and operator (the current char) to an array
            chunkedEquation[uuid.uuid4()] = [chunk, char]
            chunk = ""  # clear chunk so next one is blank

        # terminating char detected case
        elif char == TERMINATE_CHAR:
            # assign uuid similar to above, this time with terminating character as operator instead
            chunkedEquation[uuid.uuid4()] = [chunk, TERMINATE_CHAR]

        # ignore all whitespace
        elif char == " ":
            continue

        # if no cases are hit above, generate syntax error
        else:
            print("user generated syntax error")
            return

    return chunkedEquation


def sort(eq):
    pemdas = {}
    output = []

    for subEq in eq:
        # build pemdas from scratch for added simplification when new operators are added
        for weight, operator in enumerate(OPERATORS):
            pemdas[operator] = len(OPERATORS) - weight

        # assign terminating character a weighted value of 0
        pemdas[TERMINATE_CHAR] = 0

        # replace all operators in equation with weighted values assigned above
        for chunkID, chunk in subEq.items():
            subEq[chunkID] = [chunk[0], pemdas[chunk[1]]]

        # sort the subEq by key values
        sortedEq = sorted(subEq.values(), key=lambda x: x[1], reverse=True)
        for index, chunkID in enumerate(subEq.keys()):
            subEq[chunkID] = sortedEq[index]

        # restore all operators
        for chunkID, chunk in subEq.items():
            operator = list(pemdas.keys())[list(
                pemdas.values()).index(chunk[1])]

            # sort lambda converted 0th indice to a string
            subEq[chunkID] = [int(chunk[0]), operator]

        output.append(subEq)

    return output


def evaluate(eq):
    output = None
    previousOperator = None
    previousChunk = None

    for chunkID, chunk in eq.items():
        op = chunk[1]  # take current chunk operator to apply
        chunk = int(chunk[0])  # current numeric value "the chunk"

        # if first number in the equation, skip and store values
        if not previousOperator:
            previousOperator = op
            previousChunk = chunk
            continue

        # if output has not changed, evaluate previous (first number) and current number
        if output is None:
            output = OPERATORS[previousOperator](previousChunk, chunk)
            previousOperator = op
            continue

        # else, simply use evaluate using operators library
        output = OPERATORS[previousOperator](output, chunk)
        previousOperator = op

    return output


if __name__ == "__main__":
    main()
