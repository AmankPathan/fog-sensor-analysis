import os
import glob
import numpy as np
import pandas as pd

def build_histogram(sensor_path, bin_edges):
    """
    sensor_path: path to a folder containing .csv files for one sensor
    bin_edges: numpy array of bin edges (e.g., np.linspace(0, 100, 101))
    Returns: histogram counts (list of same length as bin_edges-1)
    """
    hist = np.zeros(len(bin_edges) - 1, dtype=np.int64)
    file_pattern = os.path.join(sensor_path, "*.csv")
    file_list = glob.glob(file_pattern)
    total_files = len(file_list)
    print(f"Found {total_files} files in {sensor_path}")

    for idx, file in enumerate(file_list):
        df = pd.read_csv(file, header=None, sep='\s+')
        x = df[0].values
        y = df[1].values
        z = df[2].values
        distances = np.sqrt(x**2 + y**2 + z**2)
        hist += np.histogram(distances, bins=bin_edges)[0]
        if (idx+1) % 50 == 0:
            print(f"Processed {idx+1}/{total_files} files")
    return hist

if __name__ == "__main__":
    # Define bin edges from 0 to 100 m, step 1 m
    bin_edges = np.linspace(0, 100, 101)

    # Define sensors and conditions
    sensors = ['radar', 'velodyne', 'blickfeld']
    conditions = ['clear', 'fog']

    # Base path: adjust if your dataset is in a different location
    base_path = '../data'

    # Store histograms in a dictionary: histograms[sensor][condition]
    histograms = {}

    for sensor in sensors:
        histograms[sensor] = {}
        for condition in conditions:
            print(f"\nProcessing {sensor} ({condition})...")
            sensor_path = os.path.join(base_path, f'c_building_pedestrian_{condition}_anon', sensor)
            hist = build_histogram(sensor_path, bin_edges)
            histograms[sensor][condition] = hist
            print(f"First 10 bins: {hist[:10]}")

    print("\nAll histograms built successfully.")
    # Optional: save the histograms to a file for later use (we'll do that later)

    # Save histograms to a compressed numpy file
    save_dict = {}
    for sensor in sensors:
        for condition in conditions:
            key = f"{sensor}_{condition}"
            save_dict[key] = histograms[sensor][condition]
    np.savez_compressed('histograms.npz', **save_dict)
    print("Histograms saved to histograms.npz")