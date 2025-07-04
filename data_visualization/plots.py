import pandas as pd
import matplotlib.pyplot as plt

# load the data from the xlsx file
df = pd.read_excel("../data/DATA.xlsx", sheet_name="Sheet1")

# create the scatter plot using the data
plt.scatter(df["Hours_Coding"], df["Num_Bugs"], color="purple", marker="o")

# add title and labels
plt.title("Hours Coding vs Number of Bugs")
plt.xlabel("Hours Coding")
plt.ylabel("Number of Bugs")
plt.grid(True)
# show the plot
plt.savefig("../plots/my_scatter_plot.png", dpi=300, bbox_inches="tight")
plt.show()

