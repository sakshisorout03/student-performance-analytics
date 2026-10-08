import pandas as pd
import numpy as np
from functions import calculate_total, calculate_average, assign_grade, check_pass_fail

# Load dataset
df = pd.read_csv("students.csv")

# Calculate Total, Average, Grade and Status
totals = []
averages = []
grades = []
status = []

for index, row in df.iterrows():
    marks = [row['Python'], row['AI_ML'], row['Data_Science']]
    
    total = calculate_total(marks)
    avg = calculate_average(marks)
    grade = assign_grade(avg)
    result = check_pass_fail(avg, row['Attendance'])

    totals.append(total)
    averages.append(round(avg, 2))
    grades.append(grade)
    status.append(result)

df['Total'] = totals
df['Average'] = averages
df['Grade'] = grades
df['Status'] = status

# Display results
print("===== Student Performance Analysis =====")
print(df)

print("\n===== Top 5 Performers =====")
print(df.sort_values(by='Average', ascending=False).head(5)[['Student_ID', 'Name', 'Average', 'Grade']])

print("\n===== Subject-wise Analysis =====")
print(f"Python - Avg: {df['Python'].mean():.2f}, Max: {df['Python'].max()}, Min: {df['Python'].min()}")
print(f"AI_ML - Avg: {df['AI_ML'].mean():.2f}, Max: {df['AI_ML'].max()}, Min: {df['AI_ML'].min()}")
print(f"Data_Science - Avg: {df['Data_Science'].mean():.2f}, Max: {df['Data_Science'].max()}, Min: {df['Data_Science'].min()}")

print("\n===== Department-wise Average =====")
print(df.groupby('Department')['Average'].mean())

print(f"\nTotal Pass: {len(df[df['Status'] == 'Pass'])}")
print(f"Total Fail: {len(df[df['Status'] == 'Fail'])}")

# Save final report
df.to_csv("final_report.csv", index=False)
print("\nFinal report saved to final_report.csv")