import pandas as pd
import numpy as np

def compute_basic_stats(df: pd.DataFrame) -> dict:
    stats = {}
    if 'number_of_stops' in df.columns:
        stats['stops_max'] = int(df['number_of_stops'].max())
        stats['stops_min'] = int(df['number_of_stops'].min())
        stats['stops_avg'] = float(df['number_of_stops'].mean())
    # bags / parcels / oversize
    for col, name in [('number_of_bags','bags'), ('number_of_parcels','parcels'), ('oversize_packages','oversize')]:
        if col in df.columns:
            stats[f'{name}_avg'] = float(df[col].mean())
            stats[f'{name}_max'] = int(df[col].max())
            stats[f'{name}_min'] = int(df[col].min())

    # total and ratio example
    if 'number_of_parcels' in df.columns and 'number_of_bags' in df.columns:
        total_parcels = df['number_of_parcels'].sum()
        total_bags = df['number_of_bags'].sum()
        stats['avg_parcels_per_bag'] = float(total_parcels / total_bags) if total_bags else np.nan

    # mileage summary
    stats['avg_driver_daily'] = float(df['milage_x_daily'].mean()) if 'milage_x_daily' in df.columns else np.nan
    stats['avg_ementor_daily'] = float(df['milage_y_daily'].mean()) if 'milage_y_daily' in df.columns else np.nan
    stats['avg_extra_daily'] = float(df['extra_milage_daily'].mean()) if 'extra_milage_daily' in df.columns else np.nan

    # score percentage above threshold
    if 'score' in df.columns:
        threshold = 847
        days_higher = (df['score'] > threshold).sum()
        total_days = df['score'].count()
        stats['percentage_higher'] = (days_higher / total_days) * 100 if total_days else 0.0
    else:
        stats['percentage_higher'] = 0.0

    return stats
