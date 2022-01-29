''''
Task 1:
write a program to calculate area of circle with radius (float) (collect using input function)#
write a program to calculate perimeter of the cricle with radius (float) (collect it through input function)
'''


pi=3.14
r=float(input("enter the radius of circle:"))
AOC = pi*r*r  #Area of circle
p = 2*pi*r #perimeter
print("Area of circle for radius {} is {}".format(r, AOC))
print("Perimeter of circle for radius {} is {}".format(r, p))

'''
Task 2: String slicing programs
'''

val = "Information*Technology"

print(val[3:10])
print(val[2:5])
print(val[0:10])
print(val[5:-5])
print(val[2:8])
print(val[:8])
print(val[5:])
print(val[8:12])
print(val[:])
print(val[12:5])

print(val[3:10:1])
print(val[3:10:2])
print(val[3:10:3])
print(val[5:-5:1])
print(val[5:-5:2])
print(val[5:-5:5])
print(val[:8:4])
print(val[5::3])
print(val[::2])
print(val[12:5:3])

var = "Python_Interpreter"

print(var[3:10])
print(var[2:5])
print(var[0:10])
print(var[5:-5])
print(var[2:8])
print(var[:8])
print(var[5:])
print(var[8:12])
print(var[:])
print(var[12:5])

print(var[3:10:1])
print(var[3:10:2])
print(var[3:10:3])
print(var[5:-5:1])
print(var[5:-5:2])
print(var[5:-5:5])
print(var[:8:4])
print(var[5::3])
print(var[::2])
print(var[12:5:3])



