import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.DataFrame({
'scores': [70, 80, 85, 90, 95, 100]
})
# Matplotlib Histogram
plt.hist(df['scores'])
plt.title('Distribution of Scores')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.show()


import numpy as np
data = [1, 2, 3, 4, 5]
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
variance = np.var(data)




import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame
df = pd.DataFrame({
    'age': [25, 30, 35, 40, 45],
    'income': [50000, 60000, 70000, 80000, 90000]
})

# Summary statistics
summary = df.describe()

# Calculate mean age
mean_age = df['age'].mean()

# Calculate income quantiles (25th, 50th, 75th percentiles)
income_quantiles = df['income'].quantile([0.25, 0.5, 0.75])

# Plot the income distribution with quantile lines
plt.figure(figsize=(8, 5))
plt.plot(df['age'], df['income'], marker='o', label='Income by Age')

# Add horizontal lines for income quantiles
plt.axhline(y=income_quantiles[0.25], color='blue', linestyle='--', label='25th Percentile')
plt.axhline(y=income_quantiles[0.5], color='green', linestyle='--', label='Median (50th)')
plt.axhline(y=income_quantiles[0.75], color='orange', linestyle='--', label='75th Percentile')

# Add vertical line for mean age
plt.axvline(x=mean_age, color='red', linestyle=':', label=f'Mean Age ({mean_age})')

# Titles and labels
plt.title('Income vs Age with Mean and Quantiles')
plt.xlabel('Age')
plt.ylabel('Income')
plt.legend()
plt.grid(True)
plt.show()
