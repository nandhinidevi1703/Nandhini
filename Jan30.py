#Using Range function  print multiples of 5 from 0 to 75
for i in range(76):
    if i%5 == 0:
        print(i)
        
#Using Range function  print multiples of 8 from 0 to 72
for j in range(73):
    if j%8 == 0:
        print(j)

#Task2&3
#Li = list()
#Di = dict()

#Task4
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
Li1 = list()

for num in range(num1,num2):
    if num%8 == 0:
        Li1.append(num)

print(Li1)

#Task5
Lis = [3,4,5,2,7,8,9,10]
Li_odd = list()
Li_even = list()
for val in Lis:
    if val%2 == 0:
        Li_even.append(val)
    else:
        Li_odd.append(val)
print(Li_odd)
print(Li_even)

#Task6
a = [-1,-7,8,10,20,21,17,28,-3,0,0]
neg_Li = list()
pos_Li = list()
zero_Li = list()

for a1 in a:
    if a1 < 0:
        neg_Li.append(a1)
    elif a1 == 0:
        zero_Li.append(a1)
    else:
        pos_Li.append(a1)
print(neg_Li)
print(pos_Li)
print(zero_Li)
print("Number of negative element: {}".format(len(neg_Li)))
print("Number of positive element: {}".format(len(pos_Li)))
print("Number of Zero element: {}".format(len(zero_Li)))

#Task7
print(list(range(5)))
print(list(range(1,5)))
print(list(range(5,20)))
print(list(range(-5,5)))
print(list(range(10,100,10)))
print(list(range(10,0,-1)))
print(list(range(-5,5,3)))
print(list(range(10,100,5)))
print(list(range(10,0,-2)))

#Task8
number = int(input("Enter the numebr: "))
if number>1:
    for i1 in range(2, int(number/2)+1):
        if number%i1 == 0:
            print("{} is not prime number".format(number))
            break
    else:
        print("{} is prime number".format(number))
else:
    print("{} is not prime number".format(number))
        
#Task9
num3 = int(input("Enter number to check armstrong no: "))
temp = num3
add = 0

while temp!=0:
    k = temp%10
    add += k**3
    temp = temp // 10
if add == num3:
    print("{} is armstromg number".format(num3))
else:
    print("{} is not a armstromg number".format(num3))

#Task10
fac_num = int(input("Enter the number "))
fact_num = 1
for fact in range(1,fac_num+1):
    fact_num *= fact
print(fact_num)

#Task11
'''fib = int(input("enter number:"))
b=0
c=1'''



        
