def better_calculator():
    print("better calculator")
    equation = input("do it:")
    numbers = []
    currentNumber = []
    for char in equation:
        if char in "123456789":
            currentNumber.append(char)

        if char in "+=-/* ":
            numbers.append(int("{}".join(currentNumber)))
            if char != " ":
                numbers.append(char)
            currentNumber = []

    patients = []
    intermittent = 0
    operator = ""
    for _ in numbers:
        if _ in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
            patients.append(_)

        elif _ in "+=-/*":
            operator = _

        if len(patients) == 2 and operator != "":
            if operator == "+":
                intermittent = (patients[0] + patients[1])

            if operator == "-":
                intermittent = (patients[0] - patients[1])

            if operator == "/":
                intermittent = (patients[0] / patients[1])

            if operator == "*":
                intermittent = (patients[0] * patients[1])

            patients[0] = intermittent

    print(intermittent)
