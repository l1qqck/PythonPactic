from protocols import IPriceble
from dataclasses import dataclass

@dataclass
class Drink(IPriceble):
	name: str
	price: float
	def get_type(self) ->str:
		return "напиток"