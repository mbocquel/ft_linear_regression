from sys import argv
import pandas as pd
import os.path


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
        assert len(argv) == 1, "Wrong number of arguments"
        check_file = os.path.isfile("params.csv")
        if (not check_file):
            theta = pd.DataFrame({'theta0': [0],
                               'theta1': [0]})
            theta.to_csv("params.csv", index=False)
        else:
            theta = pd.read_csv("params.csv")
        theta0 = testParamsAreFloat(theta.loc[0,'theta0'])
        theta1 = testParamsAreFloat(theta.loc[0,'theta1'])
        assert (theta1 is not None and theta0 is not None), "thetas not num"
        mileage = None
        while (mileage is None or mileage < 0):
            mileage = testParamsAreFloat(
                input("Please enter a car mileage in km : "))
            if (mileage is None or mileage < 0):
                print("\033[31mEnter a correct positif or nul number\n\033[0m")
        price = theta0 + theta1 * mileage
        print("     \033[32mThe expected price is :",
              "{:.2f}".format(max(0, price)), "euros\033[0m")
        return 0
    except AssertionError as msg:
        print("Error:", msg)
        return 1
    except Exception as err:
        print("Error: ", err)
        return 1


if __name__ == "__main__":
    main()
