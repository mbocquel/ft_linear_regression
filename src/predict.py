from sys import argv


def testParamsAreFloat(str):
    """
    Function that make sure that the parameters are correct numbers.
    """
    try:
        result = float(str)
        return (result)
    except ValueError:
        return (None)


def main():
    """
    Program that estimate the price of a car using linear regression.
    The program requires theta0 and theta1 as argument.
    These parameters must be first estimate using the trainning program.
    """
    try:
        assert len(argv) == 3, "Please provide theta0 and theta1"
        theta0 = testParamsAreFloat(argv[1])
        theta1 = testParamsAreFloat(argv[2])
        assert (theta1 is not None and theta0 is not None), "theta0 and theta1 must be numbers"
        mileage = None
        while (mileage is None or mileage < 0):
            mileage = testParamsAreFloat(input("Please enter a car mileage in km : "))
            if (mileage is None or mileage < 0):
                print("     \033[31mPlease enter a correct positif number...\n\033[0m")
        price = theta0 + theta1 * mileage
        print("     \033[32mThe expected price is :", "{:.2f}".format(max(0, price)), "euros\033[0m")
    except AssertionError as msg:
        print("Error:", msg)
    except Exception as err:
        print("Error: ", err)


if __name__ == "__main__":
    main()
