import requests
from requests.exceptions import ConnectionError
import os
# функция переводчик

def translate_it(**kwargs):
	"""
	Функция принимает на вход 4 параметра
	path_to_source = <string> - путь до исходного файла(обязательно)
	path_to_result = <string> - путь куда сохранять результат(обязательно)
	source_lang = <string>  - язык текста исходного файла(обязательно)
	translate_lang = <string>  - язык перевода(по умолчанию - русский)
	"""
	params = {
		'path_to_source': kwargs.get('path_to_source'),
		'path_to_result': kwargs.get('path_to_result'),
		'source_lang': kwargs.get('source_lang'),
		'translate_lang': kwargs.get('translate_lang', 'ru'),
	}
	API_KEY = 'trnsl.1.1.20190312T122323Z.6f2305315fdb7096.8d321f0720ec6dcdefee52351b515d663484b0e8'
	URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

	try:
		#  check params
		for param_name, param_value in params.items():
			if not param_value:
				raise TypeError('Отсутствует обязательный параметр - {}'.format(param_name))
		#  read data from file
		path_to_source = params['path_to_source']
		source_text_list = []
		source_text_string = ''
		with open(path_to_source, 'r') as source_file:
			for line in source_file.readlines():
				source_text_list.append(line)

		if source_text_list:
			source_text_string = ''.join(source_text_list)
		else: 
			raise TypeError('В файле отсутствует текст')
	except FileNotFoundError as error:
		print('По указанному пути файл отсутствует')
	except TypeError as exception:
		print(exception)
	else:
		# get translate
		source_lang = params['source_lang'].lower()
		translate_lang = params['translate_lang'].lower()
		payload = {
		    'key': API_KEY,
		    'text': source_text_string,
		    'lang': '{}-{}'.format(source_lang, translate_lang),
		}
		try:
			response = requests.post(URL, params = payload)
		except ConnectionError as exception:
			print('Не удалось установить соединение')
		else:
			if response.status_code == requests.codes.ok:
				response_result_data = response.json()['text']
				translated_text = ' '.join(response_result_data)
				# write to file
				filename = f"{source_lang}_to_{translate_lang}.txt"
				path_to_result = params['path_to_result']
				filename_path = os.path.join(path_to_result, filename)
				with open(filename_path, 'w') as file:
					file.write(translated_text)
					print('Перевод сохранен в {}'.format(filename_path))
					print()
				return translated_text

if __name__ == '__main__':
	print(translate_it(path_to_source='FR.txt', path_to_result='for_texts', source_lang='fr'))











