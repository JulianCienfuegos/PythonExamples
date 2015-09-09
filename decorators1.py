def around(func):
	def wrapper(*args):
		print 'before computation'
		result = func(*args)
		print 'after  computation'
		return result
	return wrapper

@around
def my_div(a,b):
	if b == 0:
		print'Division by zero'
	else:
		return float(a)/float(b)

@around 
def my_mult(a,b):
	return float(a*b)

print my_div(1,10)
print my_mult(4,4)