#Prgm 1
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

Add = num1+num2
print("Addition pf two numbert is: {}".format(Add))

#Prgm 2
num3 = int(input("Enter number 1: "))
num4 = int(input("Enter number 2: "))

if num3>num4:
    print("Maximum number is {}".format(num3))
else:
    print("Maximum number is {}".format(num4))

#Prgm 3
fac_num = int(input("Enter a number to find factorial: "))
fact = 1

if fac_num < 0:
    print("no factorial value for negative numbers")
else:
    for i in range(1, fac_num+1):
        fact *= i
        
print("Factial of number {} is {}".format(fac_num,fact))

#Prgm 4
P = int(input("Enter the principle amount: "))
N = int(input("Enter no of years: "))
R = int(input("Enter rate of interest in %: "))

SI = (P*N*R)/100

print("Simple interest is {}".format(SI))

#Prgm 5
P1 = int(input("Enter the principle amount: "))
N1 = int(input("Enter no of years: "))
R1 = int(input("Enter rate of interest in %: "))

A = P1*((1+R1/100)**N1)
CI = A - P1

print("Compound interest is {}".format(CI))

#Prgm 6
arm_num = int(input("Enter the number: "))
temp = arm_num
add_sum = 0

while temp != 0:
     digit = temp % 10
     add_sum += digit ** 3
     temp //= 10

if add_sum == arm_num:
    print("Number is Armstrong number")
else:
    print("Number is not armstrong")

#Prgm 7
r = int(input("Enter radius:"))
pi = 3.14
area = pi*r*r
print("Area of circle for radius {} is {}".format(r, area))

#Prgm 8
r1 = int(input("Enter start interval: "))
r2 = int(input("Enter end interval: "))
Li = list()

for num in range(r1, r2+1):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           Li.append(num)
print(Li)

#Prgm 9
p_num = int(input("Enter number:"))
if p_num > 1:
       for i in range(2, p_num):
           if (p_num % i) == 0:
               print("number is not prime")
               break
            
       else:
           print("number is prime")

#Prgm 10
n = int(input("Number is : "))
a = 0
b = 1
if n < 0:
    print("Incorrect input")
elif n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(b)

#Prgm 11
st =input("Enter character: ")
print(ord(st))

#Prgm 12
N = int(input("enter value: "))
Sq_sum = 0
for i in range(1, N+1):
    Sq_sum += i**2
print(Sq_sum)

#Prgm 13
N1 = int(input("enter value: "))
cube_sum = 0
for i in range(1, N1+1):
    cube_sum += i**3
print(cube_sum)

#prgm14
Li = [2,4,3,6,5,8,7,9]
even = []
for i in Li:
    if i%2 == 0:
        even.append(i)
        
print(even)


# prgm15
Li = [2,4,3,6,5,8,7,9]
odd = []
for i in Li:
    if i%2 != 0:
        odd.append(i)

print(odd)

#prgm16
r =[]
n1 = int(input())
n2 = int(input())
for i in range(n1,n2+1):
    if i%2 == 0:
        r.append(i)
print(r)

#prgm17
r1 =[]
n1 = int(input())
n2 = int(input())
for i in range(n1,n2+1):
    if i%2 != 0:
        r1.append(i)
print(r1)

#prgm18
Li1 = [2,6,8,-1,-5,5,-8]
posLi = []
for i in range(len(Li1)):
    if Li1[i] > 0:
        posLi.append(Li1[i])
print(posLi)


#prgm19
Li1 = [2,6,8,-1,-5,5,-8]
negLi = []
for i in range(len(Li1)):
    if Li1[i] < 0:
        negLi.append(Li1[i])
print(negLi)

#prgm20

l1 = [11, 5, 17, 18, 23, 50]
 
for i in l1:
    if i % 2 == 0:
        l1.remove(i)
 
print(l1)

#prgm21

or_list = [5, 6, [], 3, [], 9]

for ele in or_list:
    if ele == []:
        or_list.remove(ele)

print(or_list)

#prgm22
t = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'),()]

