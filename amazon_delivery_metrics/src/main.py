
from cleaning_data import load_data, basic_type_casts, compute_daily_mileage
from analyzing_data import compute_basic_stats
from visualization import run_all_plots
import os

DATA_FP = os.path.join("..","data","merged_dataset.csv")  # adjust relative path if running from repo root

def main():
    df = load_data(DATA_FP)
    df = basic_type_casts(df)
    df = compute_daily_mileage(df)
    stats = compute_basic_stats(df)
    run_all_plots(df, stats)
    # optionally save cleaned / daily diff dataset
    out_fp = os.path.join("..","data","merged_daily_diffs.csv")
    df.to_csv(out_fp, index=False)
    print("Done. Charts saved in charts/ and cleaned data saved to", out_fp)

if __name__ == "__main__":
    main()






