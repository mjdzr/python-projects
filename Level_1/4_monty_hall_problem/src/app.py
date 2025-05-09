import time

import streamlit as st

from src.monty_hall import simulate_game

# Title and banner
st.set_page_config(layout="centered")
st.image("https://brilliant-staff-media.s3-us-west-2.amazonaws.com/tiffany-wang/gWotbuEdYC.png", use_container_width=True)
st.title(":mag: Monte Hall Problem Simulation")

num_games = st.number_input(
    "Enter the number of simulations:",
    min_value=10,
    max_value=10000,
    value=100,
    step=10,
    format="%d",
)

col1, col2 = st.columns(2)

# Create subheaders
col1.subheader('Win percentage if the player does not switch the doors:')
col2.subheader('Win percentage if the player switches the doors:')

# Create charts
chart1 = col1.line_chart(x=None, y=None, height=400)
chart2 = col2.line_chart(x=None, y=None, height=400)

# Simulate the game based on the numbers the user has provided:
num_wins_with_switch = 0
num_wins_without_switch = 0

for i in range(num_games):
    # Run a single simulation and add the results to the chart
    wins_with_switch, wins_without_switch = simulate_game(1, 'count')
    num_wins_with_switch += wins_with_switch
    num_wins_without_switch += wins_without_switch

    # Add to charts
    chart1.add_rows([num_wins_without_switch / (i + 1)])
    chart2.add_rows([num_wins_with_switch / (i + 1)])

    # Delay drawing the next line
    time.sleep(0.001)
