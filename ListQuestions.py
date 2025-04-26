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


if __name__=="__main__":
    # 1. sol
    l = [1, 2, [3,4,5], 7,8,[4,5]]
    flattenList(l)