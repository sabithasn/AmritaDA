import pandas as pd
import os

# Function to split Excel file based on a column value
def split_excel(input_file, column_name):
    # Read the Excel file
    df = pd.read_excel(input_file)
    
    # Get unique values from the specified column
    unique_values = df[column_name].unique()
    
    # Create an output directory
    output_dir = 'Year'
    os.makedirs(output_dir, exist_ok=True)
    
    # Loop through unique values and create separate Excel files
    for value in unique_values:
        # Filter the DataFrame for the current unique value
        filtered_df = df[df[column_name] == value]
        
        # Define the output file name
        output_file = os.path.join(output_dir, f"{value}.xlsx")
        
        # Save the filtered DataFrame to a new Excel file
        filtered_df.to_excel(output_file, index=False)
        print(f"Created: {output_file}")

# Example usage
if __name__ == "__main__":
    input_excel_file = 'input.xlsx'  # Replace with your input Excel file path
    column_to_split_by = 'JoiningYear'  # Replace with the column name you want to split by
    split_excel(input_excel_file, column_to_split_by)
