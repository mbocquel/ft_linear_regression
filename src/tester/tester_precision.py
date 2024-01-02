import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sys import argv


def main():
    """
    Tester program that uses a library to do the linear regression
    and to calculate the performances indicators
    """
    try:
        df = pd.read_csv(argv[1])
        y = df.price
        X = df[['km']]

        # Train the model
        lm = LinearRegression()
        lm.fit(X, y)
        print("sklearn library LinearRegression theta0: ", lm.intercept_)
        print("sklearn library LinearRegression theta1: ", lm.coef_[0])

        # Predict on the test data
        X_test = df[['km']]
        y_test = df.price
        y_pred = lm.predict(X_test)

        # Compute the root-mean-square
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        print("sklearn MSE:", "{:.5f}".format(mse))
        print("sklearn RMSE:", "{:.5f}".format(rmse))
        print("sklearn R-SQUARED:", "{:.5f}".format(r2))
        return 0
    except Exception as err:
        print("Error: ", err)
        return 1


if __name__ == "__main__":
    main()
