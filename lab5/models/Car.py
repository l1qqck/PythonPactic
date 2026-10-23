import math

class Car:
	def __init__(self, brand , model , year , mileage , price):
		self.brand = brand
		self.model = model
		self.year = year
		self.mileage = mileage
		self.price = price
	
	def __repr__(self):
		return f" марка = {self.brand} , модель = {self.model} , год = {self.year} , пробег = {self.mileage} , цена = {self.price}"
	
	@staticmethod
	def make_price_predicate(min_value, max_value):
		def predicate(car):
			return min_value <= car.price < max_value
		return predicate