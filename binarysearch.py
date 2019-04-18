# binary search

import random
from timeit import default_timer as timer

start_time = timer()

a = []
x = 10000
num = random.randint(0,10000)
while x > 0:
		x -= 1
		b = random.randint(0,10000)
		a.append(b)
a.sort()
print('Guessed number is: ' + str(num))

def linear():
	global a, num
	c = num in a

	if c:
		print('\n' + str(num) + ' is in list.')
	else:
		print('\n' + str(num) + ' is not in list.')
	print('The linear method took ' + str(timer() - start_time) + ' seconds.')
		
def binary():
	global a, num
	while len(a)//2 > 0:
		mid = len(a)//2
		if a[mid] == num:
			return True
		elif a[mid] > num:
			a = a[:mid]
		else:
			a = a[mid + 1:]
	return False
		
def torf():	
	if binary() == True:
		print(str(num) + ' is in list.')
	else:
		print(str(num) + ' is not in list.')
	print('The binary method took ' + str(timer() - start_time) + ' seconds.')
			
binary()
torf()
#linear()

# Binary method involves sorting the list into ascending order, so it is always going to be the slower one.
# Unless one has to use multiple binary searches, sorting the list is not the most efficient.
