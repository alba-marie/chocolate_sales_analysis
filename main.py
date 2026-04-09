import pandas as pd
from src.load import load_data

def main():
    df = load_data('data/sales.csv')
    print(df.head())
if __name__ == "__main__":
    main()