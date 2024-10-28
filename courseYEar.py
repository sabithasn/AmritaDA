import pandas as pd

# Load the Excel file
input_file = "input.xlsx"  # Replace with your input file path
output_file = "courses_per_year.xlsx"  # Output file to save courses per year

# Read the Excel sheet with student data
# Assuming the sheet has columns: 'StudentID', 'Course', 'Year'
df = pd.read_excel(input_file, sheet_name='Sheet1')

# Drop duplicate rows to ensure each course-year combination is unique
unique_courses_per_year = df[['JoiningYear', 'AcademicProgram']].drop_duplicates()

# Write to a new Excel file with a single sheet
with pd.ExcelWriter(output_file) as writer:
    unique_courses_per_year.to_excel(writer, sheet_name='Courses_Per_Year', index=False)

print("Courses per year have been saved to", output_file)
