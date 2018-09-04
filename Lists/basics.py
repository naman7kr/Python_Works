spam = ['cat','dog','123']
print(spam[2]*3)
print(spam[1:])
print(spam[-1])
spam[1]='elephant'
print(spam[:])
spam= spam+['duck','lion']
print (spam*2)
del spam[1]
print (spam)
for i in spam:
	print (i)
print (len(spam))

print ('duck' in spam)
print ('ele' not in spam)
a,b,c,d = spam
print(a)
spam=spam+['duck']
print (spam)
print (spam.index('duck'))
spam+='ab'
print (spam)
spam.append('c')
print (spam)
spam.insert(2,'lol')
print (spam)
spam.remove('duck')
print (spam)
spam.sort()
print (spam)
spam.sort(reverse=True)
print (spam)
spam.append('Z')
spam[2]=spam[2].upper()
spam.sort(key=str.lower)
print(spam)
spam=['aman','rahul']
print (spam)
#tuple
eggs= ('hello', 42,0.5)
print (type(('hello',)))
print (eggs)
print(eggs[0])
#eggs[0]=5 error tuple do not support object assignment
a=tuple(spam)
print(a)
a=list(a)
print(a)
print(list('hello'))
 