from flask import Flask
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('final_report.csv')
    top5 = df.sort_values(by='Average', ascending=False).head(5)[['Student_ID','Name','Average','Grade']]
    dept_avg = df.groupby('Department')['Average'].mean().round(2).reset_index()

    subjects = ['Python', 'AI_ML', 'Data_Science']
    sub_rows = ""
    for sub in subjects:
        sub_rows += f"<tr><td>{sub}</td><td>{round(df[sub].mean(),2)}</td><td>{df[sub].max()}</td><td>{df[sub].min()}</td></tr>"

    return f"""
    <html><head>
    <title>Sakshi - Python with AI Project</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head><body style="background:#f0f2f5">
    <div class="container mt-3">
        <h4 class="text-center text-primary">Student Performance Analytics</h4>
        <p class="text-center">By Sakshi | MCA Student | Python with AI Project</p>

        <div class="row">
            <div class="col-md-6"><div class="card p-3 shadow-sm mb-3">
                <h6>🏆 Top 5 Performers</h6>
                {top5.to_html(classes='table table-bordered', index=False)}
            </div></div>
            <div class="col-md-6"><div class="card p-3 shadow-sm mb-3">
                <h6>📚 Subject-wise Analysis (Avg, Max, Min)</h6>
                <table class="table table-bordered"><tr><th>Subject</th><th>Avg</th><th>Max</th><th>Min</th></tr>{sub_rows}</table>
                <h6 class="mt-3">🏢 Department-wise Average</h6>
                {dept_avg.to_html(classes='table table-bordered', index=False)}
                <p class="mt-2">✅ Total Pass: {len(df[df['Status']=='Pass'])} | ❌ Total Fail: {len(df[df['Status']=='Fail'])}</p>
            </div></div>
        </div>

        <div class="card p-3 shadow-sm">
            <h6>📋 Final Report - Complete Data</h6>
            <div class="table-responsive">{df.to_html(classes='table table-bordered table-striped', index=False)}</div>
        </div>

        <div class="text-center mt-4 mb-4 p-3 bg-dark text-white rounded">
            <p class="m-0">Project by Sakshi | MCA | Python with AI</p>
        </div>
    </div></body></html>
    """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
