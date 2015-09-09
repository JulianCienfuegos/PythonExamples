class natural_number(object):
	def __init__(self, n):	
		if n >= 0:
			self.n = n
		else:
			self.n = 0
	def __repr__(self):
		return "natural number: " + str(self.__dict__)
	def __str__(self):
		return "natural number: " + str(self.n)
	def __mul__(self, other):
		return self.n*other
	def __rmul__(self, other):
		return self.n*other


def quadratic(func, A = 1, B = 1, C = 1):
	def quad(a,b):
		return natural_number(A*func(a, b)*func(a,b) + B*func(a, b) + C)
	return quad

def pos_add(a,b):
	return natural_number(a + b)

def pos_sub(a,b):
	return  natural_number(a - b)

print pos_add(1,1)
print pos_sub(1,2)

pa  = quadratic(pos_add, 2, 2, 2)
print pa(1, 1)