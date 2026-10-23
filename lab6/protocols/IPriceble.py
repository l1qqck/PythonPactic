from typing import Protocol, runtime_checkable

@runtime_checkable
class IPriceble(Protocol):
	name: str
	price: float
	
	def get_type(self) ->str:
		...