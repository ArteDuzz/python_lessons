# Задание номер 2
program_name = 'Ассистент путешественника'
print('Вас приветствует "%s"' % program_name)
currency_ratio_eur_rub = 75
euro_ratio_choice = input('Использовать евро в качестве расчетной валюты?(да/нет) ')
use_euro = euro_ratio_choice == 'да'
if use_euro:
  print('Текущий курс 1 евро:', currency_ratio_eur_rub, 'рублей')

trips_count = int(input('Введите количество поездок для расчета: '))
days_per_trip = []
single_day_costs = []
tickets_per_trip = []
single_ticket_costs = []
filled_trips = 0
trips_costs_sum = 0
# В комментариях стояли названия стран, но в задании они никак не фигурируют поэтому я их не добавил
for current_trip in range(trips_count):
  days_per_trip.append(int(input('Введите количество дней для %s-ой поездки : ' % str(current_trip + 1))))
  single_day_costs.append(int(input('Введите стоимость проживания в день : ')))
  tickets_per_trip.append(int(input('Введите количество билетов для поездки: ')))
  single_ticket_costs.append(int(input('Введите стоимость одного билета: ')))

  budget_per_trip = int(input('Введите бюджет на поездку: '))
  current_trip_days_cost = days_per_trip[current_trip] * single_day_costs[current_trip]
  current_trip_tickets_cost = tickets_per_trip[current_trip] * single_ticket_costs[current_trip]
  current_trip_cost = current_trip_days_cost + current_trip_tickets_cost

  if budget_per_trip and current_trip_cost >= budget_per_trip:
    excess_value = current_trip_cost - budget_per_trip
    excess_print_text = str(excess_value) + ' рублей'
    if use_euro:
      excess_rub_value = excess_value * currency_ratio_eur_rub
      excess_print_text = str(excess_value) + ' евро (' + str(excess_rub_value) + ' рублей)'
    print('Внимание! Бюджет на поездку превышен на', excess_print_text)
  trips_costs_sum += current_trip_cost
costs_sum_print_text = str(trips_costs_sum) + ' рублей'
if use_euro:
  trips_costs_rub_sum = trips_costs_sum * currency_ratio_eur_rub
  costs_sum_print_text = str(trips_costs_sum) + ' евро (' + str(trips_costs_rub_sum) + ' рублей)'
print('Предполагаемые расходы на все поездки составляют -', costs_sum_print_text)
# задание 3
print('---')
months_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
sign_change_dates_list = [20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22, 22]
zodiac_signs_list = ['Козерог', 'Водолей', 'Рыбы', 'Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец']
input_month = input('Введите месяц: ').lower()
input_day = int(input('Введите день: '))
if input_month in months_list and input_day <= 31:
  month_index = months_list.index(input_month)
  zodiac_sign_index = month_index
  zodiac_change_date = sign_change_dates_list[zodiac_sign_index]
  if input_day >= zodiac_change_date:
    zodiac_sign_index += 1
    if zodiac_sign_index == len(zodiac_signs_list):
      zodiac_sign_index = 0
  print('Вывод:')
  print(zodiac_signs_list[zodiac_sign_index])
else:
  print('Некорректные данные')