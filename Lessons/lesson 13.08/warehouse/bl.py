import math

products = [
    {
        "name":"adidas superstar", 
        "descr":"test descr", 
        "brand":"adidas", 
        "price":100
    }
]

product_attrs = list(products[0].keys())

def get_all():
    res = ""
    if products:
        for p in products:
            res = f"{res} {product_to_str(p)}\n"
        return res.rstrip()
    return

def get(name):
    for p in products:
        if p["name"] == name:
            return product_to_str(p)

def add(**product):
    products.append(product_from_str(**product))

def product_to_str(product):
    res = ""
    for key in product:
        res = f"{res} {key}:'{product[key]}'"
    return res.lstrip()

def product_from_str(**kwargs):
    product = {}
    for key in product_attrs:
        if key == "price":
            try:
                product[key] = float(kwargs[key])
            except ValueError:
                product[key] = math.nan
            break
        product[key] = kwargs[key]
    return product


if __name__ == "__main__":
    # print(get("adidas superstar"))
    print(get_all())