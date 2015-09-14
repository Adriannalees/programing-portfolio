fahrenheit = 0.0
print "fahrenheit celsius"
while fahrenheit <= 250:
	celsius = ( fahrenheit - 32.0 ) / 1.8 # here we calculate the celsius value
	print "%5.1f &7.2f" % (fahrenheit , celsius)
	fahrenheit = fahrenheit + 25
	