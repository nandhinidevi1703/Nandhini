'''
set task
#Create two empty sets
#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
#check whether set2 is subset of set1 or no ?
#check whether both have common elements are no ?
#remove 8 from set 1 and set 2 ==> find the inferences
#discard 0 from set1 and set2 
#find collection of both sets ===> set1 and set2
'''

a = set()
b = set()
c =(7,8,9,1,2,3,4,5,0)
d = (4,5,6,0)
a.update(c)
b.update(d)
print(b.issubset(a))
print(a.isdisjoint(b))
a.remove(8)
b.discard(8)
print(a)
print(b)

'''
Dictionary:

#create a dictionary
#{1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
#Extract "bobtn" from above dictionary
#Extract "arbeg" from above dictionary
#print all keys in dictionary and convert it into tuple
#Find the average of all numbers available under key "2"
'''

dic = {1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
print(dic[3][1][0::2])
print(dic[3][2][-1:-6:-1])
print(tuple(dic.keys()))
a1 = dic[2]
print(a1)
avg = sum(a1)/len(a1)
print(avg)




