# Задания 2,3
documents = [
	{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
	{"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
	{"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
	{"type": "invoice", "number": "10007"}
]
directories = {
	'1': ['2207 876234', '11-2'],
	'2': ['10006'],
	'3': []
}

def check_document_existance(user_doc_number):
	doc_founded = False
	for current_document in documents:
		doc_number = current_document['number']
		if doc_number == user_doc_number:
			doc_founded = True
		if not doc_founded:
			print('Документ с таким номером не найден.')
	return doc_founded;

def show_doc_owner_name():
	user_doc_number = input('Введите номер документа - ')
	print()
	doc_exist = check_document_existance(user_doc_number)
	if doc_exist:
		for current_document in documents:
			doc_number = current_document['number']
			if doc_number == user_doc_number:
				doc_owner_name = current_document['name']
				print('Владелец документа - {}'.format(doc_owner_name))
				break
	return

def show_all_doc_owners_names():
	users_list = []
	for current_document in documents:
		try:
			doc_owner_name = current_document['name']
			users_list.append(doc_owner_name)
		except KeyError:
			pass
	uniq_users = set(users_list)
	print('Список владельцев документов - {}'.format(uniq_users))

def remove_doc_from_shelf(doc_number):
	for directory_number, directory_docs_list in directories.items():
		if doc_number in directory_docs_list:
			directory_docs_list.remove(doc_number)
			break
	return

def add_new_shelf(shelf_number = ''):
	if not shelf_number:
		shelf_number = input('Введите номер полки - ')
	if shelf_number not in directories.keys():
	    directories[shelf_number] = []
	    print('Добавлена полка "{}"'.format(shelf_number))
	return

def append_doc_to_shelf(doc_number, shelf_number):
	add_new_shelf(shelf_number)
	directories[shelf_number].append(doc_number)
	return

def delete_doc():
	user_doc_number = input('Введите номер документа - ')
	print()
	doc_exist = check_document_existance(user_doc_number)
	if doc_exist:
		for current_document in documents:
			doc_number = current_document['number']
			if doc_number == user_doc_number:
				documents.remove(current_document)
				remove_doc_from_shelf(doc_number)
				print('Документ с номером "{}" был успешно удален'.format(doc_number))
				break
	return

def show_doc_shelf():
	user_doc_number = input('Введите номер документа - ')
	print()
	doc_exist = check_document_existance(user_doc_number)
	if doc_exist:
		for directory_number, directory_docs_list in directories.items():
			if user_doc_number in directory_docs_list:
				print('Документ находится на полке номер {}'.format(directory_number))
				break
	return

def move_doc_to_shelf():
	user_doc_number = input('Введите номер документа - ')
	user_shelf_number = input('Введите номер полки для перемещения - ')
	print()
	remove_doc_from_shelf(user_doc_number)
	append_doc_to_shelf(user_doc_number, user_shelf_number)
	# print(directories)
	print('Документ номер "{}" был перемещен на полку номер "{}"'.format(user_doc_number, user_shelf_number))
	return

def show_document_info(document):
	doc_type = document['type']
	doc_number = document['number']
	doc_owner_name = document['name']
	print('{} "{}" "{}"'.format(doc_type, doc_number, doc_owner_name))
	return

def show_all_docs_info():
	print('Список всех документов:')
	print()
	for current_document in documents:
		show_document_info(current_document)
	return

def add_new_doc():
	print('Добавление нового документа:')
	new_doc_number = input('Введите номер документа - ')
	new_doc_type = input('Введите тип документа - ')
	new_doc_owner_name = input('Введите имя владельца документа- ')
	new_doc_shelf_number = input('Введите номер полки для хранения - ')
	new_doc = {
		"type": new_doc_type,
		"number": new_doc_number,
		"name": new_doc_owner_name
	}
	documents.append(new_doc)
	append_doc_to_shelf(new_doc_number, new_doc_shelf_number)
	print()
	print('На полку "{}" добавлен новый документ:'.format(new_doc_shelf_number))
	show_document_info(new_doc)
	return

def secretary_program_start():
	"""
	ap - (all people) - команда, которая выводит список всех владельцев документов
	p – (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
	l – (list) – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
	s – (shelf) – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
	a – (add) – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
	имя владельца и номер полки, на котором он будет храниться.
	d – (delete) – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
	m – (move) – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
	as – (add shelf) – команда, которая спросит номер новой полки и добавит ее в перечень;
	q - (quit) - команда, которая завершает выполнение программы
	"""
	print('Вас приветствует программа помошник!')
	print('(Введите help, для просмотра списка поддерживаемых команд)')
	while True:
		print()
		user_command = input('Введите команду - ')
		print()
		if user_command == 'p':
			show_doc_owner_name()
		elif user_command == 'ap':
			show_all_doc_owners_names()
		elif user_command == 'l':
			show_all_docs_info()
		elif user_command == 's':
			show_doc_shelf()
		elif user_command == 'a':
			add_new_doc()
		elif user_command == 'd':
			delete_doc()
		elif user_command == 'm':
			move_doc_to_shelf()
		elif user_command == 'as':
			add_new_shelf()
		elif user_command == 'help':
			print(secretary_program_start.__doc__)
		elif user_command == 'q':
			break
if __name__ == '__main__':
	secretary_program_start()