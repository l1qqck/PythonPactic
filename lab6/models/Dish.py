from dataclasses import dataclass
from protocols import IPriceble

@dataclass
class Dish(IPriceble):	
	name: str
	price: float
	
	def get_type(self) ->str:
		return "блюдо"

	
		

	

    
