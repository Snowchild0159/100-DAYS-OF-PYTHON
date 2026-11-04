from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True



while is_on:
   option = menu.get_items()
   order = input(f"what do you want to order {option}?")
   if order == "off":
        is_on = False
   elif order == "report":
       coffee_maker.report()
       money_machine.report()
   else:
       drink = menu.find_drink(order)
       if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
               coffee_maker.make_coffee(drink)
 























# is_on = True
# while is_on:
#     option = menu.get_items()
#     order = input(f"what do you want to order {option}?")
#     if order == "off":
#         is_on = False
#     elif order == "report":
#         report = coffee_maker.report()
#         print(report) 
#     elif order == option and coffee_maker.is_resource_sufficient(order):
#         money_machine.make_payment(order)
#         CoffeeMaker.make_coffee(order)
#         print(money_machine.report())
