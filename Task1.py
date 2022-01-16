# data type conversion

print("*******Integer value to float, bool, string conversion********")

a=4

print(a)
print(type(a))

print("int to float conversion")
b=float(a)

print(b)
print(type(b))

print("int to bool conversion")
c=bool(a)    

print(c)
print(type(c))

print("int to string conversion")
d=str(a)    

print(d)
print(type(d))

'''
output:
4
<class 'int'>
int to float conversion
4.0
<class 'float'>
int to bool conversion
True
<class 'bool'>
int to string conversion
4
<class 'str'>
'''

print("********Floating point value to int, bool, string conversion********")
      
a=4.5

print(a)
print(type(a))

print("float to int conversion")
b=int(a)

print(b)
print(type(b))

print("float to bool conversion")
c=bool(a)    

print(c)
print(type(c))

print("float to string conversion")
d=str(a)    

print(d)
print(type(d))


'''
output:
4.5
<class 'float'>
float to int conversion
4
<class 'int'>
float to bool conversion
True
<class 'bool'>
float to string conversion
4.5
<class 'str'>
'''

print("*********Boolean to int, float, string conversion*************")

a=True

print(a)
print(type(a))

print("bool to int conversion")
b=int(a)

print(b)
print(type(b))

print("bool to float conversion")
c=float(a)    

print(c)
print(type(c))

print("bool to string conversion")
d=str(a)    

print(d)
print(type(d))


'''
output:
True
<class 'bool'>
bool to int conversion
1
<class 'int'>
bool to float conversion
1.0
<class 'float'>
bool to string conversion
True
<class 'str'>
'''

print("************String to int, float, bool conversion***********")

a="Hello"

print(a)
print(type(a))

print("string to int conversion")
b=int(a)

print(b)
print(type(b))

print("string to float conversion")
c=float(a)    

print(c)
print(type(c))

print("string to bool conversion")
d=bool(a)    

print(d)
print(type(d))

'''
output:
Hello
<class 'str'>
string to int conversion
Traceback (most recent call last):
  File "C:/Users/nandh/AppData/Local/Programs/Python/Python310/Task1.py", line 133, in <module>
    b=int(a)
ValueError: invalid literal for int() with base 10: 'Hello'

'''
