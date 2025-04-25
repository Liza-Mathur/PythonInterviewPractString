str1 = str(input("Enter first String "))

def checkPalindrome(str1 : str):
    return ''.join(reversed(str1)) == str1

print(checkPalindrome(str1))
