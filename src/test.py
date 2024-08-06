import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error

def test():
    # Load the test data
    df = pd.read_csv('../data/more_data.csv')
    X = df[['id', 'feature1', 'feature2']]
    y_true = df['value']

    # Load the trained model
    model = joblib.load('../models/model.pkl')

    # Make predictions
    y_pred = model.predict(X)

    # Calculate the mean squared error
    mse = mean_squared_error(y_true, y_pred)
    print(f'Mean Squared Error: {mse}')

if __name__ == '__main__':
    test()
