import yfinance as yf
from pathlib import Path

def fetch_stock_data(ticker: str, period="6mo", interval="1d"):
    """Fetches stock price history for a given ticker symbol."""
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)

    # Save to raw data folder
    output_path = Path(f"data/raw/{ticker}_stock.csv")
    df.to_csv(output_path)

    print(f"✅ Saved {ticker} data to {output_path}")
    print(df.head())
    return df


if __name__ == "__main__":
    fetch_stock_data("AAPL")
