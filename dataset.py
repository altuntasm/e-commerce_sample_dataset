import pandas as pd
import numpy as np

# Create an empty DataFrame by specifying column names
columns_products = ["product_id", "stock", "maincategory"]

# Generate unique product_id
product_ids = np.random.choice(range(1000, 10000), size=5000, replace=False)

# Stock quantity and category
stocks = np.random.randint(20, 101, size=5000)
categories = np.random.choice(["Abaya", "Shawl", "Tunic", "Shoes", "Bags", "Skirt"], size=5000)

# Populate the DataFrame
products = pd.DataFrame({
    "product_id": product_ids,
    "stock": stocks,
    "maincategory": categories
})

# Display the first few rows
# print(products.head())

# Create an empty DataFrame by specifying column names
columns_customers = ["customer_id", "name", "country", "segment", "e-mail"]

# Generate unique customer_id
customer_ids = np.random.choice(range(10000, 20000), size=2000, replace=False)

# name, country, segment
name = np.random.choice(["Ayse", "Zeynep", "Hilal", "Asena", "Nazli", "Betul", "Heba", "Angela", "Doga", "Deniz",
                         "Melek", "Sinem", "Ali", "Akif", "Mehmet"], size=2000)
country = np.random.choice(["1", "2", "3", "4", "5", "6"], size=2000)
segment = np.random.choice(["Churn", "Likelihood to Churn", "Silver", "Gold", "Elite"], size=2000)

# Create the email field using name and customer_id
emails = [f"{name.lower()}{cid}@vuhuv.com" for name, cid in zip(name, customer_ids)]

customers = pd.DataFrame({
    "customer_id": customer_ids,
    "name": name,
    "country": country,
    "segment": segment,
    "e-mail": emails
})

# Display the first few rows
# print(customers.head())

# Define the total number of rows and the number of repeated order_id
num_rows = 40000
num_unique_orders = 10000  # Number of repeated order_id

# Generate order_id and customer_id
order_ids = np.repeat(np.random.choice(range(101000, 199000), size=num_unique_orders, replace=False), 4)
customer_id = np.repeat(np.random.choice(customers["customer_id"], size=num_unique_orders, replace=True), 4)

# Select unique product_id values within the same order_id
product_id = []
for _ in range(num_unique_orders):
    product_id.extend(np.random.choice(products["product_id"], size=4, replace=False))

# Price, quantity, and revenue
prices = np.random.randint(400, 801, size=num_rows)  # Price between 400-800
quantities = np.random.choice([1, 2, 3, 4], size=num_rows)  # Quantity of 1, 2, 3, or 4
revenues = prices * quantities  # Revenue = price * quantity

# Date - Random dates within the first 10 months of 2024
dates = pd.to_datetime(
    np.random.choice(pd.date_range("2024-01-01", "2024-10-31"), size=num_rows)
)

# Create the DataFrame
orders = pd.DataFrame({
    "order_id": order_ids,
    "product_id": product_id,
    "customer_id": customer_id,
    "price": prices,
    "quantity": quantities,
    "revenue": revenues,
    "date": dates
})

# Display the first few rows
# print(orders.head())

# Create an empty DataFrame by specifying column names
columns_sessions = ["session_id", "devicetype", "timeOnScreen", "pageview", "source"]

# Generate unique session_id
session_ids = np.random.choice(range(1000, 100000), size=50000, replace=False)

# Device type, source, time on screen, and page views
devicetype = np.random.choice(["Android", "iOS"], size=50000)
source = np.random.choice(["Meta", "Google", "Criteo", "Direct", "Tiktok", "Others"], size=50000)
timeOnScreen = np.random.randint(3, 300, size=50000)
pageview = np.random.randint(1, 15, size=50000)

# Populate the DataFrame
sessions = pd.DataFrame({
    "session_id": session_ids,
    "devicetype": devicetype,
    "pageview": pageview,
    "source": source,
    "timeOnScreen": timeOnScreen
})

# Display the first few rows
# print(sessions.head())

# Save DataFrames to CSV files
products.to_csv("products.csv", index=False)
customers.to_csv("customers.csv", index=False)
orders.to_csv("orders.csv", index=False)
sessions.to_csv("sessions.csv", index=False)
