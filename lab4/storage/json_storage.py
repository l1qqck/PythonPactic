import json
import os

class Storage:
	@staticmethod
	def getFilePath():
		# Получаем директорию, где лежит этот файл (json_storage.py)
		base_dir = os.path.dirname(os.path.abspath(__file__))

		# Поднимаемся на уровень вверх (из storage в корень проекта)
		project_root = os.path.dirname(base_dir)

		# Собираем полный путь к файлу
		file_path = os.path.join(project_root, "storage", "data.json")
		
		return file_path


	@staticmethod
	def sendToStorage(newData):
		file_path = Storage.getFilePath()

		if not os.path.exists(file_path):
			data = []
		else:
			with open(file_path , "r", encoding="utf-8") as file:
				data = json.load(file)
		
		data.append(newData)
		
		with open(file_path , "w", encoding="utf-8") as file:
			json.dump(data, file, ensure_ascii= False, indent= 4)

	@staticmethod
	def pullFromStorage():
		file_path = Storage.getFilePath()
		
		with open(file_path , "r", encoding="utf-8") as file:
			return json.load(file)
