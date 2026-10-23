from protocols import IPriceble
from models import Dish
from enum import Enum
import decorators

class OrderStatus(Enum):
	accepted = "принят"
	diagnosed = "диагностируется"
	repaired = "ремонтируется"
	ready = "готов"
	cancelled = "отменен"


class Order:
	nextId = 1
	dish_popularity = {}

	def __init__(self):
		self.orderId = Order.nextId
		Order.nextId +=1
		self.items : list[Priceble] = []
		self.status : OrderStatus = OrderStatus.accepted

	def __repr__(self) -> str:
		lines = [f"Заказ с номером: {self.orderId} {self.status}"]
		for item in self.items:
			lines.append(f"{item.get_type()} : {item.name} , цена: {item.price}")
		lines.append(f"Стоимость заказа: {sum(item.price for item in self.items)}")
		return "\n".join(lines)

	def add_item(self , *items: IPriceble) -> None:
		for item in items:
			
			if self.status == OrderStatus.cancelled :
				raise RuntimeError("Нельзя добавить блюдо в отменённый заказ")
			if not isinstance(item, IPriceble):
				raise ValueError("нельзя добавлять в заказ другие предметы , кроме напитков и блюд")
			print(type(item))
			if isinstance(item, Dish.Dish):
				if item.name in Order.dish_popularity:
					Order.dish_popularity[item.name] += 1
				else:
					Order.dish_popularity[item.name] = 1
			self.items.append(item)

	def set_status(self , new_status : OrderStatus) -> None:
		self.status = new_status

	

		
				
		
	

