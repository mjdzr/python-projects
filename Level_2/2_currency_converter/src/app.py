import streamlit as st
from currency_conventor import currency_list, get_exchange_rate, currency_converter

st.title(':dollar: Currency Convertor!!')

st.markdown("""
This tool allows the user to convert amounts between different currencies. 

I know! Google does the same thing :)
            """)

# base currency
base_amount = st.number_input('Enter a value to be converted', 
                              min_value=0.0,
                              max_value=1e15,
                              value = 1.0)
base_currency = st.selectbox('Convert from:', currency_list())
target_currency = st.selectbox('To:', currency_list())

# Convert
if base_amount > 0 and base_currency and target_currency:
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    target_amount = currency_converter(base_amount, exchange_rate)
    if exchange_rate:
        st.success(f'1 {base_currency} = {exchange_rate:.4f} {target_currency}')
        col1, col2, col3 = st.columns(3)
        col1.metric(label='Base:', value=f'{base_amount:.2f} {base_currency}')
        col2.markdown("<h1 style='text-align: center; margin: 0;'>&#8594;</h1>", unsafe_allow_html=True)
        col3.metric(label='Target:', value=f'{target_amount:.2f} {target_currency}')
    else:
        st.error('Error fetching exchange rate information')