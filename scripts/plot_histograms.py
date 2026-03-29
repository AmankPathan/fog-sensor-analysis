import numpy as np 
import matplotlib.pyplot as plt
import os

# Load the saved histogram file
data = np.load('histograms.npz')

bin_edges = np.linspace(0, 100, 101)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

sensors = ['radar', 'velodyne', 'blickfeld']
conditions = ['clear', 'fog']

os.makedirs('../figures', exist_ok=True)

for sensor in sensors:
    plt.figure(figsize=(10, 6))
    for condition in conditions:
        key = f"{sensor}_{condition}"
        counts = data[key]
        plt.plot(bin_centers, counts, label=condition.capitalize(), linewidth=2)
    
    plt.xlabel('Distance (m)', fontsize=12)
    plt.ylabel('Number of Points', fontsize=12)
    plt.title(f'{sensor.capitalize()} – Clear vs Fog', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 60)

    # Save Figure
    plt.savefig(f'../figures/{sensor}_histogram.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved {sensor}_histogram.png")

print("All plots generated.")