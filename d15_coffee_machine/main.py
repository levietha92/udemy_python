# procedure programming style --> noodle

import menu

resources = menu.resources
menu = menu.MENU
resource_list = ['water', 'milk', 'coffee']
choice_list = ['espresso', 'latte', 'cappuccino']

# setting variables
coin_bal = 0
continued = True
sufficient_bal = True

water_bal = int(resources['water'])  # initial balance of inventory
milk_bal = int(resources['milk'])
coffee_bal = int(resources['coffee'])


# report balance func
def report():
    for item in resources:
        print(f"{item}: {resources[item]} ml left")


# insert coins func
def insert_coins(choice):
    """
    A function that informs the buy of the coffee cost and ask for coin inserts
    Return: total coin inserted
    """
    global continued, coin_bal, sufficient_bal

    cost = float(menu[choice]['cost'])

    if continued == True and sufficient_bal == True:
        print(f"Your coffee will cost {cost}")
        total = int(input("Please insert quarters ")) * 0.25
        total += int(input("Please insert dimes ")) * 0.1
        total += int(input("Please insert nickles ")) * 0.05
        total += int(input("Please insert pennies ")) * 0.01

        if total < cost:
            print("You are too broke for coffee")
            continued = False
        else:
            returns = total - cost
            print(f"Here is your returns {returns}")
            coin_bal += cost

    return coin_bal


# check sufficient stock before charging money
def check_inventory(choice):
    """
    A function that check the order's required resources against the inventory balance
    if sufficient resource it continues
    return "continued" true or false
    """
    global sufficient_bal
    if water > water_bal or milk > milk_bal or coffee > coffee_bal:
        print("We are out of stock, please refill inventory")
        # refill = bool(input("Do you want to refill now? "))
        # if refill == True:
        #     refill_inv()
        #     sufficient_bal = True
        # else:
        #     sufficient_bal = False
    else:
        sufficient_bal = True

    return sufficient_bal

def refill_inv():
    global water_bal, milk_bal, coffee_bal, sufficient_bal, continued
    if sufficient_bal == False:
        water_bal += 200
        milk_bal += 200
        coffee_bal += 100
        print("Your inventory has been refilled!")
        sufficient_bal = True
    return sufficient_bal

# make coffee
def make_coffee(choice):
    """
    A function that will deduct the resources balance if it makes coffee
    Return continued
    """
    global continued, water_bal, milk_bal, coffee_bal, sufficient_bal

    if continued == True and sufficient_bal == True:
        water_bal -= water
        milk_bal -= milk
        coffee_bal -= coffee
        print("Here is your coffee, enjoy!")
        continued = bool(input("Do you want another cup? True/False..."))
    return continued


"""
turn on coffee machine
ask and choose coffee 
check if enough resource to make said coffee
- if not --> stop --> turn off
- if yes --> continue
inform of cost
insert coins
check if coins inserted are enough
- if not --> inform and return coins
- if = --> proceed to make coffee and +total coins
- if > --> return coins and proceed to make coffee and +total coins
make coffee
- deduct resources
- return coffee
- continue turn on mode and ask again
"""

while continued == True and sufficient_bal == True:
    choice = input("Choose your coffee...")
    if choice in choice_list:
        resources = menu[choice]['ingredients']
        # inventory required
        water = int(resources['water'])
        milk = int(resources['milk'])
        coffee = int(resources['coffee'])

        check_inventory(choice)
        insert_coins(choice)
        make_coffee(choice)

    else:
        report()
        print("We don't have that order on the menu")
        print(f"Please choose from this list {choice_list}")
