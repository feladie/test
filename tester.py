def f01():
	print("Hello World!")
	f02()

def f02():
	x = 'i'
	y = 'love'
	z = 'python'
	f03(x, y, z)  # Last line in f2()

def f03(*words):
	truth = " ".join(words)  # This is broken.
	truth_emphasized = truth + "!"
	print(truth_emphasized)
	f04(truth)  # Last line in f03()

def f04(string):
	length = len(string)
	for index in range(1, length):
		print(string[-index], end=" ")
	print(string[0])
	f05(string)  # Last line in f04()

def f05(word):
	count = 0
	for ch in word:
		print(' ' * count, word)
		count += 1
	f06("South Hall", "Python Rocks!")  # Last line in f05()

def f06(string1, string2):
	length1 = len(string1)
	length2 = len(string2)
	if length1 > length2:
		print('{} is longer than {} by {} chars'.format(string1, string2, length1 - length2))
		print('{} has only '.format(string2), '{0:.2f}'.format(length2 / length1 * 100), ' the number of chars of {}'.format(string1))
	else:
		print('{} is longer than {} by {} chars'.format(string2, string1, length2 - length1))
		print('{} has only '.format(string1), '{0:.2f}'.format(length1 / length2 * 100), ' the number of chars of {}'.format(string2))

def f07():
	count = 1
	total = 0
	while(count < 500):
		if count % 15 == 0:
			total += count
		elif count % 5 == 0:
			total += count
		elif count % 3 == 0:
			total += count
		count += 1
	return total

###############################################################################
def f08():
	total = 0
	for n in range(1, 500):
		if n % 15 == 0:
			total += n
		elif n % 5 == 0:
			total += n
		elif n % 3 == 0:
			total += n
	return total
###############################################################################
def f09():
	lst = []
	for n in range(1, 500):
		if n % 15 == 0:
			lst.append(n)
		elif n % 5 == 0:
			lst.append(n)
		elif n % 3 == 0:
			lst.append(n)
	return sum(lst)
###############################################################################
def f10(n):
	if n == 0:
		return 0
	else: 
		if n % 15 == 0:
			return n + f10(n - 1)
		elif n % 5 == 0:
			return n + f10(n - 1)
		elif n % 3 == 0:
			return n + f10(n - 1)
		else:
			return f10(n - 1)

###############################################################################
# Write f11() to take arguments, printing them as floats if they started as
# strings, integers if they started as floats, and as the value 0 if they
# started as ints.
def f11(item):
	if isinstance(item, str):
		print(float(item))
	elif isinstance(item, float):
		print(int(item))
	elif isinstance(item, int):
		print(0)

def f12():
    # lst = []
    # user_input = ''
    # while(user_input != 'done'): 
    #     with open('log_file.txt', 'w') as f:
    #         try:
    #             user_input = float(input('User input: '))
    #         except:
    #             f.write(str(user_input) + '\n')
    #         else:
    #             print(user_input)
    # else:
    # 	print('done')
    pass
    
def main():
	# print(f07())
	# print(f08())
	# print(f09())
	# print(f10(499))
	# f11_args = [1, "2", 3.0, '4', 5.0, 6]  # Last lines in various_solutions()
	# for arg in f11_args:
	# 	f11(arg)
	f12()

if __name__ == '__main__':
	main()