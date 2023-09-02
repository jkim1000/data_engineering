import pandas as pd
import numpy as np
import requests


def get_binance_data(ticker:str, interval:str) -> pd.DataFrame:
    url = "https://api.binance.us/api/v3/klines"
    params = {"symbol": ticker, "interval": interval}
    columns = [
        "open_time",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "close_time",
        "qav",
        "num_trades",
        "taker_base_vol",
        "taker_quote_vol",
        "ignore",
    ]

    binance_data = pd.DataFrame(
        requests.get(url, params=params).json(), columns=columns, dtype=np.float64
    )
    binance_data["open_time"] = [
        pd.to_datetime(x, unit="ms").strftime("%Y-%m-%d %H:%M:%S")
        for x in binance_data.open_time
    ]
    binance_data["close_time"] = [
        pd.to_datetime(x, unit="ms").strftime("%Y-%m-%d %H:%M:%S")
        for x in binance_data.close_time
    ]

    return binance_data




if __name__ == "__main__":
    data = get_binance_data("BTCUSDT", "1h")
    print(data)
