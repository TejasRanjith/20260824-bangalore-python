import re
def process_dataset(dataset):
    for item in dataset:
        for data in item:
            m = re.search(r"[A-Za-z]+",data)
            print(m.groups())
            
            

data_input = [
    ("Laptop", "Price: 1200", "Rating: 4.8"),
    ("Phone", "Price: 800", "Rating: 4.5"),
    ("Mouse", "Price: 25", "Rating: 4.7"),
    ("Charger", "Price: 15", "Rating: 4.2")
]
process_dataset(data_input)