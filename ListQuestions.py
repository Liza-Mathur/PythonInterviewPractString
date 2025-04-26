def flattenList(l : list):
    # [1, 2, [3,4,5], 7,8,[4,5]]
    l2 = []
    for k in l :
        # if type(k) == list:
        if isinstance(k, list):
            for i in k:
                l2.append(i)
        else:
            l2.append(k)
    print(l2)

def rotateList(k : int, l: list):
    if k > len(l):
        k = k % len(l)
    # approach 1 : 
    l2 = []
    for i in l[(0-k): ]:
        l2.append(i)
    for i in l[0:(0-k)]:
        l2.append(i)
    print(l2)

    # approach 2 
    l1 = l
    lenl = len(l1)
    l1 = l1[(0-k):] + l1[:(0-k)]
    print(l1)

    # approach 3
    l3 = [l[(i-k)%len(l)] for i in range(len(l))]
    print(l3)

def targetSumPairs(l , t):
    solList=[]

    for i, k in enumerate(l):
        for j in l[i+1:]:
            if k+j == t:
                solList.append((k, j))
        # if i == len(l) - 2:
        #     break
        # Not needed since python is not java (indian mom) jo harr baat pr daate. Python will handel out of bounds exception in slicing
    print(solList)
            
def removeDuplicatesWithOrder(l:list):
    seen = set()
    l2 = []
    for k in l : 
        if k not in seen:
            seen.add(k)
            l2.append(k)
    print("App 1 - ", l2)
    # Can use list here but finding in set is faster than in list - as in not for me but for interpreter

    # l3 = [i if i not in l3 for i in l]
    # How to do it in list comprehensions?

def getLenList(l:list):
    l2 = [len(i) for i in l]
    print(l2)

    # OR
    l2 = []
    for i in l:
        l2.append(len(i))
    print(l2)

    # OR
    i = 0
    while i<len(l):
        l.append(len(l[0]))
        l.remove(l[0])
        i += 1    
    print(l)

def sortTuplesList(l : list):
    # Using dict

    # Using list
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            a = l[i][1]
            b = l[j][1]
            if b < a :
                c = l[i]
                l[i] = l[j]
                l[j] = c

        # print(l)
    print(l)


if __name__=="__main__":
    # # 1. sol
    l = [1, 2, [3,4,5], 7,8,[4,5]]
    flattenList(l)
    # # 2nd Sol
    l = list(range(1,50,2))
    rotateList(5, l)
    # # 3rd Sol
    l = [0, -1, 2, -3, 1]
    # target = -2 
    # targetSumPairs(l, target)
    # # Sol 4
    l = [2,56,2,1,7,3,1]
    removeDuplicatesWithOrder(l)
    # # Sol5
    l = ['apple', 'banana', 'guava', 'lemon', 'watermelon', 'muskmelon', 'appleseeds', '']
    getLenList(l)
    # Sol 6
    # l = [(4,2), (3,1), (3,9), (8,4)]
    l = [(1, 3), (2, 2),(9,1), (4, 1)]
    sortTuplesList(l)

    # l = [1,2,3,4,5]
    # print(l)
    # l[2] = l[4]+l[2]
    # l[4] = l[2]-l[4]
    # l[2] = l[2]-l[4]
    # print(l) # WORKS
