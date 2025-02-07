import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df, contamination=0.05):
    """Detect anomalies using Isolation Forest."""
    model = IsolationForest(n_estimators=100, contamination=contamination, random_state=42)
    df['anomaly'] = model.fit_predict(df.select_dtypes(include=['number']))  # Only numeric columns
    return df[df['anomaly'] == -1]  # Returning anomalous data

if __name__ == "__main__":
    data = pd.read_csv("../data/sample_data.csv")
    anomalies = detect_anomalies(data)
    print("Detected Anomalies:")
    print(anomalies)
