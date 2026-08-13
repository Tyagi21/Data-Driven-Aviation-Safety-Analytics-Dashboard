import pandas as pd

# Load dataset
df = pd.read_csv("data/T_ONTIME_MARKETING.csv")

print("Original Shape:")
print(df.shape)

# Select useful columns
selected_columns = [
    'YEAR',
    'MONTH',
    'FL_DATE',
    'MKT_UNIQUE_CARRIER',

    'ORIGIN',
    'ORIGIN_CITY_NAME',
    'ORIGIN_STATE_NM',

    'DEST',
    'DEST_CITY_NAME',
    'DEST_STATE_NM',

    'DEP_DELAY',
    'ARR_DELAY',

    'CANCELLED',
    'DIVERTED',

    'AIR_TIME',
    'DISTANCE',

    'WEATHER_DELAY',
    'CARRIER_DELAY',
    'NAS_DELAY',
    'SECURITY_DELAY',
    'LATE_AIRCRAFT_DELAY'
]

df = df[selected_columns]

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Remove extreme delay outliers
df = df[
    (df['DEP_DELAY'] <= 300) &
    (df['ARR_DELAY'] <= 300)
]
print("\nCleaned Shape:")
print(df.shape)

# Airline Mapping
airline_mapping = {
    'AA': 'American Airlines',
    'UA': 'United Airlines',
    'WN': 'Southwest Airlines',
    'DL': 'Delta Air Lines',
    'AS': 'Alaska Airlines',
    'B6': 'JetBlue Airways',
    'F9': 'Frontier Airlines',
    'NK': 'Spirit Airlines',
    'G4': 'Allegiant Air',
    'HA': 'Hawaiian Airlines'
}

df['MKT_UNIQUE_CARRIER'] = (
    df['MKT_UNIQUE_CARRIER']
    .replace(airline_mapping)
)
# Save cleaned dataset
df.to_csv("data/aviation_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")