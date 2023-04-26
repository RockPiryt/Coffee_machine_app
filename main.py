#COFFEE MACHINE
resources = {
    "water": 100,
    "milk": 50,
    "coffee": 76,
    "money": 2.5,
}


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

def is_enough_resources(ingredients_user_coffee):
    '''Function checks if there are enough resources to make drink for user.If is enough return True.'''

    #enough ingredients to make coffee for user - 
    # looping for ingredient ('milk'/'water'/'coffee')
    for ingredient in ingredients_user_coffee:
        if resources[ingredient] >= ingredients_user_coffee[ingredient]:
            return True
    return False

turn_on = True
while turn_on is True:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        turn_on = False
    elif choice == 'report':
        print(f"Water = {resources['Water']} ml")
        print(f"Milk = {resources['Milk']} ml")
        print(f"Coffee = {resources['Coffee']} g")
        print(f"Money = {resources['Money']} $")
    else:
        #eg.user choose latte - string 'latte' is used as key in menu dict
        user_drink = MENU[choice]#"latte"
        if is_enough_resources(user_drink["ingredients"]) is True:
            print('In machine there is enough ingredients to make your coffee. The machine will prepare a drink for you.')
        else:
            print('Sorry in the machine is not enough water or coffee or milk to prepare your drink')
