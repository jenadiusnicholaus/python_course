class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def move(self):
		print("move")

	def draw(self):
		print('draw')

	def coordinate(self):
		print(f'x and y exis is {self.x, self.y}')


# calling an objects 

# What is an object  
#                   is instance of the class


point1 = Point(110,198)

print(point1.x, point1.y)
print(point1.draw())
print(point1.move())

print(point1.coordinate())




