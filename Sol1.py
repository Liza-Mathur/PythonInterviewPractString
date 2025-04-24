def revString(string, index = None):
    # Gonna use reccursion .
    if index is None:
        index = len(string) - 1
    elif index == -1:
        return ""
    return string[index] + revString(string, index -1)

def revStringLists(string):
    # Using while loop and lists
    l = list(string)
    stringRev = ""
    i = len(string) -1 
    while i >= 0 :
        stringRev += l[i]
        i -= 1
    return stringRev

string = str(input("Enter the string you want to reverse : "))
stringRev = revString(string)
print("Reversed string is - ", stringRev)
stringRevList = revStringLists(string)
print("Reversed string is - ", stringRevList)