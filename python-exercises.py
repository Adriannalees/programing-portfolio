# python learning exercises

# Functions
def echo(thing):
	return thing

def swap(thing1, thing2):
	return thing2, thing1

	
def main_function():
	print "testing echo('marco'): ", echo('marco')
	print "testing echo('shut up'): ", echo('no, you shut up')
	print "testing swap('fame', 'fortune')", swap('fame', 'fortune')


#Arithmetic Functions
def reverse(x):
	return -x

def plus(a, b):
	return a + b
	
def diff(x, y):
	return x - y
	
def abs_diff(d, b):
	diff = d - b
	if diff < 0:
		diff *= -1
	return diff
	
def divide(w, p):
	return w / float(p)
	
def remainder(w, p):
	return w % p

def power(x, e):
	answer = 1
	for i in range(e):
		answer *= x
	return answer

def power2(x, e):
	return x ** e
	
def calculate(a, b, c, d, e):
	return (a + b / d - e) * c
	
def ratio(al, fred):
	if al > fred:
		return al / fred
	else:
		return fred / al

def pythagoras(a, b):
	return (a**2 + b**2)**(.5)

def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-3): ", reverse(-3)
	print "testing plus(1, 1): ", plus(1, 1)
	print "testin' diff(12, 5): ", diff(12, 5)
	print "test abs_diff(10, 5): ", abs_diff(10, 5)
	print "test abs_diff(5, 10): ", abs_diff(5, 10)
	print "test divide(10, 2): ", divide(10, 2)
	print "test divide(2, 10): ", divide(2, 10)
	print "test remainder(40, 19): ", remainder(40, 19)
	print "test remainder(126, 19): ", remainder(126, 19)
	print "test remainder(133, 19): ", remainder(133, 19)
	print "test power(2, 3): ", power(2, 3)
	print "test calculate(1, 2, 3, 4, 5): ", calculate(1, 2, 3, 4, 5)
	print "testing ratio(3.2, 7.8): ", ratio(3.2, 7.8)
	print "testing ratio(7.8, 3.2): ", ratio(7.8, 3.2)
	print "testing pythagoras(3, 4): ", pythagoras(3, 4)
	print "testing pythagoras(35, 67): ", pythagoras(35, 67)
	
def reverse(zack):
	return not zack

def band(a, b):
	if a==True and b==True:
		return True
	else:
		return False

def band2(a, b):
	return a and b
	
def bor(a, b):
	if a==True or b==True:
		return True
	else:
		return False
	
def bor2(a, b):
	return a or b
	
def xsame(b, g):
	return b == g

def xor(b, g):
	return b != g


def main_boolean():
	print "test reverse(True): ", reverse(True)
	print "test reverse(False): ", reverse(False)
	print "test reverse(1): ", reverse(1)
	print "test reverse(0): ", reverse(0)
	print "test band(True, True): ", band(True, True)
	print "test band2(True, True): ", band(True, True)
	print "test band(True, False): ", band(True, False)
	print "test band2(True, False): ", band(True, False)
	print "test band(False, False): ", band(False, False)
	print "test band2(False, False): ", band(False, False)
	print "test bor(True, True): ", bor(True, True)
	print "test bor(True, True): ", bor(True, True)
	print "test bor(True, False): ", bor(True, False)
	print "test bor(True, False): ", bor(True, False)
	print "test bor(False, False): ", bor(False, False)
	print "test bor(False, False): ", bor(False, False)
	print "test xsame(True, True): ", xsame(True, True)
	print "test xsame(True, False): ", xsame(True, False)
	print "test xsame(False, True): ", xsame(False, True)
	print "test xsame(False, False): ", xsame(False, False)
	print "test xor(True, True): ", xor(True, True)
	print "test xor(True, False): ", xor(True, False)
	print "test xor(False, True): ", xor(False, True)
	print "test xor(False, False): ", xor(False, False)

def positive(n):
	return n > 0
	
def bigger(r, p):
	return r > p
		
def no_diff(w, h):
	return w == h		

def not_same(b, g):
	return b != g
	
def less_than(r, p):
	return r < p
	
def at_least_13(d):
	return d >= 13

def at_most_13(d):
	return d <= 13

