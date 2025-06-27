# Data Visualization Scripts

This folder contains Python scripts for creating various data visualizations from the statistics dataset.

## Files

### `plots.py`

- **Purpose**: Creates a scatter plot showing the relationship between hours coding and number of bugs
- **Features**:
  - Purple scatter plot with circular markers
  - Grid lines for better readability
  - Saves output as `my_scatter_plot.png` in the plots folder
- **Dependencies**: pandas, matplotlib

### `frequency_dist_table.py`

- **Purpose**: Creates a histogram with Kernel Density Estimation (KDE) curve for the number of bugs
- **Features**:
  - Histogram with 10-bin intervals (0-70 bugs)
  - Overlaid KDE curve for smooth distribution visualization
  - Sky blue color scheme with black edges
  - Saves output as `bug_histogram_with_kde.png` in the plots folder
- **Dependencies**: pandas, seaborn, matplotlib, numpy

## Usage

Run these scripts from the root directory of the project to generate visualizations. The scripts will automatically save the plots to the `../plots/` folder.
