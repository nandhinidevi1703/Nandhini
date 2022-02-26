#user def funtions
#Write function to concatenate three strings
def concatenate_string(s1, s2, s3):
    return s1+s2+s3

print(concatenate_string("Python ","programming ","class"))

#Write a function multiply three different integers and return a int
def multiply_three_int(int1, int2, int3):
    return int1*int2*int3

print(multiply_three_int(3,4,5))

#Write a function to check a string is palindrom or not
def palindrome(string):
    rev = string[::-1]
    if rev == string:
        return "palindrome"
    else:
        return "Not palindrome"

print(palindrome(input("enter the string:")))

def middle_string_char(st1):
    return st1[len(st1)//2]

print(middle_string_char(input("enter string")))


def mid_char_vowel(st):
    if st[len(st)//2] in ("a","e","i","o","u"):
        return "vowel"
    else:
        return "Not a vowel"

print(mid_char_vowel(input("enter string: ")))


def prime(n):
    if n > 1:
       for i in range(2,int(n//2)+1):
        if n%i==0:
            return False
    return True

n=int(input("enter the number: "))
print(prime(n))


def factor(a):
    li1 = []
    for i in range(1,a+1):
        if a%i ==0:
            li1.append(i)
        else:
            continue
    else:
        return li1
    
a = int(input("Enter the number: "))
print(factor(a))

def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print(fact(int(input("enter number:"))))


def armNo(n):
    temp = n
    add = 0
    while temp != 0:
        d = temp%10
        add += d**3
        temp = temp/10
    if add == n:
        return True
    else:
        return False

print(armNo(int(input("enter number:"))))

def fib(n,a,b):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            return b
n= int(input("enter value:"))
a=0
b=1
print(fib(n,a,b))





