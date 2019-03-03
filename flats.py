import csv

flats_list = list()

with open('output.csv', newline='') as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)

#можете посмотреть содержимое файла с квартирами через print, можете - на вкладке output.csv
# print (flats_list[0])


#1:
# 1) Напишите цикл, который проходит по всем квартирам, и показывает только новостройки
#и их порядковые номера в файле. Подсказка - вам нужно изменить этот код:
new_building_flats_count = 0
for flat in flats_list:
  if "новостройка" in flat:
    new_building_flats_count += 1
    [flat_id, _, flat_building_oldness, *_] = flat
    print(flat_building_oldness, flat_id, sep=' - ')
# 2) добавьте в код подсчет количества новостроек
print()
print('Итого квартир в новостройках - ', new_building_flats_count)
print()


#2:
# 1) Сделайте описание квартиры в виде словаря, а не списка. Используйте следующие поля из файла output.csv: ID, Количество комнат;Новостройка/вторичка, Цена (руб). У вас должно получиться примерно так:
# flat_info = {"id":flat[0], "rooms":flat[1], "type":flat[2], "price":flat[11]}
flats_info_dict = {}
for flat in flats_list[1:]:
  [flat_id, flat_rooms, flat_type, *rest_info, flat_price] = flat[:12]
  flat_info = {'id': flat_id, 'rooms': flat_rooms, 'type': flat_type, 'price': flat_price}
  flats_info_dict[flat_id] = flat_info
# print(flats_info_dict)
print()
# 2) Измените код, который создавал словарь для поиска квартир по метро так, чтобы значением словаря был не список ID квартир, а список описаний квартир в виде словаря, который вы сделали в п.1 
subway_dict = {}
subway_flats_count_dict = {}
for flat in flats_list[1:]:
  subway = flat[3].replace("м.", "")
  if subway:
    if subway not in subway_dict.keys():
      subway_dict[subway] = list()
      subway_flats_count_dict[subway] = 0
    flat_id = flat[0]
    subway_dict[subway].append(flats_info_dict[flat_id])
    subway_flats_count_dict[subway] += 1
print(subway_dict)
print()
# 3) Самостоятельно напишите код, который подсчитывает и выводит, сколько квартир нашлось у каждого метро.
for subway_id, flats_count in subway_flats_count_dict.items():
  print(subway_id, flats_count, sep=' - ')
