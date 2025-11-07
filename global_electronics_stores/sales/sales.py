import pandas as pd
import matplotlib.pyplot as plt

def  analyze_sales():
    file_path = './data/Sales.csv' 
    sales_data = pd.read_csv(file_path)

    sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'])
    sales_data['YearMonth'] = sales_data['Order Date'].dt.to_period('M')

    monthly_sales = sales_data.groupby('YearMonth')['Quantity'].sum().reset_index()
    monthly_sales['YearMonth'] = monthly_sales['YearMonth'].astype(str)


    plt.figure(figsize=(12, 6))
    plt.plot(monthly_sales['YearMonth'], monthly_sales['Quantity'], marker='o', linestyle='-')
    plt.title('Monthly Sales Quantity', fontsize=14)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Quantity Sold', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()




