from models import *

def most_popular_dishes():
	return sorted(Order.dish_popularity, key=Order.dish_popularity.get, reverse=True)[:3]
		
		
	