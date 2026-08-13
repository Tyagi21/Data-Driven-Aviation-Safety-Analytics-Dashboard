import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Aviation Safety Analytics Dashboard",
    page_icon="✈️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

/* Main background */

.stApp{
    background-color:#0B1727;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background-color:#08111D;
}

/* All text */

html, body, [class*="css"]{
    color:white;
}

/* Titles */

h1{
    color:#00D4FF;
    font-weight:700;
}

h2,h3{
    color:#4FC3F7;
}

/* Divider */

hr{
    border:1px solid #29465B;
}

</style>
""", unsafe_allow_html=True)

df = pd.read_csv("data/aviation_cleaned.csv")

st.sidebar.title("✈ Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Dataset Overview",
        "Airline Analysis",
        "Airport Analysis",
        "Delay Analysis",
        "About"
    ]
)
 #HOME PAGE
if page == "Home":

    st.title("✈ Aviation Safety Analytics Dashboard")

    st.markdown("""
Welcome to the **Data-Driven Flight Operations & Delay Analysis System**.

An interactive dashboard for analyzing airline operations, airport traffic,
and flight delay patterns using aviation operational data.""")

    st.divider()

    st.subheader("Dashboard Overview")

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.metric(
            label="✈ Total Flights",
            value=f"{len(df):,}"
        )

    with col2:
        st.metric(
            label="Airlines",
            value=df['MKT_UNIQUE_CARRIER'].nunique()
        )

    with col3:
        st.metric(
            label="Origin Airports",
            value=df['ORIGIN'].nunique()
        )

    with col4:
        st.metric(
            label="Avg Departure Delay",
            value=f"{df['DEP_DELAY'].mean():.1f} min"
        )

    with col5:
        st.metric(
            label="Avg Arrival Delay",
            value=f"{df['ARR_DELAY'].mean():.1f} min"
        )

    with col6:
        total_airports = len(set(df['ORIGIN']).union(set(df['DEST'])))

        st.metric(
            label="Total Airports",
            value=f"{total_airports:,}"
        )

    st.divider()

    st.info(
        "Use the navigation panel on the left to explore different sections of the dashboard."
    )

# DATASET OVERVIEW
elif page == "Dataset Overview":

    st.title("Dataset Overview")

    st.write("This section provides an overview of the processed aviation dataset.")

    st.write("Dataset Shape:")

    st.write(df.shape)

    st.subheader("First 20 Records")

    st.dataframe(df.head(20))

# AIRLINE ANALYSIS
elif page == "Airline Analysis":

    st.title("✈ Airline Analysis")

    st.markdown("### Airline Performance Overview")

    st.write(
        "This section provides insights into airline operations, flight volume, and average delays."
    )

    st.divider()

    airlines = sorted(df["MKT_UNIQUE_CARRIER"].unique())

    selected_airline = st.selectbox(
        "Select an Airline",
        airlines
    )

    airline_df = df[df["MKT_UNIQUE_CARRIER"] == selected_airline]

    st.subheader(f"📊 {selected_airline}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Flights",
            f"{len(airline_df):,}"
        )

    with col2:
        st.metric(
            "Average Departure Delay",
            f"{airline_df['DEP_DELAY'].mean():.1f} min"
        )

    with col3:
        st.metric(
            "Average Arrival Delay",
            f"{airline_df['ARR_DELAY'].mean():.1f} min"
        )

    st.divider()

    top_airlines = (
        df["MKT_UNIQUE_CARRIER"]
        .value_counts()
        .reset_index()
    )

    top_airlines.columns = ["Airline", "Flights"]

    fig1 = px.bar(
        top_airlines,
        x="Airline",
        y="Flights",
        color="Flights",
        text_auto=True,
        title="Top Airlines by Number of Flights"
    )

    fig1.update_layout(
        xaxis_title="Airline",
        yaxis_title="Number of Flights"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )
    avg_delay = (
        df.groupby("MKT_UNIQUE_CARRIER")["ARR_DELAY"]
        .mean()
        .reset_index()
    )

    avg_delay.columns = ["Airline", "Average Delay"]

    fig2 = px.bar(
        avg_delay,
        x="Airline",
        y="Average Delay",
        color="Average Delay",
        text_auto=".1f",
        title="Average Arrival Delay by Airline"
    )

    fig2.update_layout(
        xaxis_title="Airline",
        yaxis_title="Delay (Minutes)"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.divider()

    st.subheader("Flight Records")

    st.dataframe(airline_df.head(20))

# AIRPORT ANALYSIS
elif page == "Airport Analysis":

    st.title("🛫 Airport Analysis")

    st.markdown("### Airport Operations Analysis")

    st.write(
        "Analyze flight activity across origin and destination airports."
    )

    st.divider()

    airport_info = (
        df[["ORIGIN", "ORIGIN_CITY_NAME", "ORIGIN_STATE_NM"]]
        .drop_duplicates()
        .sort_values("ORIGIN")
    )

    airport_info["Display"] = (
        airport_info["ORIGIN"]
        + " — "
        + airport_info["ORIGIN_CITY_NAME"]
        + ", "
        + airport_info["ORIGIN_STATE_NM"]
    )

    selected_display = st.selectbox(
        "Select Origin Airport",
        airport_info["Display"]
    )

    selected_airport = airport_info.loc[
        airport_info["Display"] == selected_display,
        "ORIGIN"
    ].iloc[0]

    airport_df = df[df["ORIGIN"] == selected_airport]

    city = airport_df["ORIGIN_CITY_NAME"].iloc[0]
    state = airport_df["ORIGIN_STATE_NM"].iloc[0]


    st.subheader(f"🛫 {selected_airport}")

    st.caption(f"{city}, {state}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Flights",
            f"{len(airport_df):,}"
        )

    with col2:
        st.metric(
            "Avg Departure Delay",
            f"{airport_df['DEP_DELAY'].mean():.1f} min"
        )

    with col3:
        st.metric(
            "Avg Arrival Delay",
            f"{airport_df['ARR_DELAY'].mean():.1f} min"
        )

    st.divider()

    top_origin = (
        df["ORIGIN"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    top_origin.columns = ["Airport", "Flights"]

    fig1 = px.bar(
        top_origin,
        x="Airport",
        y="Flights",
        color="Flights",
        text_auto=True,
        title="Top 10 Origin Airports"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    top_dest = (
        df["DEST"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    top_dest.columns = ["Airport", "Flights"]

    fig2 = px.bar(
        top_dest,
        x="Airport",
        y="Flights",
        color="Flights",
        text_auto=True,
        title="Top 10 Destination Airports"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.divider()

    st.subheader(f"Top Destination Cities from {selected_airport}")

    top_destinations = (
        airport_df["DEST_CITY_NAME"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    top_destinations.columns = ["Destination City", "Flights"]

    fig3 = px.bar(
        top_destinations,
        x="Destination City",
        y="Flights",
        color="Flights",
        text_auto=True,
        title=f"Top Destination Cities from {selected_airport}"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.divider()

    st.subheader("Flight Records")

    st.dataframe(
        airport_df[
            [
                "FL_DATE",
                "MKT_UNIQUE_CARRIER",
                "DEST",
                "DEST_CITY_NAME",
                "DEP_DELAY",
                "ARR_DELAY",
                "DISTANCE"
            ]
        ].head(20),
        use_container_width=True
    )

# DELAY ANALYSIS
elif page == "Delay Analysis":

    st.title("⏱ Delay Analysis")

    st.markdown("### Flight Delay Analytics")

    st.write(
        "Analyze flight delays, delay causes, and operational performance."
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Avg Departure Delay",
            f"{df['DEP_DELAY'].mean():.1f} min"
        )

    with col2:
        st.metric(
            "Avg Arrival Delay",
            f"{df['ARR_DELAY'].mean():.1f} min"
        )

    with col3:
        st.metric(
            "Maximum Departure Delay",
            f"{df['DEP_DELAY'].max():.0f} min"
        )

    with col4:
        st.metric(
            "Maximum Arrival Delay",
            f"{df['ARR_DELAY'].max():.0f} min"
        )

    st.divider()

    delay_causes = {
        "Carrier Delay": df["CARRIER_DELAY"].sum(),
        "Weather Delay": df["WEATHER_DELAY"].sum(),
        "NAS Delay": df["NAS_DELAY"].sum(),
        "Security Delay": df["SECURITY_DELAY"].sum(),
        "Late Aircraft Delay": df["LATE_AIRCRAFT_DELAY"].sum()
    }

    delay_df = pd.DataFrame({
        "Delay Type": delay_causes.keys(),
        "Minutes": delay_causes.values()
    })

    fig1 = px.pie(
        delay_df,
        names="Delay Type",
        values="Minutes",
        title="Delay Cause Distribution"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    fig2 = px.bar(
        delay_df,
        x="Delay Type",
        y="Minutes",
        color="Minutes",
        text_auto=True,
        title="Delay Cause Comparison"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.divider()

    st.subheader("Delay Statistics")

    stats = pd.DataFrame({
        "Metric": [
            "Average Departure Delay",
            "Average Arrival Delay",
            "Maximum Departure Delay",
            "Maximum Arrival Delay",
            "Minimum Departure Delay",
            "Minimum Arrival Delay"
        ],
        "Value": [
            round(df["DEP_DELAY"].mean(),2),
            round(df["ARR_DELAY"].mean(),2),
            df["DEP_DELAY"].max(),
            df["ARR_DELAY"].max(),
            df["DEP_DELAY"].min(),
            df["ARR_DELAY"].min()
        ]
    })

    st.dataframe(
        stats,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("Flights with Highest Delays")

    high_delay = df.sort_values(
        by="ARR_DELAY",
        ascending=False
    )

    st.dataframe(

        high_delay[
            [
                "FL_DATE",
                "MKT_UNIQUE_CARRIER",
                "ORIGIN",
                "DEST",
                "DEP_DELAY",
                "ARR_DELAY"
            ]
        ].head(20),

        use_container_width=True
    )

# ABOUT
elif page == "About":

    st.title("ℹ About")

    st.markdown("""
### Project Title

**Data-Driven Aviation Safety Analytics Dashboard using Python**

---

### Description

This dashboard has been developed as part of a Data Science internship project.

The project focuses on:

- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Airline Analysis
- Airport Analysis
- Flight Delay Analysis
- Interactive Dashboard Development

---

### Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Streamlit

---

### Dataset

Processed U.S. Airline On-Time Performance Dataset
""")