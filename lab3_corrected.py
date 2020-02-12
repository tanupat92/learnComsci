def Combinations(myset,m):
    q = [] 
    result = []
    for i in myset:
        q.append([i])
    while q != []:
        tmp = q.pop(0)
        if len(tmp)==m:
            result.append(tmp)
        else:    
            for i in myset:
                if i not in tmp:
                    tmp2 = tmp+[i]
                    q.append(tmp2)
    print(result)
    result2 = [set(x) for x in result]
    return [result2[i] for i in range(len(result2)) if result2[i] not in result2[i+1:] ]
print('combinations',Combinations([1,2,3,4],2))
print('combinations',Combinations([1,2,3,4],3))