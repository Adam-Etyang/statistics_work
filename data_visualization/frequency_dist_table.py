from cProfile import label
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("data/DATA.xlsx", sheet_name="Sheet1")

#create bins and labels
bin_edges = list(range(0,61,10))
bin_labels = [f"{bin_edges[i]}-{bin_edges[i+1]-1}" for i in range(len(bin_edges)-1)]

#Group Num_Bugs into intervals
df['Bug_interval'] = pd.cut(df['Num_Bugs'],bins = bin_edges,labels = bin_labels,right = False)

#frequency count per interval
freq_table = df['Bug_interval'].value_counts().sort_index()

#plot histogram
plt.figure(figsize=(10,6))
plt.bar(freq_table.index.astype(str),freq_table.values,color='skyblue',edgecolor='black')

#labels and title
plt.xlabel('Number of Bugs')
plt.ylabel('Frequency')
plt.title('Histogram of Number of Bugs')

plt.savefig('plots/histogram_of_number_of_bugs.png',dpi=300,bbox_inches='tight')
plt.show()