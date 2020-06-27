customer = {
	'name': 'jenad',
	'email': 'jnichoraus3@gamil.com',
	'password':' 121233344',
	'is_active':True
}

# accessing the dictionary in python

# we do like, use key to get the value  as "name" is keya and 'jenad' is value

print(customer['name'])

# Or we can ust use get method to access the dictionary

print(customer.get('names', 'is good programmer'))
 

# simple program for converting number into words

# define a dictionary

digit_mapping = {
	
	'0':'zero',
	'1': 'One',
	'2': 'Two',
	'3': 'Tree',
	'4': 'Four',
	'5': 'Five',
	'6': 'six',
	'7': 'Seven',
	'8': 'Eight',
	'9': 'Nine',

}
phone_nunmber = input('Enter phone number: ')

output =""
for char in phone_nunmber:
	output += digit_mapping.get(char,"!") + " "


print(output)



 
