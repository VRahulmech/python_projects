import data


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino): "
def ask_for_drink():
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    return drink


# TODO: 2. Turn off the Coffee Machine by entering “off ” to the prompt.
# TODO: 3. Print report.
def print_report():
    print(data.resources)


# TODO: 4. Check resources sufficient
def check_resources(drink):
    for ingredient in data.MENU[drink]["ingredients"].keys():
        if data.MENU[drink]["ingredients"][ingredient] <= data.resources[ingredient]:
            continue
        else:
            print(f"Sorry! There is not enough {ingredient}")
            return False
    return True


# TODO: 5. Process coins.
def process_coins():
    print('Insert the coins: ')
    quart = int(input("number of quarters: "))
    dimes = int(input("number of dimes: "))
    nickles = int(input("number of nickles: "))
    pennies = int(input("number of pennies: "))
    return quart*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01


# TODO: 6. Check transaction successful?
def check_transaction(amount, cost):
    if amount < cost:
        print(f'sorry! insufficient amount. Refunding {amount}')
        return False
    elif amount > cost:
        print(f"Transaction successful. Please collect {amount - cost}")
        # data.Money += cost
        return True
    else:
        print("Transaction Successful")
        # data.Money += cost
        return True


def make_transaction(drink):
    for ingredient in data.MENU[drink]['ingredients'].keys():
        data.resources[ingredient] -= data.MENU[drink]['ingredients'][ingredient]



# TODO: 7. Make Coffee.
def make_coffee():
    while True:
        drink = ask_for_drink()
        if drink  =='off':
            return

        elif check_resources(drink) \
                and check_transaction(process_coins(), data.MENU[drink]["cost"]):
            print(f"report before purchasing {drink}:")
            print_report()
            make_transaction(drink)
            print(f"report after purchasing {drink}:")
            print_report()


make_coffee()



