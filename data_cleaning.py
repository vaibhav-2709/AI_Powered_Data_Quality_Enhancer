import pandas as pd

def clean_data(df):
    """Handle missing values and inconsistent data."""
    df.fillna(df.mean(numeric_only=True), inplace=True)  # Fill numeric NaN with mean
    df.fillna("", inplace=True)  # Fill categorical NaN with empty string
    return df

if __name__ == "__main__":
    data = pd.read_csv("../data/sample_data.csv")
    cleaned_data = clean_data(data)
    print(cleaned_data.head())
