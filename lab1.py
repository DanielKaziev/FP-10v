INIT_ARRAY = [1, 5, 4, 45, 55, 100, 75, 90, 33]

def moreThanFifty(a):
    if a >= 50:
        return True
    return False

def findMid(val):
    lenOfArr = len(val)
    if lenOfArr % 2 == 0:
         mid = val[int(lenOfArr/2)]
         return (mid + val[int(lenOfArr/2)-1])/2
    return val[int(lenOfArr/2)]

def sortByASC(val):
    print(list(filter(moreThanFifty, sorted(val))))
    return findMid(list(filter(moreThanFifty, sorted(val))))



print(sortByASC(INIT_ARRAY))
