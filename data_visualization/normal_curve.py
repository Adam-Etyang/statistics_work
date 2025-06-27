import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

df = pd.read_excel("data/DATA.xlsx", sheet_name="Sheet1")

# Create bins and labels
bin_edges = list(range(0, 61, 10))
bin_labels = [f"{bin_edges[i]}-{bin_edges[i+1]-1}" for i in range(len(bin_edges)-1)]

# Group Num_Bugs into intervals
df['Bug_interval'] = pd.cut(df['Num_Bugs'], bins=bin_edges, labels=bin_labels, right=False)

# Frequency count per interval
freq_table = df['Bug_interval'].value_counts().sort_index()

# Calculate normal distribution parameters
mean_bugs = df['Num_Bugs'].mean()
std_bugs = df['Num_Bugs'].std()

# Create the plot
plt.figure(figsize=(10, 6))

# Plot histogram using numerical positions for proper alignment
bin_centers = np.array([5, 15, 25, 35, 45, 55])  # Center of each bin
bars = plt.bar(bin_centers, freq_table.values, width=8, color='skyblue', 
               edgecolor='black', alpha=0.7, label='Histogram')

# Create x values for smooth normal curve
x_normal = np.linspace(0, 60, 1000)

# Calculate normal distribution PDF
y_normal = norm.pdf(x_normal, mean_bugs, std_bugs)

# Scale the normal curve to match histogram
# Total area under histogram = total observations
bin_width = 10
total_obs = len(df)
y_normal_scaled = y_normal * total_obs * bin_width

# Plot the normal curve
plt.plot(x_normal, y_normal_scaled, 'r-', linewidth=2, 
         label=f'Normal Curve (μ={mean_bugs:.1f}, σ={std_bugs:.1f})')

# Set x-axis ticks and labels
plt.xticks(bin_centers, bin_labels)

# Labels and title
plt.xlabel('Number of Bugs')
plt.ylabel('Frequency')
plt.title('Histogram of Number of Bugs with Normal Curve Overlay')
plt.legend()
plt.grid(True, alpha=0.3)

# Set reasonable axis limits
plt.xlim(-2, 62)
plt.ylim(0, max(freq_table.values) * 1.1)

plt.tight_layout()
plt.savefig('plots/histogram_of_number_of_bugs_with_normal_curve.png', dpi=300, bbox_inches='tight')
plt.show()