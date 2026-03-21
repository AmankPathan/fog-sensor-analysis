import pandas as pd
import os

sensor = "velodyne"
file_name = "000000.csv"

file_path = os.path.join("..", "data", "c_building_pedestrian_clear_anon", sensor, file_name)

# Read with space delimiter, no header
df = pd.read_csv(file_path, header=None, delim_whitespace=True)

print(f"Sensor: {sensor}")
print(f"Shape: {df.shape} rows × {df.shape[1]} columns")
print("\nFirst 3 rows:")
print(df.head(3))