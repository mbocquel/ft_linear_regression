from sys import argv
from load_csv import load
import pandas as pd


def testParamsAreFloat(str):
    """
    Function that make sure that the parameters are correct numbers.
    """
    try:
        result = float(str)
        return (result)
    except ValueError:
        return (None)


def calculateCostMSE(theta0, theta1, mileage, price):
    """
    Function that calcultate the cost square error
    for a linear regression, provided
    """
    return (1/(2*len(mileage)) * sum((theta1*mileage + theta0 - price)**2))


def printPrecisionStats(df: pd.DataFrame, theta0: float, theta1: float):
    """
    Calculate and print the model performance statistics
    """
    price = df.loc[:, 'price']
    mileage = df.loc[:, 'km']
    mse = 1/len(mileage) * sum((price - (theta0 + theta1 * mileage))**2)
    rmse = mse ** (1/2)
    mean = sum(price) / len(price)
    var = sum((price - mean)**2) / len(price)
    r2 = 1 - mse/var
    print("---------- Model performances statistics ----------")
    print("MEAN SQUARED ERROR (MSE):", "{:.5f}".format(mse))
    print("ROOT MEAN SQUARED ERROR (RMSE):", "{:.5f}".format(rmse))
    print("R-SQUARED (coefficient of determination):", "{:.5f}".format(r2))
    print("---------------------------------------------------")


def main():
    """
    Program that takes a data set and the theta value of
    the linear regression model (y = theta0 + theta1 * x1)
    and return statistics about the model precision
    """
    try:
        assert len(argv) == 4, "Expected arguments : dataset theta0 theta1"
        df = load(argv[1])
        assert df is not None, "There is a problem with the dataset..."
        theta0 = testParamsAreFloat(argv[2])
        theta1 = testParamsAreFloat(argv[3])
        assert (theta1 is not None and theta0 is not None), "thetas not num"
        printPrecisionStats(df, theta0, theta1)
        return 0
    except AssertionError as msg:
        print("Error:", msg)
        return 1
    except Exception as err:
        print("Error: ", err)


if __name__ == "__main__":
    main()
