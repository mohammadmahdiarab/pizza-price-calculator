pizza_size = input("Choose Pizza Size[ S , M , L ]: ").upper()
pepperoni = input("pepperoni [ N , Y ]: ").upper()
extra_cheese = input("extra Cheese [ N , Y ]: ").upper()

match pizza_size :
    case "S":
        more_pepperoni = 20
        pizza_price = 70
    case "M":
        pizza_price = 70
        more_pepperoni = 30
    case "L":
        pizza_price = 70
        more_pepperoni = 40
    case _:
        print("Invalid Pizza")

Total = pizza_price
if pepperoni == "Y":
    Total += more_pepperoni
if extra_cheese == "Y":
    Total += 30

print(f"Total Price: {Total}")