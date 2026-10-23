from models import *
import services

order = Order()

dish = Dish("napoleon",200)
dish1 = Dish("polen",500)
dish2 = Dish("fapolento",200)
dish3 = Dish("duglas",150)
drink = Drink("seksPlyash", 350)
print(type(dish))
order.add_item(dish,drink,dish1, dish, dish2, dish2 , dish2, dish3, dish3, dish3)

print(order)

print(services.most_popular_dishes())