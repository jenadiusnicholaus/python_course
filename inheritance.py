class Mammal:
	def walk(self):
		print('walks')

class Dog(Mammal):
	def bark(self):
		print('bark')

class Cat(Mammal):
	def be_annoying(self):
		print('be_annoying')

dog = Dog()
dog.walk()
dog.bark()
print("-------")
cat = Cat()
cat.walk()
cat.be_annoying()
