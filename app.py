from flask import Flask
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('final_report.csv')

    # Top 5 Performers
    top5 = df.sort_values(by='Average', ascending=False).head(5)[['Student_ID','Name','Average','Grade']]
    top5_html = top5.to_html(classes='table table-sm table-bordered', index=False)

    # Subject-wise Analysis
    subjects = ['Python', 'AI_ML', 'Data_Science']
    sub_data = []
    for sub in subjects:
        sub_data.append(f"<tr><td>{sub}</td><td>{round(df[sub].mean(),2)}</td><td>{df[sub].max()}</td><td>{df[sub].min()}</td></tr>")
    sub_table = "".join(sub_data)

    # Department-wise Average
    dept_avg = df.groupby('Department')['Average'].mean().round(2).reset_index()
    dept_html = dept_avg.to_html(classes='table table-sm table-bordered', index=False)

    # Stats
    total_pass = len(df[df['Status']=='Pass'])
    total_fail = len(df[df['Status']=='Fail'])
    full_table = df.to_html(classes='table table-striped table-bordered', index=False)

    return f"""
    <html><head><title>Student Analytics Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head><body style="background:#f0f2f5">
    <div class="container mt-3">
        <h2 class="text-center text-primary">Student Performance Analytics</h2>
        <p class="text-center">By Sakshi Sorout | Python Data Science Project</p>

        <div class="row mt-4">
            <div class="col-md-6"><div class="card p-3 shadow-sm mb-3">
                <h5>🏆 Top 5 Performers</h5>{top5_html}
            </div></div>
            <div class="col-md-6"><div class="card p-3 shadow-sm mb-3">
                <h5>📚 Subject-wise Analysis (Avg, Max, Min)</h5>
                <table class="table table-sm table-bordered"><tr><th>Subject</th><th>Avg</th><th>Max</th><th>Min</th></tr>{sub_table}</table>
                <h5 class="mt-3">🏢 Department-wise Average</h5>{dept_html}
                <h5 class="mt-3">✅ Total Pass: {total_pass} | ❌ Total Fail: {total_fail}</h5>
            </div></div>
        </div>

        <div class="card p-3 shadow-sm mt-2">
            <h5>📋 Final Report - Complete Data</h5>
            <div class="table-responsive">{full_table}</div>
        </div>
        <br><br>
    </div></body></html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
