import re
def process_dataset(dataset):
    result,output = [],[]
    for item in dataset:
        item_dict = dict()
        for data in item:
            
            if re.findall(r"^[A-Za-z]+$",data):
                item_dict["product"] = re.findall(r"^[A-Za-z]+$",data)[0]
                
            elif "Price" in re.split(r"(Price)[:\s]",data):
                item_dict["price"] = float(re.split(r"(Price)[:\s]",data)[-1])
                
            elif "Rating" in re.split(r"(Rating)[:\s.]",data):
                item_dict["score"] = float(re.split(r"(Rating)[:\s.]",data)[-1])
                
        result.append(item_dict)
        
    for item in filter(lambda x:x["price"]<1000,result):
        output.append(item)
    
    
    return output

            

data_input = [
    ("Laptop", "Price: 1200", "Rating: 4.8"),
    ("Phone", "Price: 800", "Rating: 4.5"),
    ("Mouse", "Price: 25", "Rating: 4.7"),
    ("Charger", "Price: 15", "Rating: 4.2")
]
print(process_dataset(data_input))