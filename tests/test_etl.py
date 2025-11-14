import pandas as pd
from pipeline.etl import clean_data

def test_clean_data():
    df = pd.DataFrame({"amount": [10, None, None]})
    clean_df = clean_data(df)

    assert clean_df["amount"].isna().sum() == 0