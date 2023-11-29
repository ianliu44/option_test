import streamlit as st
import yfinance as yf
import pandas as pd
# Create a text input box and assign its value to a variable

ticker1 = yf.Ticker("USDJPY=X")
ticker2=yf.Ticker('HKDUSD=X')


test=ticker1.info
test2=ticker2.info



h=ticker1.info['ask']*ticker2.info['ask']

h=1/h

h=h*1000

payoff=(h-52.276)*3627

profit=payoff-2800

payoff=round(payoff)

profit=round(profit)

st.write(f'The current payoff is {payoff}HKD')

st.write(f'The current profit is {profit}HKD')
