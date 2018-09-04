import random

def solve():
	n=random.randint(1,100000)
	open("mnrt10.txt","w").close();
	open("mnra10.txt","w").close();
	file = open("mnrt10.txt","a");
	filea=open("mnra10.txt","a");
	#k=int(input())
	k=random.randint(1,100000)
	file.write(str(n))
	file.write(" ")
	file.write(str(k))
	file.write("\n")
	a=list()
	print (k)
	for i in range (0,n):
		#a.append(int(input()))
		a.append(random.randint(1,100000))
		file.write(str(a[i])+" ")
	f=[0]*100005

	for i in range (0,n):
		f[a[i]]=1
	ans=0
	for i in range (0,n):
		if k>=a[i] and f[k-a[i]]==1:
			ans+=1;
	print ('ans:',end=' ')
	ans=int(ans/2)
	print (ans)
	filea.write(str(ans))
	file.close()
	filea.close()
solve()