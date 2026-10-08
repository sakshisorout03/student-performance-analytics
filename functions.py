import numpy as np

def calculate_total(marks_list):
    """Calculate total marks using NumPy sum."""
    return np.sum(marks_list)

def calculate_average(marks_list):
    """Calculate average marks using NumPy mean."""
    return np.mean(marks_list)

def assign_grade(average):
    """Assign grade based on average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def check_pass_fail(average, attendance):
    """Check Pass/Fail based on average and attendance criteria."""
    if average >= 50 and attendance >= 75:
        return "Pass"
    else:
        return "Fail"