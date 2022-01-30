'''
Task3:

#Fizz buzz
#Get one number from user
#5
#Multiple of 3 ==> Fizz
#Multiple of 5 ===> buzz
#Multiple of 3 and 5 ===> Fizzbuzz
#None ==> Invalid number
'''

num = int(input("enter number"))
if num%3 == 0 and num%5 == 0:
    print(" Fizzbuzz")
elif num%3 == 0:
    print("Fizz")
elif num%5==0:
    print("buzz")
else:
    print("Invalid number")

'''
Task4:

#Get one mark from student
#mark 0 to 100 otherwise invalid mark

#50 + PASS otherwise FAIL
#90 to 100 ===> A 
#80 to 89 ===> B
#70 to 79 ===> C
#60 to 69 ===> D
#50 to 59 ===> E
'''

m = int(input("enter mark"))
if m>=0 and m<=100:
    if m>=50 and m<=59:
        print("E")
    elif m>=60 and m<=69:
        print("D")
    elif m>=70 and m<=79:
        print("C")
    elif m>=80 and m<=89:
        print("B")
    elif m>=90 and m<=100:
        print("A")
    else:
        print(Fail)
    


'''Task 5: Mark calculation
'''

phy = int(input("Enter physics mark: "))
chem = int(input("Enter Chemistry mark: "))
mat = int(input("Enter Maths mark: "))

if (phy>=0 and phy<=200)and(chem>=0 and chem<=200)and(mat>=0 and mat<=200):
    if phy>=70 and chem>=70 and mat>=70:
        aggregate = phy/4  + chem/4  + mat/2
        if aggregate > 190:
            print("First class")
        elif aggregate > 150:
            print("Second calss")
        elif aggregate > 70:
            print("Third class")
        else:
            print("Fail try again")
    else:
        print("Fail try again")
else:
    print("The mark entered is invalid")
    
        
    
