import math

def sinput(query, type=int):
	try:
		return type(input(query))
	except:
		print('Invalid Input - Try Again')
		return sinput(query, type)

x = sinput('Enter a number x:   ')
y = sinput('Enter a number y:   ')
print(f'''x^y = {x**y}
log(x) = {math.log(x, 2)}''')