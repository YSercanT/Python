class coffeeMachine:
    def __init__(self):
        self.MENU = {
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

        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.profit = 0
        self.total=0

    def get_resources(self):
        return self.resources
    def update_resources(self,water=300,milk=200,coffee=100):
        self.resources["water"] = water
        self.resources["milk"] = milk
        self.resources["coffee"] = coffee
    def make_coffee(self,drink_name, order_ingredients):
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name} ☕️. Enjoy!")
    def is_transaction_successful(self,money_received, drink_cost):
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change.")
            global profit
            self.profit=self.profit
            self.profit += drink_cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False
    def process_coins(self):
        print("Please insert coins.")
        self.total = int(input("how many quarters?: ")) * 0.25
        self.total += int(input("how many dimes?: ")) * 0.1
        self.total += int(input("how many nickles?: ")) * 0.05
        self.total += int(input("how many pennies?: ")) * 0.01
        return self.total
    def is_resource_sufficient(self,order_ingredients):
        for item in order_ingredients:
            if order_ingredients[item] > self.resources[item]:
                print(f"​Sorry there is not enough {item}.")
                update=input("Do you want to update resources (Y/N):").lower()
                if update == "y":
                    self.update_resources()
                    print("The resources have been updated.")
                    return True
                else: 
                    print("We wish you a good day.")
                    return False
        return True
    def start(self):
        is_on = True

        while is_on:
            choice = input("​What would you like? (espresso/latte/cappuccino): ")
            if choice == "off":
                is_on = False
            elif choice == "report":
                print(f"Water: {self.resources['water']}ml")
                print(f"Milk: {self.resources['milk']}ml")
                print(f"Coffee: {self.resources['coffee']}g")
                print(f"Money: ${self.profit}")
            else:
                drink = self.MENU[choice]
                if self.is_resource_sufficient(drink["ingredients"]):
                    payment = self.process_coins()
                    if self.is_transaction_successful(payment, drink["cost"]):
                        self.make_coffee(choice, drink["ingredients"])

    def __main__(self):
        self.start()

coffee_machine = coffeeMachine()
coffee_machine.__main__()

       

        