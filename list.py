
# list of names
names = ['jenad', 'kuberwa', 'mkombo','Gillius']

# print a list of names in terminel
print(names)

# slide /accessing single or multiple items a list of name 
print(names[0]) 	# this returns  first item in list
print(names[0:3]) 	# this returns  ['jenad', 'kuberwa','mkombo'
print(names[-1]) 	# this returns first  item from thr end of the list
print(names[:])     # this returns all item in a list

#  change a value in list
change_name = names[0] = 'jena'
print(change_name)

"""
  Exercise for 

   write aprogram to find the largest number in a list of item
"""

 # solution

numbers = [20, 11, 3, 30, 79, 10]

maxi = numbers[0]
for number in numbers:
 	if number > maxi:
 		maxi= number
print(maxi)

# Onather exercise for you

"""
write a program to insert a item in list
"""

# solution

# fruit_list = []

# for count in range(5):
# 	get_fruit = input("Enter fruit name :")
# 	fruit_list += get_fruit 
# print(fruit)


#................ 2D list.................

matrix = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

# to access this we do like

print(matrix[0][0])

# To loop over all item in list we do like

for row in matrix:
	for item in row:
		print(item)

# .....................list method/function..............


numbers = [2,6,7,3,3,8]

# Add an item in a list 

numbers.append(12)


# Add an item somewhere in middle or at begining in a list 

#             loc  item
numbers.insert(0   ,  11)

# remove an item i list

numbers.remove(11)

#  remove all item in list
# numbers.clear() 

#  if wanna remove a last item in a list
numbers.pop() 

# if you wanna check for the exitence of na item in list

numbers.index(2) # this return  a first item in list
#  for this if pass an index that does not exist in list
#  this will give an error


# so the best practise we use " in " operator like
print(40 in numbers) 

# if you wanna count the duplicate number in list 

print(numbers.count(3))

#  if you anna sort your list
sorted_list = numbers.sort()
reverse_list = numbers.reverse()
print(sorted_list)
print(reverse_list)

# if you wanna copy a list
copied_list = numbers.copy()

print(copied_list) 
""" for copy method if you wanna add an
  item in origin list won't addect the copied one
"""
#  for example 

numbers.append(30) # This won't affect the copied list 
# because these is an independent  list


print(numbers)





# exercise for this lesson


"""
 Write program to remove a duplicate in list
"""

nums = [2,3,3,3,12,3]

unique_list =[]

for num in nums:
	if num not in unique_list:
		unique_list.append(num)
print(unique_list)

