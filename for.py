x=int(input("enter an integer :"))
enter an integer :42
>>> if x<0:
	x=0
	print("Negative number")
elif x==0:
	print('zero')
elif x==1:
	print('single')
else:
	print('more')

	
output:- more
>>> ----------------------------------------
for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
---------------
for i in range(4,10,2):
	print(i)

	
4
6
8
----------------
for i in range(-50,-100,-10):
	print(i)
-50
-60
-70
-80
-90
-----------
a=["a", "b", "c", "d", "e"]
>>> for i in a:
	print(i , len(a))

	
a 5
b 5
c 5
d 5
e 5
