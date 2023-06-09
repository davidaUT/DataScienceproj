import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# Simple Stock Price App

Shown are the stock clock price and volume of Google!

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period = '1d', start = '2010-5-31', end = '2020-5-31')

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)