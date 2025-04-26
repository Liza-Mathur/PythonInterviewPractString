from collections import defaultdict

def countWordsUsingDict(s:str):
    s = s.lower().replace(',','').replace('.','').split(" ")
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    print(d)

def invertDict(d:dict):
    # for k,v in d.items():
    #     d[v] = k
    #     del d[k]
    # print(d)

    keys = list(d.keys())
    d2= {}
    values = list(d.values())
    for i in range(len(keys)):
        d2[values[i]] = keys[i]
    print(d2)

    for i in range(len(keys)):
        d[values[i]] = keys[i]
        del d[keys[i]]
    print(d)

def groupAnagrams(words : list):

    sorted_lists = []
    anagram_lists = []

    for i in words:
        isorted = sorted(i)
        if isorted not in sorted_lists:
            sorted_lists.append(isorted)
            anagram_lists.append([i])
        else:
            idx = sorted_lists.index(isorted)
            anagram_lists[idx].append(i)
    print(anagram_lists)

    # To have these in dict directly
    d = defaultdict(list)
    for i in words:
        sortedi = ''.join(sorted(i))
        d[sortedi].append(i)
    print(d)
    # To have them in list
    print(list(d.values()))

def mergeDicts(d:dict, e:dict):
    # App 
    dt = defaultdict(list)
    for k,v in d.items():
        dt[k].append(v)
    for k,v in e.items():
        dt[k].append(v)
    print(dt)

def intersection(s1:set, s2:set):
    set3 = set()
    for k in s1:
        if k in s2:
            set3.add(k)
    print(set3)

    print(set.intersection(s1,s2))

def differenec(s1:set, s2:set):
    
    print(s1.symmetric_difference(s2))

    set3 = set()
    for k in s1:
        if k not in s2:
            set3.add(k)
        else:
            s2.remove(k)
    set3 = set3.union(s2)
    print(set3)



if __name__ == "__main__":
    # sol 1
    s = "My name is Liza Mathur. And liza mathur dont trouble herself. My name. Is that clear is"
    countWordsUsingDict(s)
    d = {'a':1, 'b':2, 'c':3, 'd':4}
    invertDict(d)
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    groupAnagrams(words)
    d = {'a':1, 'b':2, 'c':3, 'd':4}
    e = {'a':3 , 'e':6}
    mergeDicts(d, e)
    s1 = set([1,2,3,4,5])
    s2 = set([7,8,3,5,9])
    intersection(s1,s2)
    differenec(s1,s2)
    