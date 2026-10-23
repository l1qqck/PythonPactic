from operations import ProcFunc
from models import Car
from generators import carGenerator

def printList(list):
	for object in list:
		print(object)

carGen = carGenerator.genCar()

listOfCars = [next(carGen) for i in range(5)]

print("\nВСЕ\n")
printList(listOfCars)

print("\nОТФИЛЬТРОВАННЫЕ\n")
predicat = Car.make_price_predicate(0 , 490000)
filteredPriceCars = ProcFunc.filter_objects( listOfCars , predicat )
printList(filteredPriceCars)

print("\nМОДЕЛИ\n")
listOfModels = ProcFunc.get_models(listOfCars)
printList(listOfModels)

print("\nОТСОРТ_ПРОБЕГ\n")
sortedByBalance = ProcFunc.sort_objects(listOfCars, lambda car: car.mileage)
printList(sortedByBalance)

print("\nСАМЫЙ_ДОРОГОЙ\n")
maxPriceCar = ProcFunc.find_object_with_MaxPrice(listOfCars)
print(maxPriceCar)

print("\nСТАРШЕ_ЕСТЬ?\n")
isOlder = ProcFunc.if_more_year(listOfCars , 2002)
print(isOlder)



