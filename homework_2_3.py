# Задание 1, Задание 2

def command_resolver(command, available_operations):
	try:
		if len(command) < 5:
			raise Exception('Неверный формат команды')

		operation, raw_operand_1, raw_operand_2 = command.split(' ')

		assert operation in available_operations.keys(), 'Данная операция недопустима'
		try:
			operand_1 = int(raw_operand_1)
			operand_2 = int(raw_operand_2)
		except ValueError:
			raise Exception('Оба аргумента должны быть числами')
		if operation == '/' and operand_2 == 0:
			raise Exception('Недопустимо делить на ноль')

		result = available_operations[operation](operand_1, operand_2)
		print('Результат - {}'.format(result))
			
	except AssertionError as exception:
		raise Exception(exception)
	except ValueError:
		raise Exception('Недопустимое число аргументов')
	except Exception as e:
		print('Ошибка - {} (см. help)'.format(e))

def pole_notation_start():
	"""
	type 'Z X Y' where Z is one of / - + *
	and X, Y is both positive integer numbers
	example => + 2 2 => 4
	q - (quit) - команда, которая завершает выполнение программы
	"""
	arithmetic_operations = {
	    '+': lambda x, y: x + y,
	    '-': lambda x, y: x - y,
	    '*': lambda x, y: x * y,
	    '/': lambda x, y: x / y,
	}

	print('Вас приветствует программа польской нотации!')
	print('(Введите help, для просмотра синтаксиса)')
	while True:
		print()
		user_command = input('Введите команду - ')
		print()
		if user_command == 'help':
			print(pole_notation_start.__doc__)
		elif user_command == 'q':
			break
		else:
			command_resolver(user_command, arithmetic_operations)


if __name__ == '__main__':
	pole_notation_start()