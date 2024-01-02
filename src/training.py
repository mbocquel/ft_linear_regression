import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sys import argv


def calculateCostSquareError(theta0, theta1, mileage, price):
    """
    Function that calcultate the cost square error
    for a linear regression, provided
    """
    return (1/(2*len(mileage)) * sum((theta1*mileage + theta0 - price)**2))


def plotResults(mileage, price, theta0, theta1, result):
    """
    Show data and model in a graph
    """
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    x = np.linspace(min(mileage), max(mileage), 2)
    plt.plot(mileage, price, 'o', label="Dataset")
    plt.plot(x, theta1*x + theta0, 'r', label="Linear Regression")
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.title("Evolution of the price of car with mileage")
    plt.legend()
    plt.subplot(1, 2, 2)
    x = range(len(result))
    plt.plot(x, result.loc[:, 'Cost'], 'b')
    plt.xlabel("Algo iterations")
    plt.ylabel("Mean square Error")
    plt.title("Evolution of the Cost with gradient descent iterations")
    plt.show()


def updateParams(mileageN, price, theta0, theta1, alpha):
    """
    Function that simultaneously update theta0 and
    theta1 using the partial derivative
    """
    temptheta0 = theta0 - alpha * (
        1/len(mileageN)) * sum(theta1 * mileageN + theta0 - price)
    temptheta1 = theta1 - alpha * (
        1/len(mileageN)) * sum((theta1 * mileageN + theta0 - price) * mileageN)
    return (temptheta0, temptheta1)


def normilisedDataSet(data):
    """
    Function that z-score normalize the data
    """
    mean = data.mean()
    std = data.std()
    normilised = (data - mean) / std
    return (normilised, mean, std)


def executeGradientDescentAlgo(mileageN, price, alpha):
    """
    Where the gradient descent algorithm is executed for 100 iterations.
    """
    theta0_N = 0
    theta1_N = 0
    result = pd.DataFrame(columns=['theta0_N', 'theta1_N', "Cost"])
    result.loc[len(result)] = [theta0_N, theta1_N,
                               calculateCostSquareError(theta0_N,
                                                        theta1_N,
                                                        mileageN,
                                                        price)]
    for i in range(100):
        theta0_N, theta1_N = updateParams(mileageN,
                                          price,
                                          theta0_N,
                                          theta1_N,
                                          alpha)
        result.loc[len(result)] = [theta0_N, theta1_N,
                                   calculateCostSquareError(theta0_N,
                                                            theta1_N,
                                                            mileageN,
                                                            price)]
    return (theta0_N, theta1_N, result)


def main():
    """
    Program that uses Machine Learning to find the corect
    parameters for a linear regression.
    """
    try:
        assert len(argv) == 2, "You need to pass your data file as argument"
        df = pd.read_csv(argv[1])
        assert df is not None, "There is a problem with the dataset..."
        price = df.loc[:, 'price']
        mileage = df.loc[:, 'km']
        mileageN, mileageMean, mileageStd = normilisedDataSet(mileage)
        alpha = 0.1
        theta0_N, theta1_N, result = executeGradientDescentAlgo(mileageN,
                                                                price,
                                                                alpha)
        theta0 = theta0_N - (theta1_N * mileageMean / mileageStd)
        theta1 = theta1_N / mileageStd
        print("Training model result (price = theta0 + theta1 * mileage) :")
        print("     theta0 :", theta0)
        print("     theta1 :", theta1)
        params = pd.DataFrame({'theta0': [theta0],
                               'theta1': [theta1]})
        params.to_csv("params.csv", index=False)
        plotResults(mileage, price, theta0, theta1, result)
        return 0
    except AssertionError as msg:
        print("Error:", msg)
        return 1
    except Exception as err:
        print("Error: ", err)
        return 1


if __name__ == "__main__":
    main()
