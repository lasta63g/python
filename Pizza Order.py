print("--------------------MENU!---------------------")
print(" PIZZA                         S      M      L")
print("1. Margherita                 450    750    1,050")
print("2. Mushroom Pizza             550    850    1,150")
print("3. Pepperoni Pizza            550    850    1,150")
print("4. Chicken Pizza              650    950    1,250")
print("5. Tandoori Paneer Pizza      750    1,050  1,350")
print("4. Meat Lovers                850    1,150  1,450")

def take_order():
    while True:
        order =input("Place your order:").lower()
        if order in ["margherita", "mushroom pizza", "pepperoni pizza",
                        "chicken pizza", "tandoori paneer pizza", "meat lovers"]:
            break
        else:
            print("Invalid choice!")

    while True:
        size =input("Size? Small / Medium / Large:").lower()
        if size in ["small", "medium", "large"]:
            break
        else:
            print("Invalid size!")
        
    price=0
    if order.lower() == "margherita":
        if size.lower() == "small":
            price =450
        elif size.lower() == "medium":
            price= 750
        else:
            price = 1050
            
    elif order.lower() == "mushroom pizza" or order.lower == "pepperoni pizza":
        if size.lower() == "small":
            price =550
        elif size.lower() == "medium":
            price= 850
        else:
            price = 1150
            
    elif order.lower() == "chicken pizza":
        if size.lower() == "small":
            price =650
        elif size.lower() == "medium":
            price= 950
        else:
            price = 1250
            
    elif order.lower() == "tandori paneer pizza":
        if size.lower() == "small":
            price =750
        elif size.lower() == "medium":
            price= 1050
        else:
            price = 1350
            
    else :
        if size.lower() == "small":
            price =850
        elif size.lower() == "medium":
            price= 1150
        else:
            price = 1450

    quant= int(input("Please enter the quantity."))
    price = price*quant

    print("Extra Cheese : +70rs")
    cheese = input(" Would you like extra cheese?").lower()
    if cheese =="yes":
        price +=70*quant
    return price,quant,order
total=0
quantity=0
pizza=[]
while True:
    price, quant,order = take_order()  
    total += price
    quantity += quant
    pizza.append(order)
    another= input("Would you like to add another pizza? (yes/no):").lower()
    if another =="no":
        break
desc= input("Any customization? Please describe: ")
print("--------Your Order Details--------")
print(f"Total bill:{total}")
print("Items Ordered:")
for p in pizza:
    print("-", p)
print(f"Total Number of pizza: {quantity}")
print(f"Description: {desc}")


    




