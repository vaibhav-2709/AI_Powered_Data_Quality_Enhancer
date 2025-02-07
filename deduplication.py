import pandas as pd

def remove_duplicates(df):
    """Remove duplicate rows from dataset."""
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    print(f"Removed {before - after} duplicate rows.")
    return df

if __name__ == "__main__":
    data = pd.read_csv("../data/sample_data.csv")
    cleaned_data = remove_duplicates(data)
    print(cleaned_data.head())
