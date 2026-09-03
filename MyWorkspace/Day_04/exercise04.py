class ProductNotFoundError(Exception):pass
class OutOfStockError(Exception):pass
import copy
old_catalog = []

def process_order(catalog, order):
    global old_catalog
    price,old_catalog=0.0,copy.deepcopy(catalog)
    try:
        for key in order:
            if key in catalog:
                print(catalog)
                if catalog[key]['stock'] - order[key] >= 0:
                    catalog[key]['stock'] -= order[key]
                    price += order[key] * catalog[key]['price']
                else:
                    raise OutOfStockError(f"Product {key} is out of stock. Requested: {order[key]}, Available: {catalog[key]['stock']}.")
            else:
                raise ProductNotFoundError(f"Product {key} not found in store catalog.")
        print(catalog)
        return price
    except OutOfStockError:
        catalog = old_catalog
    
catalog = {
    "P01": {"price": 10.0, "stock": 5},
    "P02": {"price": 20.0, "stock": 10}
}

# 1. Successful Order
total = process_order(catalog, {"P01": 2, "P02": 1})
print(total)
# Returns: 40.0
# Catalog stock changes to: P01 stock = 3, P02 stock = 9

# 2. Failed Order (Triggers Rollback)
# Current Catalog: {"P01": {"price": 10.0, "stock": 3}, "P02": {"price": 20.0, "stock": 9}}
try:
    total = process_order(catalog, {"P01": 2, "P02": 15})
except OutOfStockError as e:
    print(e) # Output: Product 'P02' is out of stock. Requested: 15, Available: 9.

# Verify Catalog Stock: P01 must remain at 3 (NOT decreased to 1).
print(catalog["P01"]["stock"]) # Output: 3