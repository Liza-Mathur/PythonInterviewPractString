str1 = str(input("Enter your string : ")).lower()

for k in str1:
    i = str1.index(k)
    if k in str1[i+1:]:
        print(k)
        break
    if i == len(str1)-1 :
        print("No repeating character found")