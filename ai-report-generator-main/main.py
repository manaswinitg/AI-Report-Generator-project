from src.data_pipeline.ecommerce_loader import load_ecommerce_data
from src.data_pipeline.stock_loader import fetch_stock_data

def main():
    print("🚀 Starting AI Report Generator (Day 1 Setup)...\n")

    # Load e-commerce data
    ecommerce_df = load_ecommerce_data("data/raw/ecommerce_sales.csv")

    # Fetch stock data
    stock_df = fetch_stock_data("AAPL")

    print("\n✅ Data ingestion pipeline is working successfully!")

if __name__ == "__main__":
    main()
