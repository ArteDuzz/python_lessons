import copy
# Задание 1
def recipes_file_to_dict(filename):
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
		recipes_dict = recipes_file_to_dict('recipes.txt')
		shop_list_per_person = get_ingredients_per_dish(dishes_list, recipes_dict)
		if person_count == 1:
			return shop_list_per_person
		else:
			shop_list = multiply_list_by_person_count(shop_list_per_person, person_count)
			return shop_list

if __name__ == '__main__':
	print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
	print()
	print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))
