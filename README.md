# Futures Risk Monitor

A real time futures risk monitoring system designed to simulate a simplified trading desk risk workflow.

The system monitors live futures market data, tracks portfolio-level risk metrics, calculates real-time PnL and exposure, and generates alerts when predefined risk thresholds are breached.

---

# Features

- Live futures market data using Yahoo Finance
- Real-time portfolio PnL tracking
- Gross and net exposure monitoring
- Portfolio drawdown calculations
- Automated risk threshold alerts
- Streamlit dashboard
- Multi-instrument futures monitoring

---

# Instruments Monitored

| Instrument | Description |
|---|---|
| ES | E-mini S&P 500 Futures |
| NQ | E-mini Nasdaq Futures |
| CL | Crude Oil Futures |

---

# System Architecture

```text
Market Data Feed
        ↓
Portfolio Positions
        ↓
PnL Engine
        ↓
Exposure Engine
        ↓
Drawdown Engine
        ↓
Risk Checks + Alerts
        ↓
Live Dashboard
```

---

# Core Components

## Market Data Engine
Pulls live futures prices using Yahoo Finance via `yfinance`.

## PnL Engine
Calculates unrealized profit and loss for each portfolio position.

Formula:

PnL = (Current Price - Entry Price) × Quantity

## Exposure Engine
Tracks:
- Gross Exposure
- Net Exposure
- Instrument-level exposure

## Drawdown Engine
Monitors peak-to-trough portfolio decline.

## Risk Engine
Checks portfolio against:
- Exposure limits
- Daily loss thresholds
- Drawdown thresholds

## Dashboard
Interactive monitoring interface built using Streamlit.

---

# Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- yfinance

---

# Running the Dashboard

Start the Streamlit dashboard:

```bash
streamlit run dashboard.py
```

---

# Example Risk Metrics

The system monitors:
- Total Portfolio PnL
- Gross Exposure
- Net Exposure
- Portfolio Drawdown
- Active Risk Alerts

---

# Future Improvements

Potential future enhancements include:
- Real-time websocket market feeds
- Historical PnL tracking
- Value at Risk (VaR)
- Volatility monitoring
- Trade blotter integration
- Order book simulation
- PostgreSQL storage
- Slack/email alerting
- Docker deployment

---
