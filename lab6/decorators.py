import time
from models import *
from functools import wraps


def log(func):
	@wraps(func)
	def wrapper( *args , **kwargs ):
		print(f"Вызов функции {func.__name__}")
		start = time.perf_counter()
		return func(*args,**kwargs)
		end = time.perf_counter()
		print(f"Функция {func.__name__} выполнилась за {(end - start):.6f}")
	return wrapper

def log_status_change(func):
	def wrapper(self , new_status : OrderStatus):
		print(f"Старый статус заказа: {self.status}")
		result = func(self , new_status)
		print(f"Новый статус заказа: {self.status}")
		return result
	return wrapper