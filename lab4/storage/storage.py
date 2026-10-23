import json
import os

class Storage1:
    @staticmethod
    def getFilePath():
        # Получаем путь к текущей папке (где лежит json_storage.py)
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Поднимаемся на уровень выше (в корень проекта lab4)
        project_root = os.path.dirname(base_dir)

        # Формируем путь: корень -> storage -> data.json
        file_path = os.path.join(project_root, "storage", "data.json")
        
        # Создаем папку storage, если её вдруг нет
        storage_folder = os.path.dirname(file_path)
        if not os.path.exists(storage_folder):
            os.makedirs(storage_folder)
            
        return file_path

    @staticmethod
    def sendToStorage(new_data):
        file_path = Storage1.getFilePath()
        
        # 1. Инициализируем пустой список по умолчанию
        cars = []
        
        # 2. Если файл существует, читаем его
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content:
                        existing_data = json.loads(content)
                        if isinstance(existing_data, list):
                            cars = existing_data
            except (json.JSONDecodeError, IOError):
                print("Предупреждение: Файл поврежден или нечитаем. Начинаем с чистого листа.")
                cars = []

        # 3. Добавляем новую машину в список в памяти
        cars.append(new_data)

        # 4. ВАЖНО: Перезаписываем файл целиком в режиме "w"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(cars, f, ensure_ascii=False, indent=4)
        
        print(f"Машина сохранена. Всего в базе: {len(cars)}")

    @staticmethod
    def pullFromStorage():
        file_path = Storage1.getFilePath()
        
        # Если файла нет, возвращаем пустой список
        if not os.path.exists(file_path):
            return [] 

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                
                # Если файл есть, но он пустой
                if not content:
                    return []
                
                data = json.loads(content)
                
                # Защита: если в файле не список, а что-то другое
                if isinstance(data, list):
                    return data
                else:
                    return []
                    
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка чтения JSON: {e}. Возвращаем пустой список.")
            return []

    @staticmethod
    def resetStorage(new_data):
        file_path = Storage1.getFilePath()
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(new_data, f, ensure_ascii=False, indent=4)
        