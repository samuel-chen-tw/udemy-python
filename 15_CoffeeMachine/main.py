from data import MENU, resources

off_machine = False
earn = 0
machine_resources = resources


def report():
    print(f"Water: {machine_resources['water']}ml")
    print(f"Milk: {machine_resources['milk']}ml")
    print(f"Coffee: {machine_resources['coffee']}g")
    print(f"Money: ${earn}")


def check_resources(coffee):
    for item in coffee:
        if coffee[item] > machine_resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def count_coins():
    total_coins = int(input("How many quarters?: ")) * 0.25
    total_coins += int(input("How many dimes?: ")) * 0.10
    total_coins += int(input("How many nickles?: ")) * 0.05
    total_coins += int(input("How many pennies?: ")) * 0.01
    return round(total_coins, 3)


def check_money(total_insert_coins, action):
    if total_insert_coins >= MENU[action]['cost']:
        if total_insert_coins > MENU[action]['cost']:
            change = total_insert_coins - MENU[action]['cost']
            print(f"Here is ${round(change, 3)} dollars in change.")
        return True
    else:
        return False


def make_coffee(coffee, machine_resources):
    for item in coffee:
        machine_resources[item] -= coffee[item]
    print("Here is your latte. Enjoy!")
    return machine_resources


while not off_machine:
    action = input("What would you like? (espresso,latte,cappuccino): ")

    if action == "off":
        off_machine = True
    elif action == "report":
        report()
    elif action != "espresso" and action != 'latte' and action != 'cappuccino':
        print("Input Error! please try it again.")
    elif check_resources(MENU[action]['ingredients']):
        print("Please insert coins.")
        total_insert_coins = count_coins()
        if check_money(total_insert_coins, action):
            earn += MENU[action]['cost']
            machine_resources = make_coffee(MENU[action]['ingredients'], machine_resources)
        else:
            print("Sorry that's not enough money. Money refunded.")
