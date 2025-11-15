import pandas as pd
from pipeline.etl import clean_data


def test_clean_data():
    df = pd.DataFrame({"amount": [10, None, None]})
    cleaned = clean_data(df)
    assert cleaned["amount"].isna().sum() == 0
