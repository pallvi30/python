Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=int(input("enter an integer :"))
enter an integer : 42
>>> if x<0:
	x=0
	print("Negative number")
elif x==0
SyntaxError: invalid syntax
>>> elif x==0:
	
SyntaxError: invalid syntax
>>> x=int(input("enter an integer :"))
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

	
more
>>> for i in words [:]:
	if len(1)>6:
		words.insert(0,i)

		
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    for i in words [:]:
NameError: name 'words' is not defined
>>> 
>>> NameError: name 'words' is not defined
SyntaxError: invalid syntax
>>> for i in 10
SyntaxError: invalid syntax
>>> for i in 10:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    for i in 10:
TypeError: 'int' object is not iterable
>>> for i in range(10)
SyntaxError: invalid syntax
>>> for i in range(10):
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
>>> 
KeyboardInterrupt
>>> for i in range(5,10)
SyntaxError: invalid syntax
>>> for i in range(5,10):
	print(i)

	
5
6
7
8
9
>>> for i in range(4,10,2):
	print(i)

	
4
6
8
>>> for i in range(-50,-100, 10)
SyntaxError: invalid syntax
>>>  for i in range(-50,-100, 10):
	
SyntaxError: unexpected indent
>>>  for i in range(-50,-100, -10):
	
SyntaxError: unexpected indent
>>> for i in range(-50,-100,-10):
	print(i)

	
-50
-60
-70
-80
-90
>>> 
KeyboardInterrupt
>>> for i in range(-50,-100,10):
	print(i)

	
>>> for i in range(-50,-100,10):
	print(i)

	
>>> for i in range(-50,-100,10):
	print(i)

	
>>> a=["a", "b", "c", "d", "e"]
>>> for i in range(len(a))
SyntaxError: invalid syntax
>>> -50
-6
-80





-90
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> a=["a", "b", "c", "d", "e"]
>>> for i in a:
	print(i , len(a))

	
a 5
b 5
c 5
d 5
e 5
>>> list=[0,1,3,4,5,6,7,8]
>>> list
[0, 1, 3, 4, 5, 6, 7, 8]
>>> if list[0]==0:
	print(" this number is ZERO")

	
 this number is ZERO
>>> if list[0]==0:
	print(" this number is ZERO")
elif list[1]==1:
	print("this number is One")

 this number is ZERO
>>> for in in list
SyntaxError: invalid syntax
>>> for in i list:
	
SyntaxError: invalid syntax
>>> range(10)
range(0, 10)
>>> print(range(0, 10))
range(0, 10)
>>> 
>>> range(0,10)
range(0, 10)
>>> range(10)
range(0, 10)
>>> for i in range(0,10):
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
>>> list=[1,2,3,4,5,6,7,8,9]
>>> for i in list:
	print(i)

	
1
2
3
4
5
6
7
8
9
>>> list["Apple", "Mango", 1,2,3,"Rupali", 4, 5, "Cat"]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    list["Apple", "Mango", 1,2,3,"Rupali", 4, 5, "Cat"]
TypeError: list indices must be integers or slices, not tuple
>>> 
KeyboardInterrupt
>>> list=["Apple", "Mango", 1,2,3,"Rupali", 4, 5, "Cat"]
>>> for i in list:
	print(i)

	
Apple
Mango
1
2
3
Rupali
4
5
Cat
>>> name="My name is pallvi Arora"
>>> for i in name
SyntaxError: invalid syntax
>>> for i in name:
	print(i)

	
M
y
 
n
a
m
e
 
i
s
 
p
a
l
l
v
i
 
A
r
o
r
a
>>> for i in range(10):
	if n==6
	
SyntaxError: invalid syntax
>>> for i in range(10):
	if n==6:
		break
	print(n ,end-',')

	
Traceback (most recent call last):
  File "<pyshell#96>", line 2, in <module>
    if n==6:
NameError: name 'n' is not defined
>>> for i in range(10):
	if n==6:
		break
	print(n ,end, ',')

	
Traceback (most recent call last):
  File "<pyshell#98>", line 2, in <module>
    if n==6:
NameError: name 'n' is not defined
>>> for i in range(10):
	if n==6:
		break
	print(n)

	
Traceback (most recent call last):
  File "<pyshell#101>", line 2, in <module>
    if n==6:
NameError: name 'n' is not defined
>>> for i in range(10):
	if n==6:
		break
	print(n)

	
Traceback (most recent call last):
  File "<pyshell#104>", line 2, in <module>
    if n==6:
NameError: name 'n' is not defined
>>> for n in range(10):
	if n==6:
		break
	print(n)

	
0
1
2
3
4
5
>>> for n in range(10):
	if n==6:
		continue
	print(n)

	
0
1
2
3
4
5
7
8
9
>>> list.count(list)
0
>>> vegetables= ["a,a,1,2,3,,1,4,s,1,32,e]
		 
SyntaxError: EOL while scanning string literal
>>> a=["a,a,1,2,3,,1,4,s,1,32,e"]
		 
>>> a.count('a')
		 
0
>>> a=["a", "b", 1,2,3,4,"f","f","a"]
		 
>>> a
		 
['a', 'b', 1, 2, 3, 4, 'f', 'f', 'a']
>>> a.count('a')
		 
2
>>> list.append(a)
		 
>>> list.append('a')
		 
>>> a
		 
['a', 'b', 1, 2, 3, 4, 'f', 'f', 'a']
>>> a.append('a')
		 
>>> a
		 
['a', 'b', 1, 2, 3, 4, 'f', 'f', 'a', 'a']
>>> a.index('a')
		 
0
>>> a.index('a',3)
		 
8
>>> a.pop()
		 
'a'
>>> a.sort()
		 
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> vegetables=["tomato", "potato", "onion", "raddish", "
