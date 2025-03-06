# -------------------------------------------------------
# ENCODING CATEGORICAL VARIABLES FOR MACHINE LEARNING
# -------------------------------------------------------

# This script converts categorical text labels into numerical representations
# using Label Encoding and One-Hot Encoding.

# Import required library for data manipulation.
import pandas as pd  # Library for working with datasets

# -------------------------------------------------------
# LABEL ENCODING (CONVERTS CATEGORIES TO NUMBERS)
# -------------------------------------------------------

# This function replaces categorical text labels with numerical values. Label Encoding assigns
# a unique integer to each category, making it suitable for ordinal data.

def encode_label(df, column_name):
    """
    Converts categorical text labels into numerical values using Label Encoding.

    Parameters:
    - df (DataFrame): The input DataFrame.
    - column_name (str): The categorical column to encode.

    Returns:
    - DataFrame with encoded column.
    """
    df[column_name] = df[column_name].astype("category").cat.codes  # Convert text labels to numbers
    print(f"✅ '{column_name}' encoded using Label Encoding.")
    return df

# -------------------------------------------------------
# ONE-HOT ENCODING (CREATES BINARY COLUMNS FOR CATEGORIES)
# -------------------------------------------------------

# This function converts categorical values into multiple binary columns, ensuring that no 
# numerical relationship is assumed between different categories.

def encode_one_hot(df, column_name):
    """
    Converts categorical values into numerical format using One-Hot Encoding.

    Parameters:
    - df (DataFrame): The input DataFrame.
    - column_name (str): The categorical column to encode.

    Returns:
    - DataFrame with one-hot encoded columns.
    """
    df = pd.get_dummies(df, columns=[column_name], drop_first=True)  # Create binary columns
    print(f"✅ '{column_name}' encoded using One-Hot Encoding.")
    return df

# -------------------------------------------------------
# CREATING SAMPLE DATA & APPLYING ENCODING TECHNIQUES
# -------------------------------------------------------

# This section creates a sample dataset with categorical variables for testing
# Label Encoding and One-Hot Encoding.

if __name__ == "__main__":
    # Define a dictionary representing a dataset with categorical features.
    sample_data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],  # Names of individuals
        "Gender": ["Female", "Male", "Male", "Male", "Female"],  # Gender (Categorical)
        "Membership": ["Gold", "Silver", "Silver", "Gold", "Platinum"]  # Membership type (Categorical)
    }
    
    # Convert the dictionary into a Pandas DataFrame.
    df = pd.DataFrame(sample_data)
    
    # Display the original dataset before encoding.
    print("\n📌 Original Data:\n", df)

    # Apply Label Encoding to 'Gender' column
    df = encode_label(df, "Gender")

    # Apply One-Hot Encoding to 'Membership' column
    df = encode_one_hot(df, "Membership")

    # Display the processed dataset after encoding.
    print("\n📌 Processed Data:\n", df)

# -------------------------------------------------------
# CREATING SAMPLE DATA & APPLYING ENCODING TECHNIQUES
# -------------------------------------------------------

# This section creates a sample dataset with categorical variables for testing
# Label Encoding and One-Hot Encoding.

if __name__ == "__main__":
    # Define a dictionary representing a dataset with categorical features.
    sample_data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],  # Names of individuals
        "Gender": ["Female", "Male", "Male", "Male", "Female"],  # Gender (Categorical)
        "Membership": ["Gold", "Silver", "Silver", "Gold", "Platinum"]  # Membership type (Categorical)
    }
    
    # Convert the dictionary into a Pandas DataFrame.
    df = pd.DataFrame(sample_data)
    
    # Display the original dataset before encoding.
    print("\n📌 Original Data:\n", df)

    # Apply Label Encoding to 'Gender' column
    df = encode_label(df, "Gender")

    # Apply One-Hot Encoding to 'Membership' column
    df = encode_one_hot(df, "Membership")

    # Display the processed dataset after encoding.
    print("\n📌 Processed Data:\n", df)

# -------------------------------------------------------
# SAVING ENCODED DATA TO CSV
# -------------------------------------------------------

# Define the output file name.
output_file = "encoded_data.csv"

# Save the processed DataFrame to a CSV file.
df.to_csv(output_file, index=False)

# Confirm that the file has been saved successfully.
print(f"\n✅ Processed data saved to '{output_file}'.")
