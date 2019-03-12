import requests
import os
# import pprint
# print(requests.__doc__)
# print(requests)

# find apple song

# URL = 'https://itunes.apple.com/search'

# params = {'term': 'coldplay'}

# get_res = requests.get(URL, params = params)

# res_data = get_res.json()['results']
# # print(res_data)

# for item in res_data:
# 	image_url = item['artworkUrl100']
# 	print(f"{item['trackName']} - {item['artistName']} - {image_url}")

# 	filename = f"{item['artistName']}_{item['trackName']}.jpg"
# 	filename_path = os.path.join('for_any_data', filename)
# 	with open(filename_path, 'wb') as future_img:
# 		img_resp = requests.get(image_url)
# 		future_img.write(img_resp.content)
# 		print(f"Saved in {filename_path}")

# translate yandex

URL = 'https://translate.yandex.net/api/v1/tr.json/translate'
params = {
	'id': 'b2569de7.5c87a0b6.83dea07a-0-0', # nado vsyat token sperva
	'lang': 'ru-kk',
	'reason': 'auto',
	'srv': 'tr-text'
}

payload = {
	'text': 'привет всем'
}

res = requests.post(URL, params = params, data = payload)
print(res.status_code)
print(res.json())