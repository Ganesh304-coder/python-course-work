Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> A=20
>>> a
10
>>> A
20
>>> a=10
>>> a=b=c=10
>>> a,b,c=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> a,b=b,a
>>> a
20
>>> b
10
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a
NameError: name 'a' is not defined. Did you mean: 'A'?
