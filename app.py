from flask import Flask
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('final_report.csv')
    top5 = df.sort_values(by='Average', ascending=False).head(5)
    dept_avg = df.groupby('Department')['Average'].mean().round(2).reset_index()

    return f"""
    <html>
    <head>
        <title>Sakshi Sorout - Student Analytics Portfolio</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body style="background:#f8f9fa">

    <!-- NAVBAR jaise Portfolio me hota hai -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
      <div class="container">
        <a class="navbar-brand" href="#">Sakshi Sorout</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item"><a class="nav-link" href="#home">Home</a></li>
            <li class="nav-item"><a class="nav-link" href="#dashboard">Dashboard</a></li>
            <li class="nav-item"><a class="nav-link" href="#top">Top 5</a></li>
            <li class="nav-item"><a class="nav-link" href="#analysis">Analysis</a></li>
            <li class="nav-item"><a class="nav-link" href="#report">Full Report</a></li>
            <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="container mt-4">

        <!-- HOME SECTION -->
        <section id="home" class="text-center py-5 bg-white rounded shadow-sm">
            <h1 class="text-primary">Student Performance Analytics</h1>
            <p class="lead">A Python & Data Science Project to analyze student performance across departments</p>
            <p><b>By Sakshi Sorout</b> | BCA - MKM Group of Colleges, Hodal</p>
            <a href="#dashboard" class="btn btn-primary mt-2">View Analytics</a>
            <a href="https://github.com/sakshisorout03/student-performance-analytics" class="btn btn-dark mt-2">GitHub Code</a>
        </section>

        <!-- DASHBOARD SECTION -->
        <section id="dashboard" class="mt-5">
            <h3>📊 Dashboard Overview</h3>
            <div class="row text-center">
                <div class="col-md-3"><div class="card p-3 shadow-sm">Total Students<br><h3>{len(df)}</h3></div></div>
                <div class="col-md-3"><div class="card p-3 shadow-sm">Pass<br><h3>{len(df[df['Status']=='Pass'])}</h3></div></div>
                <div class="col-md-3"><div class="card p-3 shadow-sm">Class Avg<br><h3>{round(df['Average'].mean(),2)}%</h3></div></div>
                <div class="col-md-3"><div class="card p-3 shadow-sm">Topper<br><h6>{top5.iloc[0]['Name']}<br>{top5.iloc[0]['Average']}%</h6></div></div>
            </div>
        </section>

        <!-- TOP 5 SECTION -->
        <section id="top" class="mt-5 card p-3 shadow-sm">
            <h3>🏆 Top 5 Performers</h3>
            {top5[['Student_ID','Name','Department','Average','Grade']].to_html(classes='table table-bordered table-striped', index=False)}
        </section>

        <!-- ANALYSIS SECTION -->
        <section id="analysis" class="mt-5 row">
            <div class="col-md-6"><div class="card p-3 shadow-sm h-100">
                <h5>Subject-wise (Avg, Max, Min)</h5>
                <table class="table table-bordered">
                <tr><th>Subject</th><th>Avg</th><th>Max</th><th>Min</th></tr>
                <tr><td>Python</td><td>{round(df['Python'].mean(),2)}</td><td>{df['Python'].max()}</td><td>{df['Python'].min()}</td></tr>
                <tr><td>AI_ML</td><td>{round(df['AI_ML'].mean(),2)}</td><td>{df['AI_ML'].max()}</td><td>{df['AI_ML'].min()}</td></tr>
                <tr><td>Data_Science</td><td>{round(df['Data_Science'].mean(),2)}</td><td>{df['Data_Science'].max()}</td><td>{df['Data_Science'].min()}</td></tr>
                </table>
            </div></div>
            <div class="col-md-6"><div class="card p-3 shadow-sm h-100">
                <h5>Department-wise Average</h5>
                {dept_avg.to_html(classes='table table-bordered', index=False)}
            </div></div>
        </section>

        <!-- FULL REPORT -->
        <section id="report" class="mt-5 card p-3 shadow-sm">
            <h3>📋 Full Final Report</h3>
            <div class="table-responsive">{df.to_html(classes='table table-bordered table-striped', index=False)}</div>
        </section>

        <!-- CONTACT SECTION jaise Portfolio me hota hai -->
        <section id="contact" class="mt-5 mb-5 text-center card p-4 shadow-sm bg-dark text-white">
            <h3>Contact</h3>
            <p>Project By <b>Sakshi Sorout</b></p>
            <p>BCA 2nd Year | MKM Group of Colleges, Hodal</p>
            <p>GitHub: github.com/sakshisorout03 | Email: sakshisorout03@gmail.com</p>
            <p class="small">Python with AI & Data Science | Future Interns Internship</p>
        </section>

    </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
