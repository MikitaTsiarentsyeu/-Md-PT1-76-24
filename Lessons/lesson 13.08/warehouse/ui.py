import bl

def get_all():
    res = bl.get_all()
    if res:
        print(res)
    else:
        print("no products detected")

def get():
    name = input("enter product name:\n")
    res = bl.get(name)
    if res:
        print(res)
    else:
        print("no product detected by this name")

def add():
    product = {}
    for attr in bl.product_attrs:
        product[attr] = input(f"enter product {attr}:")
    bl.add(**product)

def main_menu():
    while True:
        action = input("""choose an action number:
            1. get all products
            2. get a product by name
            3. add new product
            4. exit\n """)
        
        if action[0] == "1":
            get_all()
        elif action[0] == "2":
            get()
        elif action[0] == "3":
            add()
        elif action[0] == "4":
            exit()
        else:
            print("please choose from the action numbers only")

main_menu()