for ele in t:
    if ele == ():
        t.remove(ele)

print(t)

#prgm23
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
count = 0
elmt = int(input("enter element"))
for i in lst:
    if i == elmt:
        count = count+1
print(count)

#prgm24
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
lst1 = []
lst1 = lst.copy()
print(lst1)

#prgm25
ls = [2,3,4,5,6]
val = 0
for i in range(len(ls)):
    ls[i] = val + ls[i]
    val = ls[i]

print(ls)

#prgm26
ls1 = [11,12,13,25]
res = []
for ele in ls1:
    val = 0
    for digit in str(ele):
        val += int(digit)
    res.append(val)
print(ls1)
print(res)
    
#prgm27
Tuple1 = ("A", 1, "B", 2, "C", 3)
print("Size of Tuple1: " + str(Tuple1.__sizeof__()) + "bytes")

#prgm28
list1 = [1, 2, 5, 6]
res = [(val, pow(val, 3)) for val in list1]
print(res)

#prgm29
test_list = [5, 6, 7]
print("The original list is : " + str(test_list))
test_tup = (9, 10)
test_list += test_tup
print("The container after addition : " + str(test_list))

#prgm30
s = " abc abc abc hello"
res = {key: s.count(key) for key in s.split()}
print(res)

#prgm31
s = input("enter string")
txt = s[::-1]
print(txt)
if s == txt:
    print("palindrome")
else:
    print("non palindrome")

#prgm32
def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")
            
string = input("string1 ")
sub_str =input("string2 ")
check(string, sub_str)

#prgm33
test = input("enter string")
print("The original string is : " + test)
res = test.replace("_", " ").title().replace(" ", "")
print("The String after changing case : " + str(res)) 

#prgm34
s = input("enter to find length: ")
print(len(s))

#prgm35
def printWords(s):
    s = s.split(' ') 
    for word in s: 
        if len(word)%2==0:
            print(word) 
s = input("string")
printWords(s)

#prgm36
s = input("enter string")
txt = s[::-1]
print(txt)

#prgm37
def removeDuplicate(str):
    s=set(str)
    s="".join(s)
    print("Without Order:",s)
    t=""
    for i in str:
        if(i in t):
            pass
        else:
            t=t+i
        print("With Order:",t)
      
str="geeksforgeeks"
removeDuplicate(str)

#prgm38
test_str = input("enter string")
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = min(all_freq, key = all_freq.get)
print(res)

#prgm39
test_str = input("enter string")
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = max(all_freq, key = all_freq.get)
print(res)

#prgm40
Li = [1,2,3,4]

l = len(Li)
temp = Li[0]
Li[0] = Li[l-1]
print(Li[0])
Li[l-1]=temp
print(Li)

#prgm41
Li1 = [2,5,7,9,1]
print(Li1)
p1 = int(input())
p2 = int(input())

temp = Li1[p1-1]
Li1[p1-1] = Li1[p2-1]
Li1[p2-1]= temp

print(Li1)

#prgm42
print(len(Li))

#prgm43
T1 = [23,45]
T1.clear()

#prgm44
Li1.reverse()
print(Li1)

#prgm45
s_Li = [1,2,3,4,5]
sum_list = 0

for i in range(len(s_Li)):
    sum_list += s_Li[i]

print(sum_list)

#prgm46
Li2 = [1,2,3,4,5]
mul_list = 1

for i in range(len(Li2)):
    mul_list *= Li2[i]
    
print(mul_list)

#prgm47
a = [2,5,1,6,9]
leng = len(a)
small = a[0]

for i in range(leng):
    if small > a[i]:
        small = a[i]

print(small)

#prgm48
b = [2,5,1,6,9]
leng = len(b)
large = b[0]

for i in range(leng):
    if large < a[i]:
        large = a[i]

print(large)

#prgm49
c = [8,4,7,2,1]
d = []
n=3
leng = len(c)
for j in range(0,n):
    large = c[0]
    for i in range(leng):
        if c[i] > large:
            large = c[i]

    c.remove(large)
    d.append(large)
    
