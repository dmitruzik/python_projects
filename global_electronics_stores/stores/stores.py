import pandas as pd
import matplotlib.pyplot as plt

def analyze_stores():
    stores_data = pd.read_csv('./data/Stores.csv')

    stores_data = stores_data.dropna(subset=['Square Meters'])
    largest_store = stores_data.loc[stores_data['Square Meters'].idxmax()]
    average_size = stores_data['Square Meters'].mean()


    country_counts = stores_data['Country'].value_counts()

    plt.figure(figsize=(10, 6))
    country_counts.plot(kind='bar', color='skyblue')
    plt.title('Number of Stores Per Country')
    plt.xlabel('Country')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 6))
    bars = plt.bar(['Largest Store', 'Average Store'], [largest_store['Square Meters'], average_size], color=['blue', 'orange'])
    plt.title('Comparison of Largest Store and Average Store Size')
    plt.ylabel('Square Meters')

    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height():.0f} m²', 
             ha='center', va='bottom', fontsize=10, color='black')

    plt.tight_layout()
    plt.show()
