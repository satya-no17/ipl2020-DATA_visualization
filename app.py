import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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

# ---------------------------------
# KPI SECTION
# ---------------------------------

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

# =================================
# 2 x 3 PLOTS LAYOUT
# =================================

# ---------------------------------
# ROW 1
# ---------------------------------

col1, col2 = st.columns(2)

# ===== PLOT 1 =====

with col1:

    st.subheader("🏆 Team Wins")

    team_wins = df['Match_Winner'].value_counts()

    fig1, ax1 = plt.subplots(figsize=(7,5))

    sns.barplot(
        x=team_wins.values,
        y=team_wins.index,
        ax=ax1
    )

    ax1.set_xlabel("Wins")
    ax1.set_ylabel("Teams")

    st.pyplot(fig1)

# ===== PLOT 2 =====

with col2:

    st.subheader("🪙 Toss Decisions")

    toss = df['Toss_Decision'].value_counts()

    fig2, ax2 = plt.subplots(figsize=(6,5))

    ax2.pie(
        toss.values,
        labels=toss.index,
        autopct='%1.1f%%'
    )

    st.pyplot(fig2)

# ---------------------------------
# ROW 2
# ---------------------------------

col3, col4 = st.columns(2)

# ===== PLOT 3 =====

with col3:

    st.subheader("⭐ Top Players")

    pom = df['Player_of_Match'].value_counts().head(10)

    fig3, ax3 = plt.subplots(figsize=(7,5))

    sns.barplot(
        x=pom.values,
        y=pom.index,
        ax=ax3
    )

    ax3.set_xlabel("Awards")
    ax3.set_ylabel("Players")

    st.pyplot(fig3)

# ===== PLOT 4 =====

with col4:

    st.subheader("📈 Score Distribution")

    fig4, ax4 = plt.subplots(figsize=(7,5))

    sns.histplot(
        df['First_Innings_Score'],
        bins=20,
        kde=True,
        ax=ax4
    )

    ax4.set_xlabel("Runs")

    st.pyplot(fig4)

# ---------------------------------
# ROW 3
# ---------------------------------

col5, col6 = st.columns(2)

# ===== PLOT 5 =====

with col5:

    st.subheader("🏟️ Top Venues")

    venues = df['Venue'].value_counts().head(10)

    fig5, ax5 = plt.subplots(figsize=(7,5))

    sns.barplot(
        x=venues.values,
        y=venues.index,
        ax=ax5
    )

    ax5.set_xlabel("Matches")

    st.pyplot(fig5)

# ===== PLOT 6 =====

with col6:

    st.subheader("🔥 Win Type Analysis")

    win_type = df['Win_Type'].value_counts()

    fig6, ax6 = plt.subplots(figsize=(7,5))

    sns.barplot(
        x=win_type.index,
        y=win_type.values,
        ax=ax6
    )

    ax6.set_xlabel("Win Type")
    ax6.set_ylabel("Count")

    st.pyplot(fig6)

# ---------------------------------
# DATASET
# ---------------------------------

st.divider()

st.subheader("📄 IPL 2020 Dataset")

st.dataframe(df)