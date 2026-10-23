from models import Order, OrderStatus

class OrderContextManager:
	def __init__(self, order: Order):
		self.order = order

	def __enter__(self):
		if self.order.status == OrderStatus.accepted:
			self.order.set_status(OrderStatus.diagnosed)
		return self.order

	def __exit__(self , exc_type , exc_val ,traceback) -> bool:
		if exc_type is not None:
			self.order.set_status(OrderStatus.repaired)
			print(f"Заказ {self.order.status}")
			self.order.set_status(OrderStatus.cancelled)
			print(f"Заказ {self.order.status}")
			#return True

		print(f"Заказ {self.order.orderId} завершен")
		#return False