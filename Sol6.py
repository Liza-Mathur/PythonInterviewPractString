import collections
from collections import Counter

def sol1(str1 : str):
    sortedStr = sorted(str1)
    sortedStr = ''.join(sortedStr) 
    i = 0
    while(i < len(sortedStr)):
        ch = sortedStr[i]
        il = sortedStr.rfind(ch)
        count = il - i + 1
        print(ch ," found - ", count, "  times.")
        i = il+1
        pass

def sol2(str1 : str):
    freq = Counter(str1)
    for ch, count in freq.items():
        print(ch ," found - ", count, "  times.")

def sol3(str1 : str):
    # freq = {}
    # for i in str1:
    #     if i in freq:
    #         freq[i] += 1
    #     else : 
    #         freq[i] = 1

    freq = dict.fromkeys(str1, 0)
    for i in str1:
        freq[i] += 1
    
    for ch, count in freq.items():
        print(ch ," found - ", count, "  times.")

str1 = "Aanhkksapkher".lower()
# sol1(str1)
# sol2(str1)
sol3(str1)