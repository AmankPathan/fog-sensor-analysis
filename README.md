# Fog Influence on LIDAR and Radar Sensors – Analysis Report

## Objective
Evaluate the impact of artificial fog on three sensors:  
- **Velodyne Puck** (rotating 360° LIDAR)  
- **Blickfeld Cube 1** (solid‑state LIDAR)  
- **Texas Instruments MMWAVCAS‑RF‑EVM** (radar)  

Two scenes were compared: `c_building_pedestrian_clear_anon` (clear) and `c_building_pedestrian_fog_anon` (fog).  
For each sensor, histograms of point distances were generated (0–60 m range, 1 m bins).

## Methodology
- CSV files (space‑separated, no headers) were read for each sensor/condition.
- Coordinates (x, y, z) were extracted from columns 0,1,2.
- Euclidean distance `sqrt(x²+y²+z²)` computed for every point.
- Histograms accumulated over all files (500 files per sensor/condition).
- Plots created using Matplotlib (line plots of bin counts).

## Results & Discussion

### Radar (MMWAVCAS‑RF‑EVM)
- **Clear vs Fog**: Histograms are nearly identical; minor differences are within natural scene variation.
- **Conclusion**: Fog has **no measurable influence** on radar measurements. This is expected due to the longer wavelength (mm‑wave) which penetrates fog particles with negligible scattering/attenuation.

### Velodyne Puck (LIDAR)
- **Clear**: Wide distribution of points up to ~100 m, reflecting typical outdoor ranging.
- **Fog**:
  - Sharp drop in point counts beyond ~15 m.
  - Almost no detections beyond 25 m.
  - Some range bins show missing points entirely – consistent with the PDF’s observation of “missing scan lines”.
- **Conclusion**: Fog severely degrades Velodyne’s performance. The 905 nm laser is strongly attenuated and scattered by water droplets, making long‑range detection impossible. The rotating mechanism may also introduce blind zones due to uneven fog density.

### Blickfeld Cube 1 (LIDAR)
- **Clear**: Typical LIDAR distribution with good range up to ~60 m.
- **Fog**:
  - **Increased counts at close range (0–10 m)** – attributed to backscatter from fog particles directly in front of the sensor (false positives).
  - Reduced counts beyond 20 m, though not as drastic as Velodyne.
- **Conclusion**: Fog affects Blickfeld mainly by creating near‑field noise and reducing far‑field sensitivity. Its solid‑state design may be less prone to missing entire scan lines, but backscatter remains a challenge.

## Summary Table

| Sensor         | Fog Effect on Detection Range | Close‑Range Noise | Overall Robustness |
|----------------|-------------------------------|-------------------|--------------------|
| Radar          | None                          | None              | High               |
| Velodyne Puck  | Severe loss >15 m             | None               | Low                |
| Blickfeld Cube | Moderate loss >20 m           | High (0–10 m)      | Medium             |

## Recommendations
- For autonomous systems operating in foggy conditions, **radar should be the primary long‑range sensor**.
- LIDAR sensors can still provide useful short‑range data if backscatter is filtered (e.g., by intensity thresholding or spatial clustering).
- Sensor fusion (radar + LIDAR + camera) can compensate for individual weaknesses.

## Repository Contents
- `scripts/` – all Python code for loading, processing, and plotting.
- `figures/` – generated histograms (radar, velodyne, blickfeld).
- `data/` – ignored by Git (large dataset).

---

**Author:** Amankhan Riyasat Pathan