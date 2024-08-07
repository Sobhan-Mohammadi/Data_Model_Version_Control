import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, r2_score
import os

def test():
    # Determine the correct path to the data file
    data_path = os.path.join(os.path.dirname(__file__), '../data/more_data.csv')

    # Load the test data
    df = pd.read_csv(data_path)
    X = df[['id', 'feature1', 'feature2']]
    y_true = df['value']

    # Load the trained model
    model_path = os.path.join(os.path.dirname(__file__), '../models/model.pkl')
    model = joblib.load(model_path)

    # Make predictions
    y_pred = model.predict(X)

    # Calculate the mean squared error
    mse = mean_squared_error(y_true, y_pred)
    print(f'Mean Squared Error: {mse}')

    r2 = r2_score(y_true, y_pred)
    print(f'R2 Score: {r2}')

if __name__ == '__main__':
    test()
