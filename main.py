import logging
from analyze_sales import analyze_sales

logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

if __name__=="__main__":
    analyze_sales("data/sales.csv")
