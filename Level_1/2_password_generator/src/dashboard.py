import streamlit as st

from src.password_generator import (MemorablePasswordGenerator, PasswordGenerator, PinGenerator,
                  RandomPasswordGenerator)

st.set_page_config(layout="wide")
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("./images/banner.jpg")

with col3:
    st.write(' ')

st.markdown("<h1 style='text-align: center; color: darkblue;'>Password Generator</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    # Random Password Generator
    st.subheader("Random Password Generator")
    length = st.slider("Password Length:", min_value=4, max_value=64, value=16)
    include_numbers = st.checkbox("Include Numbers", value=True)
    include_symbols = st.checkbox("Include Symbols", value=True)

    if st.button("Generate Password", key="random_key"):
        random_password_generator = RandomPasswordGenerator(length, include_numbers, include_symbols)
        password = random_password_generator.generate()
        st.write("Password:")
        st.code(password, language="text")

with col2:
    # Memorable Password Generator
    st.subheader("Memorable Password Generator")
    num_of_words = st.slider("Number of Words:", min_value=1, max_value=10, value=4)
    seperator = st.text_input("Separator:", max_chars=1, value="-")
    capitalize = st.checkbox("Capitalize Words", value=False)
    min_word_size, max_word_size = st.slider("Minimum Word Size:",
                                             min_value=3,
                                             max_value=10,
                                             value=(3, 4)
    )

    if st.button("Generate Password", key="memorable_key"):
        memorable_password_generator = MemorablePasswordGenerator(num_of_words, seperator, capitalize, min_word_size, max_word_size)
        password = memorable_password_generator.generate()
        st.write("Password:")
        st.code(password, language="text")

with col3:
    # PIN Generator
    st.subheader("PIN Generator")
    pin_length = st.slider("PIN Length:", min_value=4, max_value=32, value=4)

    if st.button("Generate PIN", key = "pin_key"):
        pin_generator = PinGenerator(pin_length)
        pin = pin_generator.generate()
        st.code(pin, language="text")

