str1 = str(input("Enter your string : "))

l = []
for k in str1:
    if list.__contains__(l, k):
        pass
    else :
        l.append(k)
    
str2 = ''.join(l)
print(str2)

str3 = ''
for k in str1:
    if k not in str3:
        str3 = str3 + k
    
print("STR3 - ", str3)

# 3rd approach to have a set (not gonna change it to string later as set in unordered), and then check in set if char is present
# Checking in set as its complexity is way less than taht of list's 
seen = set()
output = []

for char in str1:
    if char not in seen:
        seen.add(char)
        output.append(char)

result = ''.join(output)
print(result)


