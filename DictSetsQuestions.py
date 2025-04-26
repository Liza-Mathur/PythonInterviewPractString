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


if __name__ == "__main__":
    # sol 1
    s = "My name is Liza Mathur. And liza mathur dont trouble herself. My name. Is that clear is"
    countWordsUsingDict(s)
    d = {'a':1, 'b':2, 'c':3, 'd':4}
    invertDict(d)