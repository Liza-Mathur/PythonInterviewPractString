def sol1(str1 : str):
    i = 0
    str2 = ''
    while(i < len(str1)):
        ch = str1[i]
        count = 1
        j = i+1
        # print(i)
        while(j<len(str1)):
            # print("J : ", j)
            if str1[j] == ch:
                count += 1
                j+=1
            else :
                break
        str2 += ch + str(count)
        i = j
    print(str2)    

def sol2(str1 : str):
    prevChar = str1[0]
    count = 1

    str2 = ''
    
    for ch in str1[1:]:
        if ch == prevChar:
            count += 1
        else :
            str2 += prevChar + str(count)
            prevChar = ch
            count = 1
    str2 += prevChar + str(count) 
    print(str2)

str1 = "aabbccccaarrg".lower()
sol1(str1)
sol2(str1)