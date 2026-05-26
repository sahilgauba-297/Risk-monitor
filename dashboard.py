import streamlit as st
import pandas as pd

from data import get_portfolio

#title
st.title("Futures Risk Monitor")


portfolio = get_portfolio()


col1, col2, col3 = st.columns(3)

col1.metric(
    "Total PnL",
    f"${portfolio['total_pnl']}"
)

col2.metric(
    "Gross Exposure",
    f"${portfolio['gross_exposure']}"
)

col3.metric(
    "Drawdown",
    f"{portfolio['drawdown'] * 100:.2f}%"
)

st.divider()


table_data = []

for symbol, position in portfolio["positions"].items():

    row = {

        "Symbol": symbol,

        "Quantity": position["qty"],

        "Entry Price": position["entry_price"],

        "Current Price": portfolio["prices"][symbol],

        "PnL": portfolio["pnl_data"][symbol]
    }

    table_data.append(row)

df = pd.DataFrame(table_data)

st.subheader("Portfolio Positions")

st.dataframe(df)

st.divider()



# alert
st.subheader("Risk Alerts")

if portfolio["alerts"]:

    for alert in portfolio["alerts"]:

        st.error(alert)

else:

    st.success("No active risk breaches")



st.caption(
    f"Last Updated: {portfolio['timestamp']}"
)


