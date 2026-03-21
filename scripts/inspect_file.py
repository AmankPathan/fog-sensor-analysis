import pandas as pd
import os

sensor = "velodyne"
file_name = "000000.csv"

file_path = os.path.join("..", "data", "c_building_pedestrian_clear_anon", sensor, file_name)

df = pd.read_csv(file_path, header=None)

print(f"File: {file_path}")
print(f"Shape: {df.shape} rows x {df.shape[1]} columns")
print("\nFirst 5 rows:")
print(df.head()) 