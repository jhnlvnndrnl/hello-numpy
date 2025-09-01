import numpy as np

# 1. Create a 2D NumPy array for the student scores
scores = np.array([
    [85, 90, 78],
    [88, 76, 92],
    [95, 89, 96],
    [70, 65, 80],
    [60, 75, 85]
])

# 2. Find the average score of each student
student_avg = np.mean(scores, axis=1)
print("Average score of each student:", student_avg)

# 3. Find the highest score in each subject
subject_max = np.max(scores, axis=0)
print("Highest score in each subject (Math, Science, English):", subject_max)

# 4. Find the overall average score of the class
class_avg = np.mean(scores)
print("Overall class average score:", class_avg)

# 5. Bonus: Find which student has the highest total score
student_total = np.sum(scores, axis=1)
top_student = np.argmax(student_total)
print("Student with highest total score:", top_student + 1)  # +1 for student number
