# looping over a string
for item in 'ucodetz':
	print(item)

# looping  over list of string
for item in [ 'jenadius','is founder of ucodetz']:
	print(item)

# looping over a list of number

for number in [1, 2, 3, 4, 5]:
	print(number)

# looping over a range of number

for num in range(10):
	print(num)

 # looping over an interval in range function
for num1 in range(2,10):
	print(num1)

# looping over an interval in range with give step forward function

for num3 in range(10,20, 2):
	print(num3) 

 """
 Write a program to 
 calculate the total price 
 of item in imaginary shoping cart
 """ 

prices = [ 1000, 2000, 3000]

total = 0
for price in prices:
	total +=price
print(f"The total pris is : {total}")



# ___________Nested loops_________

for x in range(4):
	for y in range(2):
		print(f"({x},{y})")

# printing F shape using nested loops 

numbers = [5, 2, 5, 2, 2]

# this is right method of doing this method
for x_count in numbers:
	output = " "
	for count in range(x_count):
		output += "*"
	print(output)

# cheating method of this solution

for x_count in numbers:
	print('*' * x_count)