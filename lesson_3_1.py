import csv
from pprint import pprint

# flats_list = []
# with open('flats.csv') as datafile:
# 	flats_csv = csv.reader(datafile, delimiter=';')
# 	# flats_csv = csv.DictReader(datafile, delimiter=';')
# 	# print(flats_csv)
# 	# for item in flats_csv:
# 	# 	print(item)
# 	# 	# print(item['Метро'])

# 	flats_list = list(flats_csv)
# 	print(flats_list)



# csv.register_dialect('customcsv', delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar='"', escapechar='\\')
# with open('flats_2.csv', 'w') as datafile:
# 	datafile_csv = csv.writer(datafile, 'customcsv')
# 	datafile_csv.writerows(flats_list)


# import json
# with open('newsafr.json') as datafile:
	# json_data = json.load(datafile)
	# pprint(json_data)
	# for item in json_data:
	# pprint(json_data['rss']['channel'])

# with open('newsafr_2.json', 'w') as datafile:
# with open('newsafr_2.json', 'w', encoding='utf-8') as datafile:
	# json.dump(json_data['rss']['channel']['items'][0], datafile, ensure_ascii = False, indent = 2)

import xml.etree.ElementTree as ET
tree = ET.parse('newsafr.xml')
root = tree.getroot()
print(root)
print(root.tag)
print(root.attrib)
xml_title = root.find('channel/title')
print(xml_title.text)

xml_news = root.findall('channel/item')
print(len(xml_news))
for article in xml_news:
	print(article.attrib['id'])
	title = article.find('title')
	print(title.text)
	print()

def sort_by_length(inputStr):
	return(len(inputStr))