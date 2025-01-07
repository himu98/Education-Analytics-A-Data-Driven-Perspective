import pandas as pd
import random

# Step 1: Define dataset parameters
tutors = ["Alex Johnson", "Maria Lee", "David Kim", "Sophia Brown", "Chris White", "Emma Green", "James Hall", "Olivia Adams", "Liam Scott", "Ella Turner"]
subjects = ["Physics", "Math", "English", "History", "Chemistry", "Biology", "Computer Science", "Economics"]
class_types = ["Lecture", "Workshop", "Q&A", "Seminar"]
ratings = [round(random.uniform(3.5, 5.0), 1) for _ in range(500)]

# Step 2: Generate dataset
data = {
    "Date": [f"2024-01-{str(random.randint(1, 31)).zfill(2)}" for _ in range(500)],
    "Tutor Name": [random.choice(tutors) for _ in range(500)],
    "Subject": [random.choice(subjects) for _ in range(500)],
    "Class Type": [random.choice(class_types) for _ in range(500)],
    "Hours Spent": [round(random.uniform(1, 3), 1) for _ in range(500)],
    "Student Count": [random.randint(10, 40) for _ in range(500)],
    "Rating": ratings
}

# Step 3: Create a DataFrame
df = pd.DataFrame(data)

# Step 4: Save as CSV
output_path = "Large_Sample_Education_Dataset.csv"
df.to_csv(output_path, index=False)

print(f"Dataset created and saved as {output_path}")
