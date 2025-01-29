filtred_list = [num for num in [3,7,2,8,4,9,12] if num%2==0]
upper_case=[name.upper() for name in ["alice", "Bob", "charlie"]]
power2=[num**2 for num in range(1,11) ]
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30},
]
users=[person['name'] for person in users if person['age']>18]
passwords=["qwerty", "Illusion", "123Oo4", "SafePass"]
filtered_passw=[password for password in passwords if not any(char in password for char in ['O','o','i','I'])]
a=[" Data Science ", "PYTHON ", " maChine learning"]
a=[b.strip().lower() for b in a]
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 900},
]
products=[product['name'] for product in products if product['price'] <1000]
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
person =[{k:v for k,v in zip(keys,values)}]
name,age,city=input('Enter: name,age,city with comma: ').split(',')
user=[
    {'name':name,'age':age,'city':city}
    ]
import json
with open('json.json', 'w') as file:
    json.dump(user,file,indent=4)
with open('json.json', 'r') as file:
    loaded_data= json.load(file)
print(loaded_data)
print(user)