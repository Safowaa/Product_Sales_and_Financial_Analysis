import pandas as pd

# Dictionary list
azubi_store = [
    {"Product_id":23, "name":"Computer","wholesale_Price":500, "retail_price":1000, "sales":100},
    {"Product_id":96, "name":"Python Workout","wholesale_Price":35, "retail_price":75, "sales":1000},
    {"Product_id":97, "name":"Pandas Workout","wholesale_Price":35, "retail_price":75, "sales":500},
    {"Product_id":15, "name":"Banana","wholesale_Price":0.5, "retail_price":1, "sales":200}, 
    {"Product_id":87, "name":"Sandwich","wholesale_Price":3, "retail_price":5, "sales":300} 
]

# Create the dataframe from the dictionary above
df = pd.DataFrame(azubi_store)
df

# profit for each product

df["net_revenue_per_product"] = (df["retail_price"] - df["wholesale_Price"]) * df["sales"]
df   

# How much total net revenue from all sales

total_net_revenue = df["net_revenue_per_product"].sum()
total_net_revenue

# what product is product retail price more than twice the wholesale price?

wp = df["wholesale_Price"] * 2 
product = df[df["retail_price"] >= wp]
product


# food vs computers vs books
# food
ba_sa = df[df["name"].str.contains("Banana|Sandwich")] 
food = ba_sa["sales"].sum()

# computers
com = df[df["name"].str.contains("Computer")]
computers = com["sales"].sum()

# books
bo = df[df["name"].str.contains("Python Workout|Pandas Workout")]
books = bo["sales"].sum()

print(f'Total sales for food is ${food}')
print(f'Total sales for computer is ${computers}')
print(f'Total sales for books is ${books}')

# 30% discount negotation on wholesale_price

df["Discount"] = df["wholesale_Price"] * 0.3
df["Discount"] 
df


# Government imposed tax of 15%, 20% and 25% 

df["Tax15%"] = df["net_revenue_per_product"] * 0.15
# df["Discount15"] 

df["Tax20%"] = df["net_revenue_per_product"] * 0.2
# df["Discount20%"] 

df["Tax25%"] = df["net_revenue_per_product"] * 0.25
# df["Discount25%"] 

df

# how much less you will net with each tax amount
# where nrpp stands for net_revenue_per_product

df["loss_at15%"] = df["net_revenue_per_product"] - df["Tax15%"]

df["loss_at20%"] = df["net_revenue_per_product"] - df["Tax20%"]

df["loss_at25%"] = df["net_revenue_per_product"] - df["Tax25%"]

df

import matplotlib.pyplot as plt

# Create a new figure and set its size
plt.figure(figsize=(10, 6))

# Bar chart for net revenue per product before tax
plt.bar(df['name'], df['net_revenue_per_product'], label='Net Revenue')

# Stacked bars for each tax scenario
plt.bar(df['name'], df['loss_at15%'], label='Net after 15% Tax', color='red', alpha=0.6)
plt.bar(df['name'], df['loss_at20%'], label='Net after 20% Tax', color='blue', alpha=0.6)
plt.bar(df['name'], df['loss_at25%'], label='Net after 25% Tax', color='green', alpha=0.6)

plt.xlabel('Product')
plt.ylabel('Revenue ($)')
plt.title('Revenue and Tax Impact Visualization')
plt.legend()

plt.xticks(rotation=45)  # Rotate product names for better visibility
plt.tight_layout()
plt.show()


import seaborn as sns

# Create a DataFrame to hold summary data
category_sales = pd.DataFrame({
    'Category': ['Food', 'Computers', 'Books'],
    'Sales': [food, computers, books]
})

# Create a bar plot
plt.figure(figsize=(8, 5))
sns.barplot(x='Category', y='Sales', data=category_sales, palette='viridis')

plt.title('Product Category Sales Visualization')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.show()