print(d)

#prgm50

or_list = [5, 6, [], 3, [], 9]

for ele in or_list:
    if ele == []:
        or_list.remove(ele)

print(or_list)

#prgm51
t = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'),()]

for ele in t:
    if ele == ():
        t.remove(ele)

print(t)

#prgm52
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
count = 0
elmt = int(input("enter element"))
for i in lst:
    if i == elmt:
        count = count+1
print(count)

#prgm53
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
lst1 = []
lst1 = lst.copy()
print(lst1)

#prgm54
ls = [2,3,4,5,6]
val = 0
for i in range(len(ls)):
    ls[i] = val + ls[i]
    val = ls[i]

print(ls)

#prgm55
ls1 = [11,12,13,25]
res = []
for ele in ls1:
    val = 0
    for digit in str(ele):
        val += int(digit)
    res.append(val)
print(ls1)
print(res)
    
#prgm56
Tuple1 = ("A", 1, "B", 2, "C", 3)
print("Size of Tuple1: " + str(Tuple1.__sizeof__()) + "bytes")

#prgm57
list1 = [1, 2, 5, 6]
res = [(val, pow(val, 3)) for val in list1]
print(res)

#prgm58
test_list = [5, 6, 7]
print("The original list is : " + str(test_list))
test_tup = (9, 10)
test_list += test_tup
print("The container after addition : " + str(test_list))

#prgm59
s = " abc abc abc hello"
res = {key: s.count(key) for key in s.split()}
print(res)

#prgm60
s = input("enter string")
txt = s[::-1]
print(txt)
if s == txt:
    print("palindrome")
else:
    print("non palindrome")

#prgm61
def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")
            
string = input("string1 ")
sub_str =input("string2 ")
check(string, sub_str)

#prgm62
test = input("enter string")
print("The original string is : " + test)
res = test.replace("_", " ").title().replace(" ", "")
print("The String after changing case : " + str(res)) 

#prgm63
s = input("enter to find length: ")
print(len(s))

#prgm64
def printWords(s):
    s = s.split(' ') 
    for word in s: 
        if len(word)%2==0:
            print(word) 
s = input("string")
printWords(s)

#prgm65
s = input("enter string")
txt = s[::-1]
print(txt)

#prgm66
def removeDuplicate(str):
    s=set(str)
    s="".join(s)
    print("Without Order:",s)
    t=""
    for i in str:
        if(i in t):
            pass
        else:
            t=t+i
        print("With Order:",t)
      
str="geeksforgeeks"
removeDuplicate(str)

#prgm67
test_str = input("enter string")
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = min(all_freq, key = all_freq.get)
print(res)

#prgm68
test_str = input("enter string")
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = max(all_freq, key = all_freq.get)
print(res)

#prgm69
Li = [1,2,3,4]

l = len(Li)
temp = Li[0]
Li[0] = Li[l-1]
print(Li[0])
Li[l-1]=temp
print(Li)

#Prgm70
arm_num = int(input("Enter the number: "))
temp = arm_num
add_sum = 0

while temp != 0:
     digit = temp % 10
     add_sum += digit ** 3
     temp //= 10

if add_sum == arm_num:
    print("Number is Armstrong number")
else:
    print("Number is not armstrong")

#Prgm71
r = int(input("Enter radius:"))
pi = 3.14
area = pi*r*r
print("Area of circle for radius {} is {}".format(r, area))

#Prgm 72
r1 = int(input("Enter start interval: "))
r2 = int(input("Enter end interval: "))
Li = list()

for num in range(r1, r2+1):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           Li.append(num)
print(Li)

#Prgm 73
p_num = int(input("Enter number:"))
if p_num > 1:
       for i in range(2, p_num):
           if (p_num % i) == 0:
               print("number is not prime")
               break
            
       else:
           print("number is prime")

#Prgm 74
n = int(input("Number is : "))
a = 0
b = 1
if n < 0:
    print("Incorrect input")
elif n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(b)

#Prgm 75
st =input("Enter character: ")
print(ord(st))

