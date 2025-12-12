# HIGHLIGHTING THE TREND

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

# upward trend
trend = np.linspace(100, 300, len(date_rng))

# yearly seasonality
seasonality = 30 * np.sin(2 * np.pi * date_rng.month / 12)

# random noise
noise = np.random.normal(0, 8, len(date_rng))

# Combined components
sales = trend + seasonality + noise

# Create DataFrame
df = pd.DataFrame(
	{
		'Date': date_rng, 
		'Sales': sales
	}
)
df.set_index('Date', inplace=True)

# Creating a month column
df['Month'] = df.index.month
monthly_avg = df.groupby('Month')['Sales'].mean()

# Creating a year column
df['Year'] = df.index.year
yearly_avg = df.groupby('Year')['Sales'].mean()

# Calculate the rolling mean
df['RollingMean'] = df['Sales'].rolling(window=12, center=True).mean()


# print(df.head(20))

plt.figure(figsize=(12, 6))
# sns.lineplot(x=date_rng, y=trend)
# sns.lineplot(x=date_rng, y=seasonality)
# sns.lineplot(x=date_rng, y=noise)
# sns.lineplot(x=date_rng, y=sales)
# sns.lineplot(data=df, x=df.index, y=df['Sales'])
# sns.lineplot(data=df, x=df.index, y=df['RollingMean'])
'''
sns.lineplot(
	x=monthly_avg.index, 
	y=monthly_avg.values,
    marker='s',
    markersize=10
)
'''
sns.lineplot(
    x=yearly_avg.index, 
    y=yearly_avg.values,
    marker='o',
    markersize=10
)
plt.show()