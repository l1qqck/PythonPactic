list_of_auto = []
auto_params = ('марка', 'модель', 'год выпуска', 'пробег', 'цена')

def printCarList(list):
    for i, car in enumerate(list, 1):
        print(f"{i} . {car}")

while True:
    car = {}
    stop_flag = False

    for param in auto_params:
        value = input(f"Введите {param} (или СТОП чтобы закончить): ")
        if value.lower() == 'стоп':
            stop_flag = True
            break
        car[param] = value

    if stop_flag:
        print("Ввод остановлен.")
        break

    # Сюда попадаем, только если пользователь ввёл все параметры
    list_of_auto.append(car)
    print("Машина добавлена!\n")

print("\nСписок машин:")
printCarList(list_of_auto)


def get_Probeg(car):
    price = car.get("пробег" , "")
    
    if not price or not price.strip().isdigit(): return 0

    return int(price)


def get_Price(car):
    price = car.get("цена" , "")
    
    if not price or not price.strip().isdigit(): return 0

    return int(price)


def sortByProbeg(cars):
    #key говорит, по какому значению сортировать
    return sorted(cars, key=get_Probeg)


def sortByPrice(cars):
    return sorted(cars, key=get_Price)

def calculateMidPrice(cars):
   
    sum = 0
    for car in cars:
        sum += get_Price(car)
    return sum / len(cars)


def calculateMaxPrice(cars):
    if len(cars) == 0:
        return None

    max_car = None
    max_value = -1

    for car in cars:
        price = get_Price(car)
        if price > max_value:
            max_value = price
            max_car = car

    return max_car


while True:

    print("\n1 . поиск автомобилей заданной марки\n2 . фильтрацию по пробегу\n3 . определение средней цены\n4 . поиск самого дорогого автомобиля\n5 . список уникальных марок\n6 . сортировку по цене\nЛЮБОЙ ДРУГОЙ СИМВОЛ ЧТОБЫ ВЫЙТИ")
    status = input("введите номер операции: ")

    match status:

        #поиск автомобилей заданной марки
        case "1": 
            search_mark = input("Введите необходимую марку: ").strip().lower()
            found_cars = [
                car for car in list_of_auto
                if car.get("марка" , "").lower() == search_mark
            ]

            if found_cars:
                print(f"\nМашины марки: {search_mark}")
                printCarList(found_cars)
            else:
                print(f"Машины марки {search_mark} нету")

        #фильтрацию по пробегу
        case "2":
            newSortedCarList = sortByProbeg(list_of_auto)
            printCarList(newSortedCarList)

        #определение средней цены
        case "3":
            print(f"Средняя цена: {calculateMidPrice(list_of_auto)}")

        #поиск самого дорогого автомобиля
        case "4":
            print(f"Самый дорогой автомобиль: \n{calculateMaxPrice(list_of_auto)}")

        #список уникальных марок
        case "5":
            unique_marks = list({car.get("марка", "").strip().lower() for car in list_of_auto if car.get("марка")})
            printCarList(unique_marks)

        #сортировку по цене
        case "6":
            newSortedCarList = sortByPrice(list_of_auto)
            printCarList(newSortedCarList)

        #выход
        case _:
            break


   
