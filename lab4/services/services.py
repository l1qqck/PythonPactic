from models import Car
from storage import Storage1
from exceptions import InvalidMileageError

import random
import string

def generateVIN():
	allowed_chars = string.ascii_uppercase.replace('I','')
	allowed_digits = string.digits
	return ''.join(random.choice(allowed_chars + allowed_digits) for _ in range(17))

def carToData(car : Car):
	return {"VIN": car._VIN,"brand": car._brand,"model": car._model,"year": car._year,"mileage": car._mileage,"price": car._price}
def dataToCar(data):
	return Car(data["VIN"], data["brand"], data["model"], data["year"], data["mileage"] , data["price"] )
def checkMileage(newMileage):
	try:
		newMileage = int(newMileage)
	except ValueError:
		raise InvalidMileageError("Пробег должен быть числом!!!")

	if newMileage < 0:
		raise InvalidMileageError("Пробег не может быть меньше 0!!!")

def addCar(car: Car):
	carData = carToData(car)
	Storage1.sendToStorage(carData)

class Service:

	@staticmethod
	def createCar():
		brand = input("Введите марку машины: ")
		model = input("Введите модель машины: ")
		try:
			year = int(input("Введите год машины: "))
		except ValueError:
			print("год - число!!!")
			return 
		

		try:
			mileage = int(input("Введите пробег машины: "))
		except ValueError:
			print("пробег - число!!!")
			return 
		
		try:
			price = int(input("Введите цену машины: "))
		except ValueError:
			print("цена - число!!!")
			return
		addCar(Car(generateVIN(),brand,model,year,mileage,price))
		
		

	@staticmethod
	def getCars():		
		allCars = Storage1.pullFromStorage()

		print("\nALL CARS : \n")
		for index,car in enumerate(allCars):
   			print(f"car {index} =", repr(car))

		return allCars 

	@staticmethod	
	def findCar():
		listOfFindedCars = Service.findCars()
		if len(listOfFindedCars ) > 0:
			return listOfFindedCars[0]


	@staticmethod
	def findCars():
		data = Storage1.pullFromStorage()
		listOfCars = []
		
		while True:
			print("1: VIN\n2: марка машины\n3: модель машины\n4: год выпуска\n5: пробег\n6: цена")
			status = input("Введите номер ключа: ")
			
			key = 0
			carKeys = ["VIN" , "brand" , "model" , "year" , "mileage" , "price"]
			
			match status:
				case "1": key = carKeys[0]
				case "2": key = carKeys[1]
				case "3": key = carKeys[2]
				case "4": key = carKeys[3]
				case "5": key = carKeys[4]
				case "6": key = carKeys[5]
				case _: 
					print("Такого ключа не существует")
					continue

			Service.getCars()			

			searchValue = input("Введите то что ищете: ")
			for car in data:
				if str(car[carKeys[int(status)]]) == searchValue:
					listOfCars.append(car)
				
			break	

			for car in listOfCars:
    				print("car =", repr(car))
    				print("-" * 20)

		return listOfCars

	@staticmethod
	def change_mileage(newMileage):
		try:
			checkMileage(newMileage)
		except InvalidMileageError:
			print("Ошибка, повторите ввод...")
			return Service.change_mileage(input("введите пробег: "))
		
		data = Service.getCars()

		
		try:
			number = int(input("Введите порядковый номер машины: "))
		except ValueError:
			print("введите число!!")
			return	
		try:
			data[number]['mileage'] = newMileage
		except IndexError:
			print("такого индекса нет!!")
			return

		Storage1.resetStorage(data)

		Service.getCars()
		
	@staticmethod
	def remove_car():
		data = Service.getCars()
		
		try:
			index = int(input("Введите порядковый номер машины"))
		except ValueError:
			print("порядковый номер должен быть числом!!")
			return removeCar()

		try:
			data.pop(index)
		except IndexError:
			print("такого индекса нет")
			return

		Storage1.resetStorage(data)
		
		print("НОВЫЙ СПИСОК МАШИН")
		Service.getCars()

		

			
		

		
		

		
						
			
			
					
					
					
					
	
