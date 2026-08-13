import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/aviation_cleaned.csv")


#1 Top 10 Airlines
top_airlines = df['MKT_UNIQUE_CARRIER'].value_counts().head(10)

plt.figure(figsize=(10,5))
top_airlines.plot(kind='bar')

plt.title("Top 10 Airlines by Number of Flights")
plt.xlabel("Airline")
plt.ylabel("Number of Flights")
plt.tight_layout()
plt.savefig(
    "screenshots/top_airlines.png"
)
plt.show()


#2 Top 10 Origin Airports
top_origin = df['ORIGIN'].value_counts().head(10)

plt.figure(figsize=(10,5))
top_origin.plot(kind='bar')

plt.title("Top 10 Origin Airports")
plt.xlabel("Airport")
plt.ylabel("Number of Flights")
plt.tight_layout()
plt.savefig(
    "screenshots/top_origin_airports.png"
)
plt.show()


#3 Top 10 Destination Airports
top_dest = df['DEST'].value_counts().head(10)

plt.figure(figsize=(10,5))
top_dest.plot(kind='bar')

plt.title("Top 10 Destination Airports")
plt.xlabel("Airport")
plt.ylabel("Number of Flights")

plt.tight_layout()

plt.savefig(
    "screenshots/top_destination_airports.png"
)

plt.show()


#4 Average Arrival Delay by Airline
airline_delay = (
    df.groupby('MKT_UNIQUE_CARRIER')['ARR_DELAY']
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,5))
airline_delay.plot(kind='bar')
plt.title("Average Arrival Delay by Airline")
plt.xlabel("Airline")
plt.ylabel("Average Delay (Minutes)")
plt.tight_layout()
plt.savefig(
    "screenshots/airline_delay_analysis.png"
)
plt.show()


#5 Delay Cause Analysis
delay_causes = {
    'Carrier Delay': df['CARRIER_DELAY'].sum(),
    'Weather Delay': df['WEATHER_DELAY'].sum(),
    'NAS Delay': df['NAS_DELAY'].sum(),
    'Security Delay': df['SECURITY_DELAY'].sum(),
    'Late Aircraft Delay': df['LATE_AIRCRAFT_DELAY'].sum()
}
plt.figure(figsize=(8,8))
plt.pie(
    delay_causes.values(),
    labels=delay_causes.keys(),
    autopct='%1.1f%%'
)
plt.title("Flight Delay Causes Distribution")
plt.tight_layout()
plt.savefig(
    "screenshots/delay_cause_analysis.png"
)
plt.show()