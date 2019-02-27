import datetime
from timeit import default_timer as timer
from random import shuffle
# Задание 1
# версия с timestamp
class Benchmark1:
	def __init__(self, function, *arguments):
		self.code_start_timestamp = datetime.datetime.now()
		self.function = function
		self.arguments = arguments

	def __enter__(self):
		self.function_output = self.function(*self.arguments)
		return self.function_output

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.code_end_timestamp = datetime.datetime.now()
		self.time_delta = (self.code_end_timestamp - self.code_start_timestamp).total_seconds() * 1000
		print('Время старта выполнения функции - {}'.format(self.code_start_timestamp.time()))
		print('Время завершения выполнения функции - {}'.format(self.code_end_timestamp.time()))
		print('Весь код исполнен за {} ms'.format(round(self.time_delta)))
# версия с timer <- её вроде как больше рекомендуют
class Benchmark2:
	def __init__(self, function, *arguments):
		self.code_start_timestamp = timer()
		self.function = function
		self.arguments = arguments

	def __enter__(self):
		self.function_output = self.function(*self.arguments)
		return self.function_output

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.code_end_timestamp = timer()
		self.time_delta = (self.code_end_timestamp - self.code_start_timestamp) * 1000
		print('Время старта выполнения функции - {}'.format(self.code_start_timestamp))
		print('Время завершения выполнения функции - {}'.format(self.code_end_timestamp))
		print('Весь код исполнен за {} ms'.format(round(self.time_delta)))

# Задание 2
# программа из задания 2_4
import copy
# Задание 1
def recipesFileToDict(filename):
	recipes_dict = {}
	with open(filename) as file:
		while True:
			dish_name = file.readline().strip()

			last_line_reached = len(dish_name) == 0
			if last_line_reached:
				return recipes_dict

			ingredients_count = int(file.readline().strip())
			ingredients_read = 0

			while ingredients_count > ingredients_read:
				# print(file.readline().strip().split(' | '))
				ingredient_name, quantity, measure = file.readline().strip().split(' | ')

				ingredient = {
					'ingredient_name': ingredient_name,
					'quantity': int(quantity),
					'measure': measure
				}
				if dish_name not in recipes_dict:
					recipes_dict[dish_name] = []

				recipes_dict[dish_name].append(ingredient)
				ingredients_read += 1
			# read empty line before next dish
			file.readline().strip()
# Задание 2
def get_ingredients_per_dish(dishes_list, recipes_dict):
	shop_list = {}
	for dish_name in dishes_list:
		try:
			dish_recipe = recipes_dict[dish_name]
		except KeyError:
			print('Блюда "{}" нет в файле рецептов'.format(dish_name))
		else: 
			for ingredient in dish_recipe:
				ingredient_name, measure, quantity = \
				[ingredient[key] for key in ('ingredient_name', 'measure', 'quantity')]
				if ingredient_name not in shop_list.keys():
					shop_list[ingredient_name] = {
						'measure': measure,
						'quantity': quantity,
					}
				else:
					shop_list[ingredient_name]['quantity'] += ingredient['quantity']
	return shop_list
def multiply_list_by_person_count(shop_list_per_person, person_count):
	shop_list = copy.deepcopy(shop_list_per_person)
	for ingredient_data in shop_list.values():
		ingredient_data['quantity'] *= person_count
	return shop_list


def get_shop_list_by_dishes(dishes_list, person_count):
	try:
		1 / person_count
		1 / len(dishes_list)
	except ZeroDivisionError:
		print('Не указан список блюд или количество гостей')
	else:
		recipes_dict = recipesFileToDict('recipes.txt')
		shop_list_per_person = get_ingredients_per_dish(dishes_list, recipes_dict)
		if person_count == 1:
			return shop_list_per_person
		else:
			shop_list = multiply_list_by_person_count(shop_list_per_person, person_count)
			return shop_list

if __name__ == '__main__':
	def sort_list(input_list):
		input_list.sort()
		return input_list

	test_list = list(range(100000))
	shuffle(test_list)

	with Benchmark1(sort_list, test_list) as result:
		# print(result)
		pass

	shuffle(test_list)

	with Benchmark2(sort_list, test_list) as result:
		# print(result)
		pass

	with Benchmark1(get_shop_list_by_dishes, ['Фахитос', 'Омлет'], 3) as result:
		print(result)
		pass

	with Benchmark2(get_shop_list_by_dishes, ['Запеченный картофель', 'Омлет'], 2) as result:
		print(result)
		pass

