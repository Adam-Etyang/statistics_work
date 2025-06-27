import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load Excel data
df = pd.read_excel("DATA.xlsx")

# Set style
sns.set(style="whitegrid")

# Plot histogram with KDE (smoothed curve)
plt.figure(figsize=(10, 6))
sns.histplot(df['Num_Bugs'], bins=range(0, 70, 10), kde=True, color='skyblue', edgecolor='black')

# Labeling
plt.xlabel("Number of Bugs")
plt.ylabel("Frequency")
plt.title("Histogram of Number of Bugs with KDE Curve")
plt.xticks(range(0, 70, 10))
plt.grid(True)

# Save and show
plt.tight_layout()
plt.savefig("bug_histogram_with_kde.png", dpi=300)
plt.show()
