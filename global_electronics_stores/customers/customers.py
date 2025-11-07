import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def analyze_customers():
    file_path = './data/Customers.csv'
    
    # Load the data with proper encoding
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='latin1')
    
    # Gender Analysis
    gender_counts = df['Gender'].value_counts()
    gender_percentages = (gender_counts / gender_counts.sum()) * 100

    plt.figure(figsize=(6, 6))
    gender_percentages.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['skyblue', 'pink'])
    plt.title('Percentage of Male and Female Customers')
    plt.ylabel('')
    plt.savefig('gender_percentage.png')  
    plt.show()

    # Age Analysis using 'Birthday' column
    if 'Birthday' in df.columns:
        df['Birthday'] = pd.to_datetime(df['Birthday'], errors='coerce')  # Convert to datetime
        df['Birth Year'] = df['Birthday'].dt.year  # Extract year from 'Birthday'
        current_year = datetime.now().year
        df['Age'] = current_year - df['Birth Year']
        average_age = df['Age'].mean()

        # Visualization with the average year as a number on the bar
        plt.figure(figsize=(8, 6))
        plt.bar(['Average Age'], [average_age], color='green')
        plt.text(0, average_age + 1, f'{average_age:.2f}', ha='center', va='bottom', fontsize=12, color='black')  # Annotate bar
        plt.title('Average Age of Customers')
        plt.ylabel('Age')
        plt.savefig('average_age.png')
        plt.show()
    else:
        print("Column 'Birthday' not found. Skipping age analysis.")

    # Country Analysis
    country_counts = df['Country'].value_counts()

    # Visualization with customer count on top of each bar
    plt.figure(figsize=(10, 6))
    bars = plt.bar(country_counts.index, country_counts.values, color='orange')
    plt.title('Number of Customers by Country')
    plt.xlabel('Country')
    plt.ylabel('Number of Customers')

    # Add annotations for each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 1, int(yval), ha='center', va='bottom', fontsize=10)

    plt.savefig('customers_by_country.png')
    plt.show()