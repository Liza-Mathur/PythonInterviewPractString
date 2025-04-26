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

    # l3 = [i if i not in l3 for i in l]


if __name__=="__main__":
    # # 1. sol
    # l = [1, 2, [3,4,5], 7,8,[4,5]]
    # flattenList(l)
    # # 2nd Sol
    # l = list(range(1,50,2))
    # print(type(l))
    # rotateList(5, l)
    # # 3rd Sol
    # l = [0, -1, 2, -3, 1]
    # target = -2 
    # targetSumPairs(l, target)
    # Sol 4
    l = [2,56,2,1,7,3,1]
    removeDuplicatesWithOrder(l)
