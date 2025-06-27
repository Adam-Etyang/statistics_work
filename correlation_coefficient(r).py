from tkinter import W
import pandas as pd
from scipy.stats import pearsonr 


#load data from the xlsx file
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

#calculate the correlation coefficient
correlation, _ = pearsonr(df['Hours_Coding'], df['Num_Bugs'])

#print the correlation coefficient
print(f"The correlation coefficient is: {correlation}")