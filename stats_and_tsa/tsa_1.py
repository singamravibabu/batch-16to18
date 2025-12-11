# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate date range
date_rng = pd.date_range(
	start='2018-01-01', 
	end='2023-12-31', 
	freq='ME'
)

# Simulate sales data with seasonality and noise
np.random.seed(42)
sales = 200 + \
    20 * np.sin(2 * np.pi * date_rng.month / 12) + \
        np.random.normal(0, 5, len(date_rng))

# Create DataFrame
df = pd.DataFrame(
	{
		'Date': date_rng, 
		'Sales': sales
	}
)
df.set_index('Date', inplace=True)

df['Month'] = df.index.month
df['Year'] = df.index.year
plt.figure(figsize=(12, 6))
# sns.lineplot(data=df, x=df.index, y=df['Sales'])
# sns.boxplot(x='Month', y='Sales', data=df)
sns.boxplot(x='Year', y='Sales', data=df)
plt.show()
