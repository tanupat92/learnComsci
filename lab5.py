ourlist2 = [10,3,2,5,7,8]
ourlist3 = [11,15]
ourlist4 = [7,7,7,7,7,7,7]
ourlist5 = [1,2,3,4,5,1,2,3,4,5]
ourlist6 = [94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1,
61, 397, 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]
ourlist7 = [347, 49, 608, 460, 67, 856, 21, 526, 552, 412, 761, 286, 481, 441, 598, 933, 462, 328, 92]



def maxdonatehateneighbor(neigbor):    
    def verywell(yahoo, val):
        if len(yahoo) >3 :
            val = val + yahoo[0]
            return max(verywell(yahoo[2:], val),verywell(yahoo[3:], val))
        elif len(yahoo) == 3:
            val = val + yahoo[0] + yahoo[2]
            return val
        elif len(yahoo) == 2:
            val = val + max(yahoo[0],yahoo[1])
            return val
        else:
            return val + yahoo[0]            

    if len(neigbor)>3:
        return max(verywell(neigbor[0:-1],0), verywell(neigbor[1:],0), verywell(neigbor[2:],0))
    else:
        return max(verywell(neigbor[0:-1],0), verywell(neigbor[1:],0))


ourlist = [ourlist2,ourlist3,ourlist4,ourlist5,ourlist6,ourlist7]
def run(function, mylist):
    for i in range(len(mylist)):
        print(i+1, function(mylist[i]))

run(maxdonatehateneighbor, ourlist)