def main_boolean_numbers():
	print "testing positive(29): ", positive(29)
	print "testing positive(-29): ", positive(-29)
	print "test bigger(200, 10): ", bigger(200, 10)
	print "test bigger(10, 200): ", bigger(10, 200)
	print "testing no_diff(99, 99): ", no_diff(99,99)
	print "testing no_diff(67, 76): ", no_diff(67,76)
	print "testing no_same(99, 99): ", not_same(99,99)
	print "testing no_same(67, 76): ", not_same(67,76)
	print "test less_than(2, 8): ", less_than(2, 8)
	print "test less_than(8, 2): ", less_than(8, 2)
	print "test at_least_13(45): ", at_least_13(45)
	print "test at_least_13(13): ", at_least_13(13)
	print "test at_least_13(11): ", at_least_13(11)
	print "test at_most_13(45): ", at_most_13(45)
	print "test at_most_13(13): ", at_most_13(13)
	print "test at_most_13(11): ", at_most_13(11)
	

def biggest(ab, yb):
	if ab > yb:
		return ab
	else:
		return yb

def smallest(ab, yb):
	if ab < yb:
		return ab
	else:
		return yb
		
def letter_grade(score):
	if score >= 90:
		return "A"
	elif score >= 80:
		return "B"
	elif score >= 70:
		return "C"
	elif score >= 60:
		return "D"
	else:
		return "F"
		
def food_tax(subtotal, grocery):
	if grocery:
		return subtotal * .03
	else:
		return subtotal * .0725
		
def same(a, b, c):
	return a == b == c

def big3(james, irving, love):
	if james >= irving and james >= love:
		return james
	elif irving >= james and irving >= love:
		return irving
	elif love >= james and love >= irving:
		return love
		
def small_sum(a, b, c):
	if a < b and b < c:
		return a + b
	elif b < a and c < a:
		return b + c
	else:
		return a + c

def meat_loaf(onions, ketchup, garlic):
	if onions and garlic and not ketchup:
		return True
	elif onions and ketchup and not garlic:
		return True
	elif garlic and ketchup and not onions:
		return True
	else:
		return False

def big3reorder(a, b, c):
	if a == big3(a, b, c):
		return a, biggest(b, c), smallest(b, c)
	elif b == big3(a, b, c):
		return b, biggest(a, c), smallest(a, c)
	else:
		return c, biggest(a, b), smallest(a, b)
	
def positive_multiple(w, h):
	product = w * h
	if not positive(product):
		return product * -1
	else:
		return product
	
	
def main_conditionals():
	print "testing biggest(500, 10): ", biggest(500, 10)
	print "testing biggest(500, 1000): ", biggest(500, 1000)
	print "testing smallest(500, 10): ", smallest(500, 10)
	print "testing smallest(500, 1000): ", smallest(500, 1000)
	print "test letter_grade(55): ", letter_grade(55)
	print "test letter_grade(65): ", letter_grade(65)
	print "test letter_grade(70): ", letter_grade(70)
	print "test letter_grade(85): ", letter_grade(85)
	print "test letter_grade(95): ", letter_grade(95)
	print "testing food_tax(12.45, True): ", food_tax(12.45, True)
	print "testing food_tax(12.45, False): ", food_tax(12.45, False)
	print "test same(7, 7, 7): ", same(7, 7, 7)
	print "test same(1, 2, 4): ", same(1, 2, 4)
	print "testing big3(3, 2, 1): ", big3(3, 2, 1)
	print "testing big3(2, 3, 1): ", big3(2, 3, 1)
	print "testing big3(1, 2, 3): ", big3(1, 2, 3)
	print "testing big3(3, 3, 1): ", big3(3, 3, 1)
	print "testing big3(1, 3, 3): ", big3(1, 3, 3)
	print "testing big3(3, 1, 3): ", big3(3, 1, 3)
	print "test small_sum(1, 2, 3): ", small_sum(1, 2, 3)
	print "test small_sum(3, 2, 1): ", small_sum(3, 2, 1)
	print "testing meat_loaf(True, True, False): ", meat_loaf(True, True, False)
	print "testing meat_loaf(True, False, False): ", meat_loaf(True, False, False)
	print "testing meat_loaf(True, True, True): ", meat_loaf(True, True, True)
	print "test big3reorder(5, 8, 2): ", big3reorder(5, 8, 2)
	print "test positive_multiple(5, 7): ", positive_multiple(5, 7)
	print "test positive_multiple(-5, -7): ", positive_multiple(-5, -7)
	print "test positive_multiple(-5, 7): ", positive_multiple(-5, 7)
	

