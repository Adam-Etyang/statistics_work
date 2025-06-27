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

- **Purpose**: Creates a histogram with frequency distribution for the number of bugs
- **Features**:
  - Histogram with 10-bin intervals (0-60 bugs)
  - Sky blue bars with black edges
  - Frequency count per interval
  - Saves output as `histogram_of_number_of_bugs.png` in the plots folder
- **Dependencies**: pandas, matplotlib, numpy

### `normal_curve.py`

- **Purpose**: Creates a histogram with overlaid normal distribution curve
- **Features**:
  - Histogram with 10-bin intervals (0-60 bugs)
  - Red normal curve overlay showing theoretical normal distribution
  - Displays mean (μ) and standard deviation (σ) in legend
  - Semi-transparent histogram bars for better curve visibility
  - Saves output as `histogram_of_number_of_bugs_with_normal_curve.png` in the plots folder
- **Dependencies**: pandas, matplotlib, numpy, scipy.stats

## Usage

Run these scripts from the root directory of the project to generate visualizations. The scripts will automatically save the plots to the `../plots/` folder.
