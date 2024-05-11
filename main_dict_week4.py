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