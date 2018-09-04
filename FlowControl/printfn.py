print ('cat','dog',sep=',',end="!")

def span (div):
	return 40/div
try:
	span(0)
except ZeroDivisionError:
	print("Invalid Argument")

