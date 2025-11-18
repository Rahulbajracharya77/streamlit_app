import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read and merge files (use on common column)
df = pd.read_csv(r"C:\Users\Ripple\Desktop\data science\Sample Data File\2022-01-02.csv")
df["Date"] = pd.to_datetime(df["S.No"])   # example only


# For UI dropdown, use unique symbols from merged df
unique_companies = df["Symbol"].unique()

user_file = st.file_uploader("Choose a file")

if user_file:
    df = pd.read_csv(user_file)

    selected_symbol = st.selectbox(
        "Choose Company you want to analyze",
        unique_companies
    )

    # Filter data based on selected company
    filtered_df = df[df["Symbol"] == selected_symbol]

    col1, col2 = st.columns(2)

    # PRICE TREND
    col1.subheader(f"Price Trend of {selected_symbol}")
    col1.line_chart(data=filtered_df, x="S.No", y="Close")

    # SCATTER
    col2.subheader(f"Close vs Open Scatter Plot for {selected_symbol}")
    col2.scatter_chart(data=filtered_df, x="Close", y="Open")

    # OPTIONAL: Matplotlib scatter
    fig, ax = plt.subplots()
    ax.scatter(filtered_df["Close"], filtered_df["Open"])
    ax.set_xlabel("Close")
    ax.set_ylabel("Open")
    ax.set_title(f"Close vs Open - {selected_symbol}")
    st.pyplot(fig)
