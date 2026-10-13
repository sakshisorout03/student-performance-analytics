from flask import Flask
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        df = pd.read_csv('final_report.csv')
        table = df.to_html(classes='table table-bordered table-striped', index=False)
        title = "Final Report - final_report.csv"
    except:
        df = pd.read_csv('students.csv')
        table = df.to_html(classes='table table-bordered table-striped', index=False)
        title = "Students Data - students.csv"

    return f"""
    <html><head><title>Student Performance Analytics</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head><body><div class="container mt-4">
    <h2 class="text-center text-primary">Student Performance Analytics</h2>
    <p class="text-center"><b>By Sakshi Sorout</b> - Python Data Science Project</p><hr>
    <h4>{title}</h4><div class="table-responsive">{table}</div>
    </div></body></html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
