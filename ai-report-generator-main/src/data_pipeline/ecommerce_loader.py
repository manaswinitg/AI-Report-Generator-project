import pandas as pd
from pathlib import Path

def load_ecommerce_data(file_path: str) -> pd.DataFrame:
    """Loads and previews raw e-commerce sales data."""
    df = pd.read_csv(file_path)
    print(f"✅ Loaded {len(df)} records from {file_path}")
    print(df.head())
    return df


if __name__ == "__main__":
    raw_path = Path("data/raw/ecommerce_sales.csv")
    load_ecommerce_data(raw_path)
