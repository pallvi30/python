Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tel={'pallvi':1029, 'sape' :4120, 'rupali':290}
>>> tel
{'pallvi': 1029, 'sape': 4120, 'rupali': 290}
>>> tel['jack']
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tel['jack']
KeyError: 'jack'
>>> tell['pallvi']
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tell['pallvi']
NameError: name 'tell' is not defined
>>> tel['pallvi']
1029
>>> del tel['pallvi']
>>> tel
{'sape': 4120, 'rupali': 290}
>>> 'guido' in tel
False
>>> 'sape' in tel
True
>>> tel1([('sap' 34),('nisha', 45), ('priti', 78)])
SyntaxError: invalid syntax
>>> tel1([('sap' 34),('nisha', 45), ('priti', 78)])
SyntaxError: invalid syntax
>>> tel1([('sap', 34),('nisha', 45), ('priti', 78)])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    tel1([('sap', 34),('nisha', 45), ('priti', 78)])
NameError: name 'tel1' is not defined
>>> tel1([('sap', 34),('nisha', 45), ('priti', 78)])
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    tel1([('sap', 34),('nisha', 45), ('priti', 78)])
NameError: name 'tel1' is not defined
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

{'sape': 4139, 'guido': 4127, 'jack': 4098}
>>> 
