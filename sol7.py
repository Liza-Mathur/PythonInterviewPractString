def sol1(str1 : str):
    slist = str1.split(" ")
    for i, k in enumerate(slist):
        k = k[0].upper() + k[1:]
        slist[i] = k
    print(" ".join(slist))

def sol2(str1 : str):
    str1 = str1[0].upper() + str1[1: ]
    flag = False
    for i, k in enumerate(str1):
        if flag:
            str1 = str1[:i] + k.upper() + str1[i+1 :]
        if k == ' ':
            flag = True
        else:
            flag = False
    print(str1)

str1 = "My name Is liza mathur."
sol1(str1)
sol2(str1)