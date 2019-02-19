# задание 3
class AnimalRegister:
	total_weight = 0
	max_weight = 0
	max_weight_animal_name = ''

	def __init__(self, total_weight, max_weight, max_weight_animal_name = ''):
		self.total_weight = total_weight
		self.max_weight = max_weight
		self.max_weight_animal_name = max_weight_animal_name

	def register_animal(self, name, weight):
		self.total_weight += weight
		if weight > self.max_weight:
			self.max_weight = weight
			self.max_weight_animal_name = name

	def show_total_weight(self):
		print('Общий вес всех животных - {}'.format(self.total_weight))

	def show_max_weight(self):
		print('Наибольший вес равен - {}'.format(self.max_weight))

	def show_most_heavy_animal(self):
		print('Самое тяжелое животное - {}'.format(self.max_weight_animal_name))

joe_counter = AnimalRegister(0, 0)
# задание 1
class Animal:
	name = ''
	weight = 0 # kg
	kind = ''
	voice_sound = ''
	is_hungry = True

	def __init__(self, name, weight, kind, voice_sound):
		self.name = name
		self.weight = weight
		self.kind = kind
		self.voice_sound = voice_sound

	def voice(self):
		print('{} "{}" говорит: {} !'.format(self.kind, self.name, self.voice_sound))

	def feed(self):
		self.is_hungry = False
		print('Животное - {} "{}" накормлено.'.format(self.kind, self.name))


class AnimalWithUdder(Animal):
	has_milk = True
	
	def collect_milk(self):
		has_milk = False
		print('Дойка произведена у : {} "{}".'.format(self.kind, self.name))

class AnimalWithWool(Animal):
	has_uncut_wool = True
	
	def collect_wool(self):
		has_uncut_wool = False
		print('Шерсть пострижена у : {} "{}".'.format(self.kind, self.name))
		
class Bird(Animal):
	has_eggs = True

	def collect_eggs(self):
		has_eggs = False
		print('Яйца собраны.')

class CurrentKind():
	def __init__(self, name, weight):
		joe_counter.register_animal(name, weight)
		super().__init__(name, weight, self.kind, self.voice_sound)

class Goose(CurrentKind, Bird):
	kind = 'гусь'
	voice_sound = 'га-га'

class Cow(CurrentKind, AnimalWithUdder):
	kind = 'корова'
	voice_sound = 'муууууу'

class Sheep(CurrentKind, AnimalWithWool):
	kind = 'овца'
	voice_sound = 'беееее'

class Chicken(CurrentKind, Bird):
	kind = 'курица'
	voice_sound = 'кудах-кудах'

class Goat(CurrentKind, AnimalWithUdder):
	kind = 'коза'
	voice_sound = 'мммееее'

class Duck(CurrentKind, Bird):
	kind = 'утка'
	voice_sound = 'кря-кря'
# задание 2
goose_gray = Goose('Серый', 7)
goose_white = Goose('Белый', 8)
cow_manya = Cow('Манька', 150)
sheep_barash = Sheep('Барашек', 20)
sheep_curvy = Sheep('Кудрявый', 17)
chicken_koko = Chicken('Ко-Ко', 6)
chicken_kukare = Chicken('Кукареку', 9)
goat_horn = Goat('Рога', 15)
goat_hoof = Goat('Копыта', 28)
duck_krya = Duck('Кряква', 12)
# для примера указал взаимодействия с одним из экземпляров
print()
print('Взаимодействие с животными:')
print()
goose_gray.feed()
goose_gray.voice()
goose_gray.collect_eggs()
print()
cow_manya.feed()
cow_manya.voice()
cow_manya.collect_milk()
print()
sheep_barash.feed()
sheep_barash.voice()
sheep_barash.collect_wool()
print()
chicken_koko.feed()
chicken_koko.voice()
chicken_koko.collect_eggs()
print()
goat_horn.feed()
goat_horn.voice()
goat_horn.collect_milk()
print()
duck_krya.feed()
duck_krya.voice()
duck_krya.collect_eggs()
print()
# задание 3
joe_counter.show_total_weight()
print()
joe_counter.show_max_weight()
print()
joe_counter.show_most_heavy_animal()