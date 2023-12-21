import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load(path: str) -> pd.DataFrame | None:
    """
    Function that load data from a csv file and return the panda dataFrame
    Return None if there was a problem
    """
    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape)
        return (df)
    except Exception as e:
        print(e)
        return None


def calculateCostSquareError(theta0: float, theta1:float, df:pd.DataFrame) -> float:
    mileage = df.loc[:,'km']
    price = df.loc[:,'price']
    return(1/(2*len(df)) * sum((theta1*mileage + theta0 - price)**2))


def plotDataSetAndRegLin(mileage, price, theta0, theta1):
    x = np.linspace(min(mileage), max(mileage), 2)
    fig, ax = plt.subplots()
    plt.plot(mileage, price, 'o')
    plt.plot(x, theta1*x + theta0, 'r' ,  label="Reg Linear")
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.title("Evolution of the price of car with mileage")
    plt.legend()
    plt.show()


def updateParams(mileage, price, theta0, theta1, alpha):
    temptheta0 = theta0 - alpha * (1/len(mileage)) * sum(theta1 * mileage + theta0 - price)
    temptheta1 = theta1 - alpha * (1/len(mileage)) * sum((theta1 * mileage + theta0 - price) * mileage)
    # theta0 = temptheta0
    # theta1 = temptheta1
    return (temptheta0, temptheta1)

def main():
    """
    Program that open the lifeexpectancy
    file and display france
    """
    try:
        df = load("data.csv")
        mileage = df.loc[:,'km']
        price = df.loc[:,'price']
        theta0 = 8000
        theta1 = -1/50
        alpha = 0.01
        print(theta1)
        result = pd.DataFrame(columns=['theta0', 'theta1', "cost"])
        result.loc[len(result)] = [theta0, theta1, calculateCostSquareError(theta0, theta1, df)]
        for i in range(100):
            theta0, theta1 = updateParams(mileage, price, theta0, theta1, alpha)
            result.loc[len(result)] = [theta0, theta1, calculateCostSquareError(theta0, theta1, df)]
        print(result)
 
        # plotDataSetAndRegLin(mileage, price, theta0, theta1)
        # for i in range(15):
        #     theta0, theta1 = updateParams(mileage, price, theta0, theta1, alpha)
        #     print([theta0, theta1])
        #     plotDataSetAndRegLin(mileage, price, theta0, theta1)
        
    except Exception as err:
        print("Error: ", err)


if __name__ == "__main__":
    main()
