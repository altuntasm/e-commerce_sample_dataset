import pandas as pd
import numpy as np

# Kolon isimlerini belirleyerek boş bir DataFrame oluşturma
columns_products = ["product_id", "stock", "maincategory"]

# Benzersiz product_id oluşturma
product_ids = np.random.choice(range(1000, 10000), size=5000, replace=False)

# Stok sayısı ve kategori
stocks = np.random.randint(20, 101, size=5000)
categories = np.random.choice(["Abaya", "Shawl", "Tunic", "Shoes", "Bags", "Skirt"], size=5000)

# DataFrame'i doldurma
products = pd.DataFrame({
    "product_id": product_ids,
    "stock": stocks,
    "maincategory": categories
})

# İlk birkaç satırı görüntüleme
# print(products.head())

# Kolon isimlerini belirleyerek boş bir DataFrame oluşturma
columns_customers = ["customer_id", "name", "country","segment","e-mail"]

# Benzersiz customer_id oluşturma
customer_ids = np.random.choice(range(10000, 20000), size=2000, replace=False)

# name, country, segment
name = np.random.choice(["Ayse", "Zeynep", "Hilal", "Asena", "Nazli", "Betul", "Heba", "Angela", "Doga", "Deniz",
                         "Melek", "Sinem", "Ali", "Akif" , "Mehmet"], size=2000)
country = np.random.choice(["1", "2", "3", "4", "5", "6"], size=2000)
segment = np.random.choice(["Churn", "Likelihood to Churn", "Silver" , "Gold", "Elite"], size=2000)

# E-posta alanını name ve customer_id kullanarak oluşturma
emails = [f"{name.lower()}{cid}@vuhuv.com" for name, cid in zip(name, customer_ids)]

customers = pd.DataFrame({
    "customer_id": customer_ids,
    "name": name,
    "country": country,
    "segment": segment,
    "e-mail": emails
})

# İlk birkaç satırı görüntüleme
# print(customers.head())


# Toplam satır sayısı ve tekrar edecek order_id sayısı
num_rows = 40000
num_unique_orders = 10000  # Tekrar eden order_id sayısı

# order_id ve customer_id oluşturma
order_ids = np.repeat(np.random.choice(range(101000, 199000), size=num_unique_orders, replace=False), 4)
customer_id = np.repeat(np.random.choice(customers["customer_id"], size=num_unique_orders, replace=True), 4)

# Farklı product_id değerlerini seçip aynı order_id içinde benzersiz olacak şekilde ayarlama
product_id = []
for _ in range(num_unique_orders):
    product_id.extend(np.random.choice(products["product_id"], size=4, replace=False))

# Fiyat, miktar ve gelir
prices = np.random.randint(400, 801, size=num_rows)  # 400-800 arasında fiyat
quantities = np.random.choice([1, 2, 3, 4], size=num_rows)  # 1, 2, 3 veya 4 miktar
revenues = prices * quantities  # Gelir = fiyat * miktar

# Tarih - 2024 yılının ilk 10 ayı içerisinden rastgele tarihler
dates = pd.to_datetime(
    np.random.choice(pd.date_range("2024-01-01", "2024-10-31"), size=num_rows)
)

# DataFrame'i oluşturma
orders = pd.DataFrame({
    "order_id": order_ids,
    "product_id": product_id,
    "customer_id": customer_id,
    "price": prices,
    "quantity": quantities,
    "revenue": revenues,
    "date": dates
})

# İlk birkaç satırı görüntüleme
#print(orders.head())


# Kolon isimlerini belirleyerek boş bir DataFrame oluşturma
columns_sessions = ["session_id", "devicetype", "timeOnScreen", "pageview", "source"]

# Benzersiz session_id oluşturma
session_ids = np.random.choice(range(1000, 100000), size=50000, replace=False)

# Stok sayısı ve kategori

devicetype = np.random.choice(["Android", "iOS"], size=50000)
source = np.random.choice(["Meta", "Google", "Criteo", "Direct", "Tiktok", "Others" ], size=50000)
timeOnScreen =  np.random.randint(3, 300, size=50000)
pageview = np.random.randint(1, 15, size=50000)

# DataFrame'i doldurma
sessions = pd.DataFrame({
    "session_id": session_ids,
    "devicetype": devicetype,
    "pageview": pageview,
    "source": source,
    "timeOnScreen": timeOnScreen
})

# İlk birkaç satırı görüntüleme
# print(sessions.head())



products.to_csv("products.csv", index=False)
customers.to_csv("customers.csv", index=False)
orders.to_csv("orders.csv", index=False)
sessions.to_csv("sessions.csv", index=False)





