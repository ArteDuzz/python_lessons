class Car:
	fuel = 0 # 1
	position = 10 # km
	speed = 0 # km/h
	color = 'black'
	price = 500

	def __init__(self, position, speed, fuel, color):
		self.position = position
		self.speed = speed
		self.fuel = fuel
		self.color = color
		self.some_list = []

	def start(self):
		print('self is: ', self)
		print('started')

	def accelerate(self, value):
		self.speed += value

	def move(self, hours):
		self.position += hours * self.speed
		self.fuel -= hours * 10 # 10 l/h

	def brake(self):
		self.speed = 0
	def stop(self):
		print('stopped')
class Expensive:
	price = 1000000000000

	def start(self):
		print('Wroom')

class Cabrio(Car, Expensive):
	roof_status = 'folded'

	def start(self):
		print('pes')
		super().start()

	def unfold(self):
		self.roof_status = 'unfolded'

	def fold(self):
		self.roof_status = 'folded'
	def __lt__(self, other):
		return self.speed < other.speed

car = Car(300, 300, 300, 'green')
car1 = Car(400, 400, 400, 'dark')
car2 = Cabrio(500, 500, 500, 'blue')
car3 = Cabrio(500, 500, 500, 'blue')

car2.unfold()
print('car is', car)
print('car1 is', car1)
print('car3 is', car2)
print(car2)
print(car2.price)
print(Cabrio.mro())
car2.start()

print(car2 < car3)





































