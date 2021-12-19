import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 40,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 55,
    }
}
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def sufficient_resources(choice):
    for item in choice:
        if choice[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def total_cost():
    print("Insert Coins please.")
    total = int(input("Insert ₹10 coins: "))*10
    total += int(input("Insert ₹5 coins: ")) * 5
    total += int(input("Insert ₹2 coins: ")) * 2
    total += int(input("Insert ₹1 coins: ")) * 1
    return total

def success_money(given_cost, coffee_cost):
    global profit
    profit += given_cost-coffee_cost
    if given_cost < coffee_cost:
        print(f"The given amount is not sufficient for '{choice}' it is of ₹{coffee_cost}.\nPayment is Refunded")
        return False
    print(f"Here is your change ₹{given_cost - coffee_cost}.")
    return True

def coffee_serve(resource):
    for item in resource:
        resources[item] -= resource[item]
    print(f"Here is your ☕{choice}")


while True:
    choice = input("What would you like? (espresso/latte/cappuccino) :")
    if choice == "off":
        sys.exit()
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ₹{profit}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        if sufficient_resources(drink["ingredients"]):
            payment = total_cost()
            if success_money(payment, drink["cost"]):
                coffee_serve(drink["ingredients"])
    else:
        print("Choose Valid Coffee")