from flask import Flask, render_template, request,session,redirect,url_for,send_file
import os
import pandas as pd
from data_loader import load_data
from anomaly_detection import detect_anomalies
from deduplication import remove_duplicates
from data_cleaning import clean_data

app = Flask(__name__)
app.secret_key = "supersecretkey"  

UPLOAD_FOLDER = "processed_files"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    file = request.files["file"]
    if not file:
        return "No file uploaded!", 400

    df = pd.read_csv(file)
    df_cleaned = clean_data(df)
    anomalies = detect_anomalies(df_cleaned)
    df_no_duplicates = remove_duplicates(df_cleaned)
    cleaned_file_path = os.path.join(UPLOAD_FOLDER, "cleaned_data.csv")
    df_no_duplicates.to_csv(cleaned_file_path, index=False)

    session["total_rows"] = len(df)
    session["anomalies"] = anomalies.shape[0]
    session["cleaned_rows"] = len(df_no_duplicates)

    return redirect(url_for("results")) 

@app.route("/results")
def results():
    return render_template(
        "results.html",
        total_rows=session.get("total_rows"),
        anomalies=session.get("anomalies"),
        cleaned_rows=session.get("cleaned_rows"),
        download_link="/download"
    )

@app.route("/download")
def download():
    """Allow users to download the cleaned CSV file."""
    cleaned_file_path = os.path.join(UPLOAD_FOLDER, "cleaned_data.csv")
    return send_file(cleaned_file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
    