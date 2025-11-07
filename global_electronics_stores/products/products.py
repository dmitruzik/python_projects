import pandas as pd
import matplotlib.pyplot as plt

def analyze_products():
    file_path = './data/Sales.csv' 
    products_data = pd.read_csv(file_path)
    products_data['Unit Cost USD'] = products_data['Unit Cost USD'].replace('[\$,]', '', regex=True).astype(float)
    products_data['Unit Price USD'] = products_data['Unit Price USD'].replace('[\$,]', '', regex=True).astype(float)

    # Unit Cost Analysis
    max_cost = products_data['Unit Cost USD'].max()
    sum_cost = products_data['Unit Cost USD'].sum()
    avg_cost = products_data['Unit Cost USD'].mean()

    # Unit Price Analysis
    max_price = products_data['Unit Price USD'].max()
    sum_price = products_data['Unit Price USD'].sum()
    avg_price = products_data['Unit Price USD'].mean()

    # Percentage Difference
    percent_difference = ((avg_price - avg_cost) / avg_cost) * 100

    # Visualizations for Costs and Prices
    plt.figure(figsize=(6, 4))
    plt.bar(['Max Cost', 'Total Cost', 'Average Cost'], [max_cost, sum_cost, avg_cost])
    plt.title('Unit Cost Analysis')
    plt.ylabel('Cost (USD)')
    plt.show()

    plt.figure(figsize=(6, 4))
    plt.bar(['Max Price', 'Total Price', 'Average Price'], [max_price, sum_price, avg_price])
    plt.title('Unit Price Analysis')
    plt.ylabel('Price (USD)')
    plt.show()

    plt.figure(figsize=(6, 4))
    plt.bar(['Avg Cost', 'Avg Price'], [avg_cost, avg_price], color=['blue', 'green'])
    plt.title('Comparison of Average Cost and Price')
    plt.ylabel('USD')
    plt.annotate(f'{percent_difference:.2f}%', xy=(0.5, (avg_cost + avg_price) / 2), 
                 xytext=(1, avg_price + 2), ha='center', arrowprops=dict(arrowstyle='->'))
    plt.show()

    print(f"Max Unit Cost: {max_cost}")
    print(f"Sum of Unit Costs: {sum_cost}")
    print(f"Average Unit Cost: {avg_cost}")
    print(f"Max Unit Price: {max_price}")
    print(f"Sum of Unit Prices: {sum_price}")
    print(f"Average Unit Price: {avg_price}")
    print(f"Percentage Difference: {percent_difference:.2f}%")

    # Analyze brands
    analyze_brands(products_data)


def analyze_brands(products_data):
    # Count unique brands
    unique_brands = products_data['Brand'].nunique()
    print(f"Number of Unique Brands: {unique_brands}")

    # Find the most popular brand
    brand_counts = products_data['Brand'].value_counts()
    most_popular_brand = brand_counts.idxmax()
    most_popular_count = brand_counts.max()
    print(f"Most Popular Brand: {most_popular_brand} (Appears {most_popular_count} times)")

    # Visualize Brand Popularity
    plt.figure(figsize=(10, 6))
    brand_counts.plot(kind='bar', color='skyblue')
    plt.title('Brand Popularity')
    plt.xlabel('Brand')
    plt.ylabel('Number of Products')
    plt.show()
