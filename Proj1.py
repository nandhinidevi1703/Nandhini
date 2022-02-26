def getInput():
    optionID = ["exit","List", "Tuple", "Set", "Dict"]
    opt = int(input("Select any one data structure: \n 1.List \n 2.Tuple \n 3.Set \n 4.Dict \n 0:Exit \n Your Option is: "))
    print(dataStructureOption(optionID,opt))
    

def dataStructureOption(optionID,opt):
    while True:
        if optionID[opt] == "List" :
            Li = list()
            Li1 = ["exit","append","pop","clear","count","extend","insert", "reverse","remove","copy","sort","index"]
            return listOp(Li1,Li)
        elif optionID[opt] == "Tuple":
            tu = tuple()
            tu1 = ["exit","add","pop","remove","copy", "clear", "issubset", "difference"]
            return tupleOp(tu1,tu)
        elif optionID[opt] == "Set":
            st = set()
            st1 = ["exit","add","copy","clear","issubset", "difference"]
            return setOp(st1,st)
        elif optionID == "Dict":
            di = dict()
            di1 = {1:"exit",2:"append"}
            return dictOp(di1,di)
        elif optionID == "Exit":
            break
        else:
            break
           

def listOp(Li1,Li):
    Li2 = []
    while True:
        print(Li)
        listOpt = int(input("Select your operation option:\n0:Exit 1:append 2:pop 3:clear 4:count 5:extend 6:insert 7:reverse 8:remove 9:copy 10:sort 11:index \n"))
        if Li1[listOpt] == "append":
            Li.append(int(input("enter the value to append:")))
        elif Li1[listOpt] == "pop":
            Li.pop()
        elif Li1[listOpt] == "clear":
            Li.clear()
        elif Li1[listOpt] == "count":
            Li.count(int(input("please enter the va;ue of count")))
        elif Li1[listOpt] == "extend":
            Li2.append(int(input("Enter the value to add in 2nd list")))
            Li.extend(Li2)
        elif Li1[listOpt] == "insert":
            p = int(input("enter postion:"))
            v = int(input("enter value"))
            Li.insert(p,v)
        elif Li1[listOpt] == "reverse":
            Li.reverse()
        elif Li1[listOpt] == "remove":
            Li.remove(int(input("enter the value to remove:")))
        elif Li1[listOpt] == "copy":
            Li2=Li.copy()
        elif Li1[listOpt] == "sort":
            Li.sort()
        elif Li1[listOpt] == "index":
            val = int(input("enter the value to find index:"))
            Li.index(val)
        elif Li1[listOpt] == "exit":
            return getInput()
        else:
            return getInput()
    
    return Li

def tupleOp(tu1,tu):
    tu2 = tuple()
    tuOpt = int(input("Select your operation option: \n 1:add 2:pop 3:concatenate 4:len 5:sum 6:min 7:max \n"))
    if tu1[tuOpt] == "count":
        tu.count(int(input("enter the value to count")))
    elif tu1[tuOpt] == "pop":
        tu.pop()
    elif Li1[listOpt] == "exit":
        return getInput()
    else:
        return getInput()   

    return tu

def setOp(st1,st):
    st2 = set()
    cp = {}
    while True:
        print(st)
        stOpt = int(input("Select your operation option: \n 0: exit 1:add 2:pop 3:concatenate 4:len 5:sum 6:min 7:max \n"))
        if st1[stOpt] == "add":
            st.add(int(input("enter the value to append:")))
            st2.add(int(input("enter the value to append to set2:")))
        elif st1[stOpt] == "copy":
            cp = st.copy()
            print(cp)
        elif st1[stOpt] == "clear":
            st.clear()
        elif st1[stOpt] == "remove":
            st.remove(int(input("enter the value to remove:")))
        elif st1[stOpt] == "issubset":
            st.issubset(st2)
        elif st1[stOpt] == "difference":
            z = st.difference(st2)
            print(z)
        elif st1[stOpt] == "exit":
            return getInput()
        else:
            return getInput()

    return st

def dictOp(di1,di):
    print(di)
    dtOpt = int(input("Select your operation option: \n 1:append 2:pop 3:concatenate 4:len 5:sum 6:min 7:max \n"))
    if di1[dtOpt] == "append":
        di.append(int(input("enter the value to append:")))
    elif di1[dtOpt] == "pop":
        di.pop()
    elif Li1[listOpt] == "exit":
        return getInput()
    else:
        return getInput()
    return di


    
print("Welcome to Data structure calculator")
getInput()
'''optionID = ["exit","List", "Tuple", "Set", "Dict"]
opt = int(input("Select any one data structure: \n 1.List \n 2.Tuple \n 3.Set \n 4.Dict \n 0:Exit \n Your Option is: "))
print(dataStructureOption(optionID,opt))'''


