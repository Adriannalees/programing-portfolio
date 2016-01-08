# python learning exercises

# functions
def echo(thing):
	return thing
	
def swap(p, h):
	return h, p
	
		
def main_function():
	print "testing echo('marco'): ", echo('marco')
	print "testing echo('shut up'): ", echo('no, you shut up')
	print "testing swap('fame', 'fortune')", swap('fame', 'fortune')
	
	
# arithmetic Functions
def reverse(x):
	return -x
	
def plus(n, k):
	return n + k
	
def diff(a, b):
	return a - b
	
def abs_diff(d, b):
	
	
	
def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-3): ", reverse(-3)
	print "test reverse(11, 2): ", plus(11, 2)
	print "test diff(18, 4): ", diff(18, 4)
	
def main():
	main_function()
	main_arithmetic()
	
main()