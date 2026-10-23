from functools import reduce

class ProcFunc:
	@staticmethod
	def filter_objects( objects, predicate):
		return list(filter( predicate , objects ))
		
	@staticmethod
	def find_object_with_MaxPrice( objects ):
		return reduce( lambda object , nextObject : object if object.price > nextObject.price else nextObject , objects)
		
	@staticmethod
	def if_more_year( objects , year ):
		return any( object.year > year for object in objects )

	@staticmethod
	def get_models(objects):
		return map( lambda object: object.model , objects )

	@staticmethod
	def sort_objects(objects, key_function):
		return sorted( objects , key= key_function , reverse= True )