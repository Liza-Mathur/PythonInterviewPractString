string1 = str(input("Get me your string 1 : "))
string2 = str(input("Get me your string 2 : "))

def checkAnagram(string1, string2):
    string1 = str.replace(string1 , " ", "").lower()
    string2 = str.replace(string2 , " ", "").lower()

    if len(string1) != len(string2):
        return "Not anagram"
    if sorted(string1) != sorted(string2):
        return "Not anagram"
    return "Anagram"

print(checkAnagram(string1, string2))

'''
Solutions
1. make a dictionary of letters and how many times they occur. And check for different values in both the dict. If not fund its anagram
2. Could use counter from collections as well 
'''