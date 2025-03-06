# -------------------------------------------------------
# PANDAS DATA WRANGLING FOR AI/ML
# -------------------------------------------------------

# This script demonstrates fundamental Pandas operations 
# for data manipulation and visualization.

import pandas as pd  # Data handling library
import matplotlib.pyplot as plt  # Visualization library

# -------------------------------------------------------
# CREATING A PANDAS DATAFRAME
# -------------------------------------------------------

# A Pandas DataFrame is a structured table-like dataset.
# Here, we define a dataset with sample names, ages, and salaries.
print("\n📌 Creating a Pandas DataFrame")

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],  # Sample names
    "Age": [25, 30, 35, 40],  # Sample ages
    "Salary": [50000, 60000, 70000, 80000]  # Sample salaries
}

df = pd.DataFrame(data)  # Convert dictionary to DataFrame

# Display the dataset
print(df)

# -------------------------------------------------------
# SELECTING SPECIFIC COLUMNS
# -------------------------------------------------------

# Pandas allows easy selection of specific columns.
# We extract the "Age" column as a Pandas Series.
print("\n📌 Selecting a Column (Series)")

print(df["Age"])  # Print only the Age column

# -------------------------------------------------------
# FILTERING DATA
# -------------------------------------------------------

# Filtering allows us to extract rows based on conditions.
# Here, we filter records where Age is greater than 30.
print("\n📌 Filtering Rows (Age > 30)")

filtered_df = df[df["Age"] > 30]  # Apply filtering condition

# Display the filtered DataFrame
print(filtered_df)

# -------------------------------------------------------
# ADDING A NEW COLUMN
# -------------------------------------------------------

# We can create new columns by performing calculations 
# on existing columns.
print("\n📌 Adding a New Column (Bonus)")

df["Bonus"] = df["Salary"] * 0.10  # Compute 10% of Salary as Bonus

# Display the updated DataFrame
print(df)

# -------------------------------------------------------
# GROUPING DATA
# -------------------------------------------------------

# Grouping allows us to perform aggregated calculations.
# Here, we calculate the mean salary for each Age group.
print("\n📌 Grouping Data by Age")

grouped_df = df.groupby("Age")["Salary"].mean()  # Compute mean salary per Age

# Display grouped data
print(grouped_df)

# -------------------------------------------------------
# VISUALIZING DATA (SALARY VS AGE)
# -------------------------------------------------------

# Visualization helps in analyzing trends in datasets.
# We generate a bar chart to represent Salary by Age.
print("\n📌 Generating Visualization: Salary vs Age")

# Set figure size
plt.figure(figsize=(8, 5))

# Create a bar chart
plt.bar(df["Age"], df["Salary"], color=["blue", "green", "orange", "red"])

# Label axes
plt.xlabel("Age")
plt.ylabel("Salary ($)")
plt.title("Salary by Age")

# Add grid for readability
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Save the visualization as an image file
image_path = "pandas_visualization.png"
plt.savefig(image_path)

print(f"\n✅ Data visualization saved successfully: {image_path}")
