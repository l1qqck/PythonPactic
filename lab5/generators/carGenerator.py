import random
from models import Car

class carGenerator:
	carMarks = [
		"Toyota",
		"Honda",
		"Ford",
		"Chevrolet",
		"BMW",
		"Mercedes-Benz",
		"Audi",
		"Volkswagen",
		"Hyundai",
		"Kia",
		"Nissan",
		"Lexus",
		"Volvo",
		"Tesla",
		"Subaru",
		"Lada",
		"УАЗ",
		"ГАЗ",
		"Москвич",
		"Aurus"
		]

	carModels = [
		model 
		for model in range(20)
	]

	carYear = [
		year
		for year in range(1900, 2026)
	]

	carMileage = [mileage for mileage in range(0 , 10000)]

	carPrice = [300_000, 350_000, 400_000, 450_000, 500_000, 1_000_000]

	@staticmethod
	def getGen(list):
		while True:
			yield random.choice(list)

	@staticmethod
	def genCar():
		while True:
			yield Car(random.choice(carGenerator.carMarks),random.choice(carGenerator.carModels), random.choice(carGenerator.carYear) , random.choice(carGenerator.carMileage) , random.choice(carGenerator.carPrice))