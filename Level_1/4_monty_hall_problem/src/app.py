import streamlit as st
from src.monty_hall import simulate_game

st.title(":mag: Monte Hall Problem Simulation")

num_games = st.number_input(
    "Enter the number of simulations:",
    min_value=100,
    value=100000,
    step=100,
    format="%d",
)

col1, col2 = st.columns(2)

# Create subheaders
col1.subheader = 'Win percentage if the player does not switch the doors:'
col2.subheader = 'Win percentage if the player switches the doors:'

# Create charts
chart1 = col1.line_chart(x=None, y=None, height=400)
chart2 = col2.line_chart(x=None, y=None, height=400)

with col1:
    pass

with col2:
    pass