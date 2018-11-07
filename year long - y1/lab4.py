'''
class Animal():
	def __init__(self, sound, name, age, favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat (self, food):
		print("yummy!!" + self.name + " is eating " + food)
	def description(self):
		print (self.name + "is" + str(self.age) + " years old and loves the color " + self.favorite_color)
	def make_sound (self, times):
		print (self.sound*times)
m = Animal("woof", "Max", 2, "blue")
m.eat("bone")
m.description()
m.make_sound(6)
'''
'''
class Person():
	def __init__ (self, name, age, city, gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def fav_breakfast (self, food):
		print ("my favorite breakfast is " + food)
h = Person("Harry", 24, "London", "male")
h.fav_breakfast("lucky charm cereal")
'''
class song