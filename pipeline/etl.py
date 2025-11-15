import pandas as pd


def clean_data(df):
    """
    Drops duplicates and fills missing amounts with 0.
    """
    df = df.drop_duplicates()
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["amount"] = df["amount"].fillna(0)
    return df


def run_etl(input_path, output_path):
    """
    Runs entire ETL: read → clean → write.
    """
    df = pd.read_csv(input_path)
    df_clean = clean_data(df)
    df_clean.to_csv(output_path, index=False)
    print(f"ETL completed. Output saved to {output_path}")


if __name__ == "__main__":
    run_etl("data/input.csv", "data/output.csv")
    
