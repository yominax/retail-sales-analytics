import pandas as pd
import logging

logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

def analyze_sales(csv_path):
    df=pd.read_csv(csv_path)
    df['Total']=df['Quantity']*df['UnitPrice']
    logging.info(f"rows: {len(df)} total revenue: {df['Total'].sum():,.2f}")
    cat=df.groupby('Category')['Total'].sum().sort_values(ascending=False)
    top=df.groupby('Product')['Total'].sum().sort_values(ascending=False).head(5)
    out=df.groupby('Month')['Total'].sum()
    cat.to_csv('output/sales_by_category.csv')
    top.to_csv('output/top_products.csv')
    out.to_csv('output/monthly_sales.csv')
    logging.info("analysis done, results saved.")
