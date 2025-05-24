import pandas as pd

import streamlit as st

"""
Author: Majid
"""

# Test a table
df = pd.DataFrame({
    "Name": ["John", "Jane", "Doe"],
    "Age": [28, 34, 29],
    "City": ["New York", "Los Angeles", "Chicago"]
})
df

col1, col2, col3 = st.columns(3)

with col1:
    # Test a slider
    my_num = st.slider("Select a number", 0, 100, 50, step=5)

    # Test a selectbox
    my_option = st.selectbox("Options", ["Use numbers", "Use Special characters"])

with col2:
    # Test a radiobutton
    my_radio = col2.radio("Select an option", ["Use numbers", "Use Special characters"])

    # Test a multiselect
    selected_options = col2.multiselect(
        "Select one or more options",
        ["Use numbers", "Use Special characters"]
    )

with col3:
    # Test multiple checkboxes
    use_numbers = col3.checkbox("Use numbers")
    use_special_characters = col3.checkbox("Use special characters")