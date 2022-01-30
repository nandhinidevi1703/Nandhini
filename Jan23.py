#list Task

List1 = []
List2= list()
List3= [5,6,7,8]

List1 =List1+List3      #concatenation
print(List1)

List4=[8,9,1,5,6,7,8,1]
Li5 = List1.extend(List4)
print(Li5)              #adding elements

print(Li5.count(8))     #frequency of 8

Mean = sum(Li5)/len(Li5)
print(Mean)

#Median = 

print(sum(Li5)+min(Li5)+max(Li5))

print(Li5)


print(List2)
print(tuple(List2))     #converting string to tuple

#find dulplicate
Li6 = list(dict(dict.fromkeys(Li5)))
print(tuple(Li6))



#tuple Task

t1=(1,4,5,6,7,8)
t2=(5,6,7,8,9)

t1= t1+t2       #concatenation 
print(t1)
t3=tuple(set(t1))
print(t3)       #removing duplicates 

                #common elements between two tuples

print(t1.index(9))#index value of 9
#multiply above elements 3 times








           

    
