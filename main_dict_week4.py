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
