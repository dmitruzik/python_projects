import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("charts", exist_ok=True)

def plot_stops_distribution(df: pd.DataFrame, out="charts/stops_distribution.png"):
    plt.figure(figsize=(8,4))
    if 'number_of_stops' in df.columns:
        sns.histplot(df['number_of_stops'].dropna(), bins=10, kde=True)
    plt.title("Distribution of Delivery Stops per Day")
    plt.xlabel("Number of Stops")
    plt.ylabel("Count of Days")
    plt.tight_layout()
    plt.savefig(out); plt.close()

def plot_avg_package_types(stats: dict, out="charts/avg_package_types.png"):
    cats = ['Bags','Parcels','Oversize']
    vals = [stats.get('bags_avg',0), stats.get('parcels_avg',0), stats.get('oversize_avg',0)]
    plt.figure(figsize=(6,4))
    plt.bar(cats, vals)
    plt.title("Average Package Types Per Day")
    plt.ylabel("Average Count")
    plt.tight_layout()
    plt.savefig(out); plt.close()

def plot_daily_mileage(df: pd.DataFrame, out="charts/daily_mileage_comparison.png"):
    plt.figure(figsize=(10,4))
    if 'date_x' in df.columns:
        plt.plot(df['date_x'], df['milage_x_daily'], label="Driver Mileage")
        plt.plot(df['date_x'], df['milage_y_daily'], label="eMentor Mileage")
        plt.gcf().autofmt_xdate()
    plt.title("Daily Mileage Comparison")
    plt.xlabel("Date")
    plt.ylabel("Miles")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out); plt.close()

def plot_extra_mileage(df: pd.DataFrame, out="charts/extra_mileage_distribution.png"):
    plt.figure(figsize=(8,4))
    sns.histplot(df['extra_milage_daily'].dropna(), bins=10, kde=True)
    plt.title("Distribution of Extra Miles Driven (Driver - eMentor)")
    plt.xlabel("Extra Miles")
    plt.ylabel("Days Count")
    plt.tight_layout()
    plt.savefig(out); plt.close()

def plot_score_vs_stops(df: pd.DataFrame, out="charts/score_vs_stops.png"):
    plt.figure(figsize=(7,5))
    sns.scatterplot(x=df['number_of_stops'], y=df['score'])
    plt.title("Delivery Score vs Number of Stops")
    plt.xlabel("Stops Per Day")
    plt.ylabel("Score")
    plt.tight_layout()
    plt.savefig(out); plt.close()

def plot_high_score_pie(percentage_higher: float, out="charts/high_score_percentage.png"):
    plt.figure(figsize=(5,5))
    plt.pie([percentage_higher, 100 - percentage_higher],
            labels=["Above 847 Score", "847 or Below"],
            autopct='%1.1f%%')
    plt.title("High Performance Days")
    plt.tight_layout()
    plt.savefig(out); plt.close()

def run_all_plots(df: pd.DataFrame, stats: dict):
    plot_stops_distribution(df)
    plot_avg_package_types(stats)
    plot_daily_mileage(df)
    plot_extra_mileage(df)
    plot_score_vs_stops(df)
    plot_high_score_pie(stats.get('percentage_higher', 0.0))
