import pandas as pd

def load_data(file_path):
    """Loads dataset from a given CSV file."""
    try:
        data = pd.read_csv(file_path)
        print(f"Dataset loaded with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

if __name__ == "__main__":
    df = load_data("../data/sample_data.csv")
    print(df.head())
