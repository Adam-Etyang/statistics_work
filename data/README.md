# Data Files

This folder contains the raw data files used for statistical analysis and visualization.

## Files

### `DATA.xlsx`

- **Format**: Excel spreadsheet (.xlsx)
- **Sheet**: Sheet1
- **Variables**:
  - `Hours_Coding`: Number of hours spent coding (independent variable)
  - `Num_Bugs`: Number of bugs found in the code (dependent variable)
- **Purpose**: Primary dataset for analyzing the relationship between coding time and bug frequency

## Data Description

This dataset appears to be used for studying the correlation between the amount of time spent coding and the number of bugs that are introduced or found in the code. The data is used across multiple analysis scripts in this project for:

- Scatter plot visualization
- Histogram analysis with KDE
- Linear regression modeling
- Correlation coefficient calculation

## Usage

All analysis and visualization scripts reference this data file using the path `../data/DATA.xlsx` relative to their respective folders.
