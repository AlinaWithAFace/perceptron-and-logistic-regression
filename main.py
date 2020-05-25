def main(user_input):
    print(user_input)

    command = user_input[0]
    if command == "P":
        perceptron(user_input[1:])
    elif command == "L":
        logistic_regression(user_input[1:])


def perceptron(tuples):
    print(tuples)


def logistic_regression(tuples):
    print(tuples)
    # (w=w+α * g(w))


def tests():
    main("P (0, 2,+1) (2, 0, -1) (0, 4,+1) (4, 0, -1)")
    # -1, +1

    main("L (0, 2,+1) (2, 0, -1) (0, 4, -1) (4, 0, +1) (0, 6, -1) (6, 0, +1)")
    # 0.5 0.6 0.23 0.12 0.78 0.21


tests()
