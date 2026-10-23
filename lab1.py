def calculate_fuel_consumption_100km(length,fuelConsumption):
	return (fuelConsumption/length)* 100

def calculate_average_consumtion(list_fuel_consumption ):
	total = 0
	for trip_fuel_consumption in list_fuel_consumption :
		total += trip_fuel_consumption
	return total / len(list_fuel_consumption )

def calculate_max_trip_consumption(list_fuel_consumption ):
	max_consumption = 0
	for trip_fuel_consumption in list_fuel_consumption :
		if max_consumption < trip_fuel_consumption:
			max_consumption = trip_fuel_consumption
	return max_consumption

def calculate_total_mileage(list_length ):
	total = 0
	for length in list_length :
		total += length
	return total

def calculate_total_fuel_consumption(list_fuel_consumption ):
	total = 0
	for fuel_consumption in list_fuel_consumption :
		total += fuel_consumption
	return total

list_fuel_consumption = []
list_length = []

while True:
	length = float(input("Введите расстояние: "))
	if length < 0: break
	fuel_consumption = float(input("Введите количество израсходованного топлива: "))
	if fuel_consumption < 0: break

	list_fuel_consumption.append(fuel_consumption)
	list_length.append(length)

	fuel_consumption_100km = calculate_fuel_consumption_100km(length,fuel_consumption)
	print(f"Расход топлива: {fuel_consumption_100km }")

print(f"Средний расход топлива: {calculate_average_consumtion(list_fuel_consumption)}")
print(f"Максимальный расход: {calculate_max_trip_consumption(list_fuel_consumption)}")
print(f"Общий пробег: {calculate_total_mileage(list_length)}")
print(f"Общий расход топлива: {calculate_total_fuel_consumption(list_fuel_consumption )}")