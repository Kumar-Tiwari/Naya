poss=0
def col(length,obs,pos):
    global poss
    for i in range(pos[1]+1,length+1):
        if[pos[0],i] in obs:
            break
        else:
            poss+=1
    for i in range(pos[1]-1,0,-1):
        if [pos[0],i] in obs:
            break
        else:
            poss+=1
            
def row(length,obs,pos):
    global poss
    for i in range(pos[0]+1,length+1):
        if [i,pos[1]] in obs :
            break
        else:
            poss+=1

    for i in range(pos[0]-1,0,-1):
        if [i,pos[1]] in obs :
            break
        else:
            poss+=1
def dr(length,obs,pos):
    global poss
    x=pos[0]-1
    y=pos[1]-1
    x1=pos[0]+1
    y1=pos[1]+1
    while y!=0 and x!=0 :
        if [x,y] in obs or x<0 and y<0:
            break
        else:
            poss+=1
        x-=1
        y-=1
    while y!=length+1 and x!=length+1 :
        if [x1,y1] in obs or x1>length or y1>length:
            break
        else:
            poss+=1
            x1+=1
            y1+=1
    
def dl(length,obs,pos):
    global poss
    x=pos[0]+1
    y=pos[1]-1
    x1=pos[0]-1
    y1=pos[1]+1
    while x!= length+1 and y!=0:
        if [x,y] in obs or x>length or y<0:
            break
        else:
            poss+=1
        x+=1
        y-=1
    while x1!=0 and y1!=length+1 :
        if[x1,y1] in obs or x1<0 or y1>length :
            break
        else:
            poss+=1
        x1-=1
        y1+=1
a=list(map(int,input().split(' ')))
pos=tuple(map(int,input().split(' ')))
obs=list()
for i in range(a[1]):
    x=list(map(int,input().split(' ')))
    obs.append(x)
col(a[0],obs,pos)
row(a[0],obs,pos)
dr(a[0],obs,pos)
dl(a[0],obs,pos)
print(poss)

    

