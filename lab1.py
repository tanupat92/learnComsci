def hanoi(n, frompeg, topeg):
    if n == 1:
        print("Move disk from peg", frompeg, "to peg", topeg)
        return True
    else:
        unusedpeg =  6-frompeg-topeg
        hanoi(n-1, frompeg, unusedpeg)
        print("Move disk from peg", frompeg, "to peg", topeg)
        hanoi(n-1, unusedpeg, topeg)
        return True
    
hanoi(4,1,3)

def IndexOfMin(array, first, last):
    index = first
    for k in range(first+1, last):
        if array[k] < array[index]:
            index = k 
    return index

def SelectionSort(a,n):
    b = []
    for i in range(0,n):
        j = IndexOfMin(a,i,n)
        k = a[j]
        a.remove(k)
        a.insert(0,k)
        b.append(k)
    return b

print(SelectionSort([19,15,9,11,3,7], 6))

def BruteForceChange(M,c,d):
    smallest = None
    value = 0 
    maxcoin = [list(range(0,(M//c[i])+1)) for i in range(len(c))]
    import itertools
    whole = list(itertools.product(*maxcoin))
    for obj in whole:
        if sum([c[i]*list(obj)[i] for i in range(len(c))]) == M:
            if  smallest == None:
                smallest = list(obj)
            elif sum(obj) < sum(smallest):
                smallest = list(obj)
    return smallest

#BruteForceChange(40,[25,20,10,5,1], 5)  

def runchange():
    M = input("Enter amount of money: ")
    M = int(M)
    a = input("Enter value of coin: ")
    b = a.split(" ")
    c = [int(b[i]) for i in range(len(b))]
    d = input("Enter number of coin type: ")
    small = BruteForceChange(M,c,d)
    print("Here is your change.")
    for i in range(len(c)):
        print(small[i], "coin(s) of", c[i])
runchange()
            