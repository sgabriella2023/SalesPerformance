import random
import pandas as pd
from faker import Faker

# Initialize Faker for generating dummy data
fake = Faker()

# Set the number of rows for your dataset
num_rows = 1000

# Generate dummy data for each column
data = {
    'Date/Time': [fake.date_time_between(start_date='-1y', end_date='now') for _ in range(num_rows)],
    'Sales Amount': [round(random.uniform(5, 40), 2) for _ in range(num_rows)],
    'Order ID': [f'0{random.randint(100000, 999999)}' for _ in range(num_rows)],
    'Product ID': [random.choice(['P001', 'P002', 'P003']) for _ in range(num_rows)],
    'Product Name': [random.choice(['Lavender Lush', 'Winter Wonderland Peppermint', 'Citrus Splash Infusion']) for _ in range(num_rows)],
    'Quantity Sold': [random.randint(1, 200) for _ in range(num_rows)],
    'Customer ID': [f'C{random.randint(1000, 9000)}' for _ in range(num_rows)],
    'Customer Name': [fake.name() for _ in range(num_rows)],
    'Region': [fake.state() for _ in range(num_rows)],
    'Location': [fake.city() for _ in range(num_rows)],
    'Salesperson ID': [f'S{random.randint(1000, 9000)}' for _ in range(num_rows)],
    'Salesperson Name': [fake.name() for _ in range(num_rows)],
    'Product Category': [random.choice(['Essential Oil', 'Candle', 'Body Scrub']) for _ in range(num_rows)],
    'Discounts/Promotions': [round(random.uniform(0, 100), 2) for _ in range(num_rows)],
    'Profit Margin': [round(random.uniform(5, 50), 2) for _ in range(num_rows)],
    'Payment Method': [random.choice(['Credit Card', 'Cash', 'Online Transfer']) for _ in range(num_rows)],
    'Order Status': [random.choice(['Pending', 'Completed', 'Canceled']) for _ in range(num_rows)]
    }
"""
    'Product ID': [f'P{random.randint(100, 600)}' for _ in range(num_rows)],
"""
#Create a DataFrame from the generated data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_filename = "Sales_Performance_dataset.csv"
df.to_csv(csv_filename, index=False)
print(f"CSV file '{csv_filename}' has been generated.")
