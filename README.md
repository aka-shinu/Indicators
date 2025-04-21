# 📈 Indicators

A lightweight Python library built with **Pandas** and **NumPy** to calculate popular **technical trading indicators** such as RSI, SMA, EMA, and more. Perfect for quantitative trading, backtesting, or data analysis workflows.

---

## 🚀 Features

- ✅ Built on top of **Pandas** and **NumPy**
- ✅ Easy integration into trading pipelines
- ✅ Clean, modular structure for extensibility
- ✅ Supports series-based input (Pandas Series or NumPy arrays)

---

## 📦 Installation

```bash
git clone https://github.com/aka-shinu/Indicators.git
cd Indicators
pip install -r requirements.txt
Requirements: pandas, numpy
```
🧮 Available Indicators
RSI (Relative Strength Index)

SMA (Simple Moving Average)

EMA (Exponential Moving Average)

(More indicators coming soon)

🧑‍💻 Example Usage
python
Copy
Edit
import pandas as pd
from indicators import rsi, sma, ema

# Example: Pandas Series of closing prices
prices = pd.Series([100, 102, 101, 105, 110, 108, 111])

# Calculate RSI with a 14-period window
rsi_series = rsi(prices, period=14)

# Calculate SMA
sma_series = sma(prices, period=10)

# Calculate EMA
ema_series = ema(prices, period=10)

print("RSI:", rsi_series)
📁 Project Structure
bash
Copy
Edit
Indicators/
├── indicators/
│   ├── __init__.py
│   ├── rsi.py
│   ├── sma.py
│   ├── ema.py
│   └── utils.py
├── tests/
│   └── test_rsi.py
├── requirements.txt
└── README.md
✅ TODO
 Add Bollinger Bands

 Add MACD & ATR

 Write full unit tests

 Add Jupyter Notebook demo

 Package for PyPI

🤝 Contributing
Found a bug? Want to add a new indicator? Open a PR or issue — contributions are always welcome!

📜 License
This project is licensed under the MIT License — see the LICENSE file for details.
