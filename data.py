import yfinance as yf
import pandas as pd
import numpy as np
import datetime as datetime

#setting risk limits
max_exposure = 100000
max_daily_loss = -2000
max_drawdown = 0.05

#futures instruments

instruments = {
    "ES" : "ES=F",
    "NQ" : "NQ=F",
    "CL" : "CL=F"
}

# creating synthetic positions

positions = {
    "ES" : {
        "qty" : 2,
        "entry_price" :5900
    },
    "NQ" : {
        "qty" : -1,
        "entry_price" : 21000
    },
    "CL" : {
        "qty" : 3,
        "entry_price" : 70
    }
}

# current portfolio state
portfolio_peak_value = 0

#getting futures data

def get_prices():

    prices = {}

    for symbol, ticker in instruments.items():

        data = yf.Ticker(ticker)

        hist = data.history(period = "1d", interval = "1m")

        latest_price = hist["Close"].iloc[-1]

        prices[symbol] = round(latest_price, 2)

    return prices    


# pnl

def calculate_pnl(prices):

    pnl_data = {}
    total_pnl = 0

    for symbol, position in positions.items():
        qty = position["qty"]
        entry = position["entry_price"]
        current = prices[symbol]

        pnl = (current - entry)*qty

        pnl_data[symbol] = round(pnl, 2)

        total_pnl += pnl

    return pnl_data , round(total_pnl,2)



# exposure

def calculate_exposure(prices):

    exposure_data = {}

    net_exposure = 0
    gross_exposure = 0

    for symbol, position in positions.items():

        qty = position["qty"]

        current_prices = prices[symbol]

        exposure = qty * current_prices

        exposure_data[symbol] = round(exposure, 2)

        gross_exposure += abs(exposure)

        net_exposure += exposure

        return (exposure_data, round(gross_exposure,2), round(net_exposure, 2))
    

#drawdown

def calculate_drawdown(current_portfolio_value):

    global portfolio_peak_value

    if current_portfolio_value > portfolio_peak_value:
        portfolio_peak_value = current_portfolio_value

    if portfolio_peak_value == 0:
        return 0
    
    drawdown = (
        (portfolio_peak_value - current_portfolio_value)/ portfolio_peak_value
    )

    return round(drawdown, 4)


# risk management 

def risk_checks(gross_exposure, total_pnl, drawdown):

    alerts = []

    if gross_exposure > max_exposure:

        alerts.append(
            "CRITICAL: Gross exposure limit breached"
        )

    if total_pnl < max_daily_loss:

        alerts.append(
            "CRITICAL: Daily loss limit breached"
        )
    if drawdown > max_drawdown:

        alerts.append(
            "WARNING : Drawdown threshold breached"
        )

    return alerts


def get_portfolio():

    prices = get_prices()

    pnl_data, total_pnl = calculate_pnl(prices)

    (exposure_data, gross_exposure, net_exposure) = calculate_exposure(prices)

    portfolio_value = 100000 + total_pnl

    drawdown = calculate_drawdown(
        portfolio_value
    )

    alerts = risk_checks(
        gross_exposure,
        total_pnl,
        drawdown
    )


    final_data = {
        "timestamp": datetime.datetime.now(),

        "prices": prices,

        "positions": positions,

        "pnl_data": pnl_data,

        "total_pnl": total_pnl,

        "exposure_data": exposure_data,

        "gross_exposure": gross_exposure,

        "net_exposure": net_exposure,

        "drawdown": drawdown,

        "alerts": alerts
    }
    return final_data


if __name__ == "__main__":

    finalD = get_portfolio()

    print(finalD)    
