import random
import pandas as pd
import numpy as np
from faker import Faker
# HeartBreak Party Supply = company name

# Initialize Faker for generating dummy data
fake = Faker()

# Set the number of rows for your dataset
num_rows = 1000

# Create a list of Product IDs, Product Names and Product Category
product_id = ['P001', 'P002', 'P003', 'P004', 'P005']
product_name = ['Heart Shaped plates', 'Pink cupcake mix', 'heart balloons', 'pink plastic champagne cups', 'plastic rose petals']
product_category = ['Tableware', 'Food and Drinks', 'Decorations', 'Tableware','Decorations']

# Create a DataFrame with repeated Product IDs for 1000 rows
repeated_product_id = np.tile(product_id, 200)
# shuffled_product_id = np.random.permutation(repeated_product_id)[:1000]

# Create a DataFrame with repeated Product IDs for 1000 rows
repeated_product_name = np.tile(product_name, 200)
# shuffled_product_name = np.random.permutation(repeated_product_name)[:1000]

# Create a DataFrame with repeated Product IDs for 1000 rows
repeated_product_category = np.tile(product_category, 200)

# keeping the shuffle lines for if I reference this code in the future and need to shuffle an array in a dataset

# Generate dummy data for each column
data = {
    'Date/Time': [fake.date_time_between(start_date='-1y', end_date='now') for _ in range(num_rows)],
    "Product ID": repeated_product_id,
    "Product Name": repeated_product_name,
    'Sales Amount': [round(random.uniform(5, 40), 2) for _ in range(num_rows)],
    'Order ID': [f'0{random.randint(100000, 999999)}' for _ in range(num_rows)],
    'Quantity Sold': [random.randint(1, 200) for _ in range(num_rows)],
    'Customer ID': [f'C{random.randint(1000, 9000)}' for _ in range(num_rows)],
    'Customer Name': [fake.name() for _ in range(num_rows)],
    'Region': [fake.state() for _ in range(num_rows)],
    'Location': [fake.city() for _ in range(num_rows)],
    'Salesperson ID': [f'S{random.randint(1000, 9000)}' for _ in range(num_rows)],
    'Salesperson Name': [fake.name() for _ in range(num_rows)],
    'Product Category': repeated_product_category,
    'Discounts/Promotions': [round(random.uniform(0, 100), 2) for _ in range(num_rows)],
    'Profit Margin': [round(random.uniform(5, 50), 2) for _ in range(num_rows)],
    'Payment Method': [random.choice(['Credit Card', 'Cash', 'Online Transfer']) for _ in range(num_rows)],
    'Order Status': [random.choice(['Pending', 'Completed', 'Canceled']) for _ in range(num_rows)]
    }

# Combine Product IDs, Product names, and other columns into a DataFrame
product_df = pd.DataFrame(data)

# Display the resulting dataset
print(product_df)

# Save the DataFrame to a CSV file
csv_filename = "Sales_Performance_dataset.csv"
product_df.to_csv(csv_filename, index=False)
print(f"CSV file '{csv_filename}' has been generated.")

