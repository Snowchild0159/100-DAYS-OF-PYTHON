from data import MENU, resources, COINS
from art import logo

print(logo)

turn_on = True

def check_resources(order):
    for item in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][item] > resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
            
        
    return True

def process_coins():
    print("Please insert coins.")
    total = 0
    for coin in COINS:
        count = int(input(f"How many {coin}?: "))
        total += count * COINS[coin]
        print(f"Total inserted: ${total:.2f}")
    return total
while turn_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "off":
        turn_on = False
        print("Turning off the coffee machine. Goodbye!")
        
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']:.2f}")


    elif order in MENU:
        if check_resources(order):
            payment = process_coins()
            cost = MENU[order]["cost"]
            if payment >= cost:
                change = payment - cost
                resources["money"] += cost
                for item in MENU[order]["ingredients"]:
                    resources[item] -= MENU[order]["ingredients"][item]
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {order}. Enjoy!")
             
            else:
                print("Sorry that's not enough money. Money refunded.")
        
    else:
        print("Invalid input. Please try again.")