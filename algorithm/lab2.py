def assignment(m):
    def value(seta):
        return sum([m[i][seta[i]] for i in range(len(seta))])

    minset = []
    currentset = []
    def findmin(next, m , minset, currentset):
        '''currentset is [0,1,2,3] means job 0,1,2,3 for 4 people '''
        if next != None:
            currentset = currentset + [next]
        if len(currentset) == len(m):
            return currentset 
        else:
            for i in range(len(m)):
                if i not in currentset:
                    currentset2 = findmin(i, m, minset, currentset)
                    if minset == []:
                        minset = currentset2
                    elif value(currentset2) < value(minset):
                        minset = currentset2
        return minset  
        
    minsetresult = findmin(None, m, minset, currentset)
    for i in range(len(m)):
        print("The", i+1, "person does the", minsetresult[i]+1, "job")

m = [[9,2,7,8],[6,4,3,7],[5,8,1,8],[7,6,9,4]]
assignment(m)

