# Statistics Work - ICS 2025

A comprehensive statistical analysis project examining the relationship between coding hours and bug frequency.

## Project Structure

This repository is organized into the following folders:

### 📊 `data_visualization/`

Contains Python scripts for creating data visualizations:

- `plots.py` - Scatter plot of hours coding vs bugs
- `frequency_dist_table.py` - Histogram with KDE curve

### 📈 `statistical_analysis/`

Contains Python scripts for statistical analysis:

- `lin_regression.py` - Linear regression modeling
- `correlation_coefficient(r).py` - Pearson correlation analysis

### 📁 `data/`

Contains the raw dataset:

- `DATA.xlsx` - Excel file with Hours_Coding and Num_Bugs variables

### 🖼️ `plots/`

Contains all generated visualizations:

- Scatter plots, histograms, and distribution plots

### 📚 `documentation/`

Contains project documentation:

- `Assignment_ICS_2025.pdf` - Original assignment instructions

## Quick Start

1. **Install Dependencies**:

   ```bash
   pip install pandas matplotlib seaborn scipy scikit-learn numpy
   ```

2. **Run Analysis**:

   - For visualizations: Run scripts in `data_visualization/`
   - For statistical analysis: Run scripts in `statistical_analysis/`

3. **View Results**:
   - Generated plots are saved in `plots/`
   - Statistical results are printed to console

## Analysis Overview

This project analyzes the correlation between:

- **Independent Variable**: Hours spent coding
- **Dependent Variable**: Number of bugs found

The analysis includes descriptive statistics, data visualization, correlation analysis, and linear regression modeling to understand the relationship between coding time and bug frequency.
