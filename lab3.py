list = [3, 7, 1, 4, 9, 2]

def searchList(inList, el, ind=0):
    if ind == len(inList):
        return "Not Found" 
    if inList[ind] == el:
        return ind 
    else:
        return searchList(inList, el, ind + 1)


print(searchList(list, 9))