def total(x):
	# total(5) 0+1+2+3+4
	t = 0
	for num in range(x):
		t += num
	return t

def total_slice(a, b):
	t = 0
	for num in range(a, b):
		t += num
	return t

def total_slice2(a, b):
	t = 0
	for num in range(smallest(a, b), biggest(a, b)):
		t += num
	return t

def total_odds(a, b):
	t = 0
	for num in range(a, b):
		if num % 2 == 1:
			t += num
	return t
	
def total_evens(a, b):
	t = 0
	for num in range(a, b):
		if num % 2 == 0:
			t += num
	return t

def total_7s(a, b):
	t = 0
	for num in range(a, b):
		if num % 7 == 0:
			t += num
	return t
	
def total_non7s(a, b):
	t = 0
	for num in range(a, b):
		if num % 7 != 0:
			t += num
	return t

def squares(x):
	ts = 0
	for num in range(x):
		ts += num**2
	return ts

def main_counted_loops():
	print "testing total(5): ", total(5)
	print "testing total(63): ", total(63)
	print "testing total_slice(3, 8): ", total_slice(3, 8)
	print "testing total_slice2(8, 3): ", total_slice2(8, 3)
	print "testing total_slice2(3, 8): ", total_slice2(3, 8)
	print "testing total_odds(2, 10): ", total_odds(2, 10) # 3+5+7+9
	print "testing total_evens(2, 10): ", total_evens(2, 10) # 2+4+6+8
	print "testing total_7s(2, 30): ", total_7s(2, 30) # 7+14+21+28
	print "testing total_non7s(2, 10): ", total_non7s(2, 10) # 2+3+4+5+6+8+9
	print "testing squares(5): ", squares(5) # 1+4+9+16

def hello():
	return "hello"
	
def nothing():
	return ""

def second_letter(two):
	return two[1]
	
def one_letter(str, num):
	return str[num]
	
def concatenate(silvester, puss_in_boots):
	return silvester + puss_in_boots

def beauty(str):
	return str + " beauty"

def slice_of_life(str):
	return str[2:5]

def slice_of_heaven(str, num):
	return str[num:num+4]

def slice_of_perfection(str, n1, n2):
	return str[n1:n1+n2]

def length(str):
	return len(str)

def main_strings():
	print "testing hello(): ", hello()
	print "testing nothing(): ", nothing()
	print "testing second_letter('cheese'): ", second_letter('cheese')
	print "testing one_letter('random', 5): ", one_letter('random', 5)
	print "testing concatenate('tweety', 'shrek'): ", concatenate('tweety',' shrek')
	print "testing beauty('sleeping'): ", beauty('sleeping')
	print "testing slice_of_life('bread'): ", slice_of_life('bread')
	print "testing slice_of_heaven('heavenly', 3): ", slice_of_heaven('heavenly', 3)
	print "testing slice_of_perfection('trees tacobell mosetracks', 7, 6): ", slice_of_perfection('trees tacobell mosetracks', 7, 6)
	print "testing length('the nile'): ", length('the nile')
		
def short_list():
	return [1, 2, 3]
	
def hollow():
	return []

def third_value(a):
	return a[2]

def one_value(list, pos):
	return list[pos]
	
def add_list(a, b):
	return a + b

def pie(somelist):
	return somelist + [314]
	
def grow_one(listy, item):
	listy.append(item)
	return listy
	
def sub_list(z):
	return z[1: 5]
	
def main_lists():
	print "test short_list(): ", short_list() 
	print "test hollow(): ", hollow()
	a = [ 'alvey', 'kanye', 'trump', 'swift', 'north', 'west']
	b = ['obama', 'will-i-am', 'seinfield', 'fergie', 'elmo', 'wierd-al', 'kermit']
	print "test third_value(a): ", third_value(a)
	print "test one_value(a, 5): ", one_value(a, 5)
	print "test add_lists(a, b): ", add_lists(a, b)
	print "test pie(a): ", pie(a)
	print "test grow_one(b): ", grow_one(b)
	print "test sub_lists(a): ", sub_lists(a)
	
	
	
def main():
	main_function()
	main_arithmetic()
	main_boolean()
	main_boolean_numbers()
	main_conditionals()
	main_counted_loops()
	main_strings()
	main_lists()
	
main()