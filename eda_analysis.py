import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/aviation_cleaned.csv")

print("Dataset Shape:")
print(df.shape)

# Basic Statistics
print("\nBasic Statistics:")
print(df.describe())

# Top Airlines
print("\nTop 10 Airlines:")
print(df['MKT_UNIQUE_CARRIER'].value_counts().head(10))

# Top Origin Airports
print("\nTop 10 Origin Airports:")
print(df['ORIGIN'].value_counts().head(10))

# Top Destination Airports
print("\nTop 10 Destination Airports:")
print(df['DEST'].value_counts().head(10))

# Average Departure Delay
print("\nAverage Departure Delay:")
print(df['DEP_DELAY'].mean())

# Average Arrival Delay
print("\nAverage Arrival Delay:")
print(df['ARR_DELAY'].mean())

print("\nMaximum Departure Delay:")
print(df['DEP_DELAY'].max())

print("\nMaximum Arrival Delay:")
print(df['ARR_DELAY'].max())

print("\nMinimum Departure Delay:")
print(df['DEP_DELAY'].min())

print("\nMinimum Arrival Delay:")
print(df['ARR_DELAY'].min())

print("\nDeparture Delay Statistics")
print(df['DEP_DELAY'].describe())

print("\nArrival Delay Statistics")
print(df['ARR_DELAY'].describe())