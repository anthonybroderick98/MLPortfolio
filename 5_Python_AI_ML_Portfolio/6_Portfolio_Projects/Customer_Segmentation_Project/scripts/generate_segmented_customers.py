import pandas as pd

# ✅ Sample clustered dataset
data = {
    "Annual Income": [15, 16, 17, 35, 37, 40, 75, 77, 80, 85],
    "Spending Score": [39, 81, 6, 77, 40, 76, 10, 4, 90, 88],
    "Age": [18, 22, 28, 45, 39, 50, 55, 42, 30, 21],
    "Cluster": [0, 1, 2, 1, 0, 2, 0, 1, 2, 1]
}

# ✅ Create DataFrame
df = pd.DataFrame(data)

# ✅ Save as CSV in the results folder
df.to_csv("../results/segmented_customers.csv", index=False)

print("✅ 'segmented_customers.csv' has been generated successfully.")
