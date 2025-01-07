# Data Visualization with Tableau

This project demonstrates the process of creating an educational dataset using Python and visualizing it with Tableau. The goal is to analyze trends in educational operations, such as tutor hours, class types, and student engagement, through interactive dashboards.

## Project Overview
- **Dataset Creation**: A custom dataset simulating an online learning platform's operations was generated using Python.
- **Visualization Tool**: Tableau was used to create interactive dashboards to derive actionable insights.
- **Key Insights**: Analysis of tutor performance, subject trends, and student participation.

---

## Dataset Generation

The dataset was created using a Python script to simulate real-world educational data. Key features of the dataset:

- **Columns**:
  - `Date`: The date of the class (e.g., `2024-01-01`).
  - `Tutor Name`: Names of tutors (e.g., `Alex Johnson`, `Maria Lee`).
  - `Subject`: Subjects taught (e.g., `Physics`, `Math`, `English`).
  - `Class Type`: Type of class (e.g., `Lecture`, `Workshop`, `Q&A`).
  - `Hours Spent`: Duration of each class in hours (e.g., `1.5`).
  - `Student Count`: Number of students attending (e.g., `25`).
  - `Rating`: Average class rating out of 5 (e.g., `4.5`).

- **Python Libraries Used**:
  - `pandas`: For data manipulation.
  - `random`: For generating random values to simulate real-world data.

### Python Script
The Python script used to generate the dataset is included in this repository as `data_generation.py`. To recreate the dataset:
1. Clone this repository.
2. Run the script in a Python environment.
3. The dataset will be saved as `Large_Sample_Education_Dataset.csv`.

---

## Tableau Visualization

The dataset was imported into Tableau to create interactive dashboards. Key visualizations include:

- **Tutor Performance Dashboard**:
  - Comparison of hours spent by tutors.
  - Most active subjects taught by each tutor.

- **Class Trends Dashboard**:
  - Analysis of class types and trends over time.

- **Student Engagement Dashboard**:
  - Patterns in student participation and ratings.

### How to View the Dashboard
The final Tableau dashboard is published on Tableau Public. You can view it here: [Tableau Dashboard Link](#) *(Replace with actual link once published)*

---

## Repository Structure

```
.
├── data_generation.py          # Python script to generate the dataset
├── Large_Sample_Education_Dataset.csv  # Generated dataset
├── Tableau_Project_File.twbx   # Tableau workbook (optional)
└── README.md                   # Project documentation
```

---

## How to Use
1. **Run the Python Script**: Generate the dataset by running `data_generation.py`.
2. **Open in Tableau**: Import `Large_Sample_Education_Dataset.csv` into Tableau.
3. **Customize Dashboards**: Use the dataset to create your own insights or use the provided Tableau workbook (if included).

---

## Key Learnings
- Data preparation and cleaning using Python.
- Designing insightful dashboards with Tableau.
- Understanding trends in educational operations through visualization.

---

## Future Scope
- Expanding the dataset to include more complex metrics (e.g., revenue, feedback trends).
- Automating the pipeline for real-time visualization updates.

---

## License
This project is open-source and available under the MIT License.

---

## Contact
**Shakib Hasan Himu**  
[LinkedIn](https://www.linkedin.com/in/shakib-hasan-himu-479623204/)  
[Email](mailto:shakibhasanhimu466@gmail.com)
