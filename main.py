import pandas

#COFFEE MACHINE
resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 250,
    "money": 10,
}

profit = 0

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



report = {
    'type coffee': ['espresso', 'latte', 'cappuccino'],
    'amount': [0, 0, 0],
    'profit': [0, 0, 0],
}


def save_report():
    '''Function generate csv file with report wit information about profit and amount of each type of coffee'''

    # create DateFrame from dict
    report_df = pandas.DataFrame(report)
    print(report_df)
    report_df.to_csv('report_data.cvs')



#ingredients_user_coffee = user_drink["ingredients"]
def make_coffee(ingredients_user_coffee, resources, choice):


    print(f'{choice} is made of: {ingredients_user_coffee}')#{'water': 200, 'milk': 150, 'coffee': 24}
    print(f'Machine resources before making drink: {resources}')

    # #new_dict={new_key:new_value for (key/value) in dict.items() if test}
    # update_resource = {key:resources[key] - value for key, value in ingredients_user_coffee.items() }

    for key, value in ingredients_user_coffee.items():
        resources[key]-=ingredients_user_coffee[key]

    print(f'Machine resources after making drink:{resources}')
    print(f'Here is your prepared drink ☕')
    if choice == 'espresso':
        report['amount'][0] += 1
        report['profit'][0] += 1.5
    elif choice == 'latte':
        report['amount'][1] += 1
        report['profit'][1] += 2.5
    elif choice == 'cappuccino':
        report['amount'][2] += 1
        report['profit'][2] += 3





def calculate_coins(drink_cost):
    '''Function to process coins. It checks that value of the coins is enough to buy a user_drink. If it is enough return True'''
    money_in_machine = resources["money"]
    print(f'In the machine are: {money_in_machine}$')
    sum_coins = 0
    is_enough_money = False
    while is_enough_money is False:
        #ask user to continue
        question_user = input(f"Type 'yes' to add coins or 'cancel' to cancel operation: ")

        if question_user == 'cancel':
            print(f'You cancel the operation. Your inserted money: {sum_coins} will be returned.')
            return True
        
        #ask user to insert coins
        quarter = input('how many quarter you insert?: ')
        dimes = input('how many dimes you insert?: ')
        nickel = input('how many nickel you insert?: ')
        pennies = input('how many pennies you insert?: ')

        #calculate value of inserted coins
        total = 0
        quarter_coins = int(quarter) * 0.25
        dimes_coins =  int(dimes) * 0.1
        nickel_coins = int(nickel) * 0.05
        pennies_coins =  int(pennies) * 0.01

        total = round(quarter_coins + dimes_coins + nickel_coins + pennies_coins, 2)
        
        #add value of added coins if value is insufficient
        sum_coins += total

        #check that value of inserted coins is enough to buy drink
        if sum_coins >= drink_cost:
            print(f'You insert: {round(sum_coins,2)}$.')
            #get change if too much coins
            if sum_coins > drink_cost:
                change = sum_coins-drink_cost
                print(f'You insert to much coins for this drink. Drink cost {drink_cost}$. Here is your change {round(change,2)}$.')

            global profit
            profit+=drink_cost
            money_in_machine += profit
            print(f'In the machine are: {money_in_machine}$')
            print('You insert enough money for drink. Machine will prepare your drink.')

            return True
        else:
            print(f'You add: {total}$.')
            print(f'Total value: {round(sum_coins,2)}$.')



def is_enough_resources(ingredients_user_coffee):
    '''Function checks if there are enough resources to make drink for user.If it is enough return True.'''

    #enough ingredients to make coffee for user - 
    # looping for ingredient ('milk'/'water'/'coffee')
    for ingredient in ingredients_user_coffee:
        if resources[ingredient] >= ingredients_user_coffee[ingredient]:
            return True
    return False

turn_on = True
while turn_on is True:
    choice = input('What would you like? (espresso/latte/cappuccino): ')#latte
    if choice == 'off':
        turn_on = False
    elif choice == 'resources':
        print(f"Water = {resources['water']} ml")
        print(f"Milk = {resources['milk']} ml")
        print(f"Coffee = {resources['coffee']} g")
        print(f"Money = {resources['money']} $")
    elif choice == 'report':
        save_report()
        print('Coffee information were generated in csv_file.')
    else:
        #eg.user choose latte - string 'latte' is used as key in menu dict
        user_drink = MENU[choice]#{'ingredients': {'water': 200, 'milk': 150, 'coffee': 24}, 'cost': 2.5}
        if is_enough_resources(user_drink["ingredients"]) is True:
            print(f'You choose: {choice}. In the coffee machine there is enough ingredients to make your coffee.')

            drink_cost = user_drink['cost']#2.5
            print(f'Your drink {choice} cost: {drink_cost}$. Please insert appropriate value of money for your drink.')
            # calculate_coins(drink_cost)

            if calculate_coins(drink_cost) is True:
                make_coffee(user_drink["ingredients"], resources, choice)
        else:
            print('Sorry in the machine is not enough water or coffee or milk to prepare your drink')
