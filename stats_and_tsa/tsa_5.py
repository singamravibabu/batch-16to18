# HIGHLIGHTING THE TREND

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

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

# Let’s apply a 12-month rolling window (1-year smoothing).

df['SMA_3'] = df['Sales'].rolling(window=3).mean()
df['SMA_6'] = df['Sales'].rolling(window=6).mean()
df['SMA_12'] = df['Sales'].rolling(window=12).mean()


plt.figure(figsize=(12, 6))

sns.lineplot(x=df.index, y='Sales', data=df,
	label='Original', alpha=0.7)
sns.lineplot(x=df.index, y='SMA_12', data=df,
	label='12-Month SMA', color='red')
sns.lineplot(x=df.index, y='SMA_3', data=df,
	label='3-Month SMA')
sns.lineplot(x=df.index, y='SMA_6', data=df, 
	label='6-Month SMA')

plt.show()