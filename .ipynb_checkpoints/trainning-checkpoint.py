import pandas as pd
import matplotlib.pyplot as plt


def load(path: str) -> pd.DataFrame | None:
    """
    Function that load data from a csv file and return the panda dataFrame
    Return None if there was a problem
    """
    try:
        df = pd.read_csv(path, index_col=0)
        print("Loading dataset of dimensions", df.shape)
        return (df)
    except Exception as e:
        print(e)
        return None


# def calculateCostSquareError(theta0: float, theta1:float, dataframe:pd.DataFrame) -> float:
    


def main():
    """
    Program that open the lifeexpectancy
    file and display france
    """
    try:
        df = load("data.csv")
        mileage = df.loc[:'km']
        price = df.loc[:'price']
        plt.plot(mileage, price, 'o')
        plt.xlabel("Mileage")
        plt.ylabel("Price")
        plt.title("Dataset")
        plt.show()
    except Exception as err:
        print("Error: ", err)


if __name__ == "__main__":
    main()
