start = [0, 1, 3, 5, 5, 8]
stop = [6, 2, 4, 7, 9, 9]
def mostactivity(start, stop):
    activity = [(start[i],stop[i]) for i in range(len(start))]
    cost = [a[1]-a[0] for a in activity]
    diction = {}
    for i in range(len(activity)):
        diction[activity[i]] = cost[i]
    #print(diction)
    result = []
    while diction != {}:
        currentkey = min(diction, key=diction.get)
        #print('currentkey', currentkey)
        if result != []:
            check = True
            for act in result:
                if not ((act[0]<currentkey[0] and act[1]<currentkey[0]) or (act[0]>=currentkey[0] and act[1]>=currentkey[1])):
                    check = False
            if check:
                result.append(currentkey)
        else:
            result.append(currentkey)
        del(diction[currentkey])
    print(result)
    return len(result)

print(mostactivity(start,stop))