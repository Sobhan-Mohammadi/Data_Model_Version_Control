import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def train():
    # Load the data
    df = pd.read_csv('../data/my_data.csv')
    X = df[['id', 'feature1', 'feature2']]
    y = df['value']

    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Save the model
    joblib.dump(model, '../models/model.pkl')

if __name__ == '__main__':
    train()
