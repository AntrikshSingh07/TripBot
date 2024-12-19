#Let's learn!
'''Say I'm a and I went out with 14 other friends named a,b,c,d,....o
I'll be a node of a graph that connets all of us, each edge can be bidirectional, holds a value that can be 
equal to zero. Obviously, the first task is to make all edges unidirectional, by abs(a-b), that'll point 
towards the node that owes more.'''

#Our task is to minimize the number to transactions,i.e to maximize the number of edges with zero value.
def solve(friends,transactions):

    #print(len(transactions))
    #print(transactions[1][2])
    n=len(transactions)
    owes,owed=[0]*len(friends),[0]*len(friends)
    for i in range(n):
        owes[friends.index(transactions[i][0])]+=transactions[i][2]
    for i in range(n):
        owed[friends.index(transactions[i][1])]+=transactions[i][2]
    #print(owes)
    #print(owed)
    #print(owes,owed)
    for i in range(len(friends)):
        if owes[i]-owed[i]>=0:
            owes[i]=(owes[i]-owed[i])
            owed[i]=0
        else:
            owed[i]=(abs(owes[i]-owed[i]))
            owes[i]=0
    #print(owes)
    #print(owed)
    rec=[]
    c=0
    #print(friends[a.index(node)])
    for ind in range(len(friends)):
        c=0
        for i in range(len(owed)):
            if owes[i]!=0 and i!=ind:
                c+=1
        rec.append(c)
    rec.append(c)
    ind=rec.index(min(rec))
    #ind=owes.index(max(owes))
    node=friends[ind]
    x = []
    for i in range(len(owed)):
        if owed[i]!=0 and i!=ind:
            x.append(friends[i] + ' pays '+ friends[ind] +' '+ str(int(owed[i])))
    for i in range(len(owed)):
        if owes[i]!=0 and i!=ind:
            x.append(friends[ind] + ' pays ' + friends[i] + ' ' + str(int(owes[i])))
    return '\n'.join(x)
