import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

def train():
    # Determine the correct path to the data file
    data_path = os.path.join(os.path.dirname(__file__), '../data/my_data.csv')
    
    # Load the data
    df = pd.read_csv(data_path)
    X = df[['id', 'feature1', 'feature2']]
    y = df['value']

    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Ensure the models directory exists
    models_dir = os.path.join(os.path.dirname(__file__), '../models')
    os.makedirs(models_dir, exist_ok=True)

    # Save the model
    model_path = os.path.join(models_dir, 'model.pkl')
    joblib.dump(model, model_path)

if __name__ == '__main__':
    train()
