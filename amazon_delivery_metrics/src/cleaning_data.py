import pandas as pd
import numpy as np

# -------------------- INSPECT DATA ----------------------------------


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def basic_type_casts(df: pd.DataFrame) -> pd.DataFrame:
    # Example of safe numeric conversions
    numeric_cols = [
        'number_of_bags','number_of_parcels','oversize_packages',
        'number_of_stops','number_of_returns','score',
        'milage_x','milage_y'
    ]
    for c in numeric_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')
    if 'date_x' in df.columns:
        df['date_x'] = pd.to_datetime(df['date_x'], errors='coerce')
    return df

def compute_daily_mileage(df: pd.DataFrame, threshold_max:int=1000) -> pd.DataFrame:
    if 'milage_x' in df.columns and 'milage_y' in df.columns:
        df = df.sort_values('date_x').reset_index(drop=True)
        df['milage_x_daily'] = df['milage_x'].diff()
        df['milage_y_daily'] = df['milage_y'].diff()

        mask_invalid_x = (df['milage_x_daily'] <= 0) | (df['milage_x_daily'] > threshold_max)
        mask_invalid_y = (df['milage_y_daily'] <= 0) | (df['milage_y_daily'] > threshold_max)

        df.loc[mask_invalid_x, 'milage_x_daily'] = np.nan
        df.loc[mask_invalid_y, 'milage_y_daily'] = np.nan
        df['extra_milage_daily'] = df['milage_x_daily'] - df['milage_y_daily']
    else:
        df['milage_x_daily'] = np.nan
        df['milage_y_daily'] = np.nan
        df['extra_milage_daily'] = np.nan
    return df
