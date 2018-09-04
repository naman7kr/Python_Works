import random
import sys
for i in range (5):
	print(random.randint(1,10))

n = (input("Enter string"))
if n=="Exit":
	sys.exit()
else :
	print(n)