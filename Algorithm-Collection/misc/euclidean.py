def euclidean(x, y):
    """ finds the greatest common denominator of two numbers """
    if y == 0:
        return x

    z = x % y
    return euclidean(y, z)


def main():
    x = int(input("First Number: "))
    y = int(input("Second Number: "))

    print("Greatest Common Denominator: " + str(euclidean(x, y)))


if __name__ == "__main__":
    main()
