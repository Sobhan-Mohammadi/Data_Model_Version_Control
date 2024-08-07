import pandas as pd

data = {
    'id': range(1, 11),
    'value': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
    'feature1': [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.0],
    'feature2': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
}

more_data = {
    'id': range(11, 21),
    'value': [1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],
    'feature1': [11.1, 12.2, 13.3, 14.4, 15.5, 16.6, 17.7, 18.8, 19.9, 20.0],
    'feature2': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}

# Create dataframes
df_data = pd.DataFrame(data)
df_more_data = pd.DataFrame(more_data)

# Save dataframes to CSV
df_data.to_csv('/home/sobhan/Desktop/Esbaar/Projects/DVC/my_ml_project_2/data/my_data.csv', index=False)
df_more_data.to_csv('/home/sobhan/Desktop/Esbaar/Projects/DVC/my_ml_project_2/data/more_data.csv', index=False)
