import os
import glob 
import numpy as np
import pandas as pd

def build_histogram(sensor_path, bin_edges):
    hist = np.zeros(len(bin_edges) - 1, dtype=np.int64)
    file_pattern = os.path.join(sensor_path, "*.csv")
    file_list = glob.glob(file_pattern)
    total_file = len(file_list)
    print(f"Found {total_file} files in {sensor_path}")

    for idx, file in enumerate(file_list):
        # Read CSV with delimiter and no header
        df = pd.read_csv(file, header=None, sep='\s+')

        # Extract x, y, z or column 0, 1, 2
        x = df[0].values
        y = df[1].values
        z = df[2].values

        # Calculate Euclidean distances
        distances = np.sqrt(x**2 + y**2 + z**2)

        # Histogram
        hist += np.histogram(distances, bins=bin_edges)[0]
        if (idx+1) % 50 == 0:
            print(f"Processed {idx+1}/{total_file} files")
    return hist

if __name__ == "__main__":
    # Define bin edges
    bin_edges = np.linspace(0, 100, 101)
    
    # Path
    clear_radar_path = "../data/c_building_pedestrian_clear_anon/radar"

    print("Building histogram for radar (clear)...")
    radar_hist = build_histogram(clear_radar_path, bin_edges)
    print("Histogram counts (first 10 bins):", radar_hist[:10])