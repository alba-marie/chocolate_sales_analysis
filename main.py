import pandas as pd
from src.load import load_data

def main():
    sales = load_data('data/sales.csv')
    stores = load_data('data/stores.csv')
    products = load_data('data/products.csv')
    customers = load_data('data/customers.csv')
    calender = load_data('data/calendar.csv')

    

if __name__ == "__main__":
    main()