import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="IPL 2020 Dashboard",
    page_icon="🏏",
    layout="wide"
)

sns.set_style("whitegrid")

@st.cache_data
def load_data():
    df = pd.read_csv("ipl.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[df['Date'].dt.year == 2020]
    return df

df = load_data()

all_teams = set()

for match in df['Teams']:
    teams = match.split(" vs ")
    all_teams.update(teams)

st.title("🏏 IPL 2020 Dashboard")
st.write("Complete IPL 2020 Analysis")

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Matches", df.shape[0])

with col2:
    st.metric("Teams", len(all_teams))

with col3:
    st.metric("Highest Score", int(df['First_Innings_Score'].max()))

with col4:
    st.metric("Venues", df['Venue'].nunique())

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("🏆 Team Wins")

    team_wins = df['Match_Winner'].value_counts()

    fig1, ax1 = plt.subplots(figsize=(7,5))

    sns.barplot(
        x=team_wins.values,
        y=team_wins.index,
        palette="viridis",
        ax=ax1
    )

    ax1.set_xlabel("Wins")
    ax1.set_ylabel("Teams")

    st.pyplot(fig1)

with col2:

    st.subheader("🪙 Toss Decisions")

    toss = df['Toss_Decision'].value_counts()

    fig2, ax2 = plt.subplots(figsize=(6,5))

    ax2.pie(
        toss.values,
        labels=toss.index,
        autopct='%1.1f%%',
        startangle=90
    )

    st.pyplot(fig2)

col3, col4 = st.columns(2)

with col3:

    st.subheader("⭐ Top Players")

    pom = df['Player_of_Match'].value_counts().head(10)

    fig3, ax3 = plt.subplots(figsize=(7,5))

    sns.barplot(
        x=pom.index,
        y=pom.values,
        palette="magma",
        ax=ax3
    )

    plt.xticks(rotation=45)

    ax3.set_xlabel("Players")
    ax3.set_ylabel("Awards")

    st.pyplot(fig3)

with col4:

    st.subheader("📈 Score Distribution")

    fig4, ax4 = plt.subplots(figsize=(7,5))

    sns.histplot(
        df['First_Innings_Score'],
        bins=20,
        kde=True,
        color='skyblue',
        ax=ax4
    )

    ax4.set_xlabel("Runs")
    ax4.set_ylabel("Frequency")

    st.pyplot(fig4)

col5, col6 = st.columns(2)

with col5:

    st.subheader("🏟️ Top Venues")

    venues = df['Venue'].value_counts().head(5)

    fig5, ax5 = plt.subplots(figsize=(6,6))

    ax5.pie(
        venues.values,
        labels=venues.index,
        autopct='%1.1f%%',
        wedgeprops=dict(width=0.4),
        startangle=90
    )

    st.pyplot(fig5)

with col6:

    st.subheader("🔥 Win Type Analysis")

    fig6, ax6 = plt.subplots(figsize=(7,5))

    sns.countplot(
        x='Win_Type',
        data=df,
        palette='coolwarm',
        ax=ax6
    )

    ax6.set_xlabel("Win Type")
    ax6.set_ylabel("Count")

    st.pyplot(fig6)

st.divider()

st.subheader("📄 IPL 2020 Dataset")

st.dataframe(df)