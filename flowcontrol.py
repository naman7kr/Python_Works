def fun1():
	return True
def leapYear(y):
	if y%400==0 or (y%100!=0 and y%4==0):
		return True
	else: 
		return False

def sumFrom1ton(n):
	
	# for i in range(1,n+1,1):
	# 	sum+=i

	return int((n*(n+1))/2)

n=int(input("Enter a number:"))
print(leapYear(n))
#for python3 cast is necessary but not in python 2.7
# yr=int(input("Enter the Year:"))
# print(leapYear(yr))

