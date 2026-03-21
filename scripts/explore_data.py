import pandas as pd

# Path for .csv
file_path = "../data/c_building_pedestrian_clear_anon/radar/000000.csv"

df = pd.read_csv(file_path, nrows=1000)

print("column names:\n", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())

