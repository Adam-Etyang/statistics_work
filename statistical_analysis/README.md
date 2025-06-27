# Statistical Analysis Scripts

This folder contains Python scripts for performing statistical analysis on the coding hours and bugs dataset.

## Files

### `lin_regression.py`

- **Purpose**: Performs linear regression analysis to model the relationship between hours coding and number of bugs
- **Features**:
  - Fits a linear regression model using scikit-learn
  - Calculates and displays the regression equation (y = a + bx)
  - Makes predictions (e.g., predicted bugs for 20 hours of coding)
  - Uses Hours_Coding as independent variable and Num_Bugs as dependent variable
- **Dependencies**: sklearn, numpy, pandas

### `correlation_coefficient(r).py`

- **Purpose**: Calculates the Pearson correlation coefficient between hours coding and number of bugs
- **Features**:
  - Computes the correlation coefficient using scipy.stats
  - Displays the correlation value to understand the strength and direction of the relationship
  - Uses Pearson's r method for correlation analysis
- **Dependencies**: pandas, scipy.stats

## Usage

Run these scripts from the root directory of the project to perform statistical analysis. The scripts will read data from the `../data/` folder and output results to the console.
