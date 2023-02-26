# 3m and 3c and 1bot
# can take 1 or 2 at a time in bot
# list of cannible and missinaries
# L[0] = number of missionaries
# L[1] = number of cannibles
from collections import deque

# %%
L = [0,0,0]
R = (3,3,1)
Goal = (0,0,0)
possible = [(1, 0), (0, 1), (1, 1), (0, 2), (2, 0)]
visited = {}
solpath = []
visiteddfs = {}
parent = {}
parentdfs = {}
total = 0;
side = ["Left","Right"]  # here side[0] id pointing to the left side of river and side[1] right

# %%

def checkcondition(cm,cc):
    numbercan_right = 3-cc
    numbermis_right = 3-cm
    return (cm > 0 and cc > cm) or (numbermis_right > 0 and numbercan_right > numbermis_right)


# %%
def bfs():
    flag = False
    q = deque()
    q.append(R)
    visited[R] = True
    cnt = 0
    while q:
        cm,cc,cs = q.pop()
        # checking condition
        if (checkcondition(cm, cc)):
            # we exceed the number
            # so simply continue the process
            continue
        elif ((cm,cc,cs)==Goal):
            print("Total states visited are - ",cnt)
            # we have reached the final state
            flag = True
            solpath.append(parent[(cm,cc,cs)])
            # return True
        op = -1 if cs == 1 else 1
        for p in possible:
            nm,nc,ns = cm + op*p[0] , cc + op*p[1] , int(not cs)
            # print((nm,nc,ns))
            if((nm,nc,ns) not in visited):
                if ((0<= nm <= 3) and (0<= nc <=3)):
                    cnt = cnt + 1
                    visited[(nm,nc,ns)] = True
                    q.append((nm,nc,ns))
                    parent[(nm,nc,ns)] = (cm,cc,cs)


    if(flag):
        return True
    return False

# %%
c = 0
def dfs(cm,cc,cs,count):
    visiteddfs[(cm,cc,cs)] = True
    if (checkcondition(cm, cc)):
        # we exceed the number
        # so simply continue the process
        return False
    elif ((cm,cc,cs)==Goal):
        print('\n \n \n ')
        print("  Total states visited are  - ",count)
            # we have reached the final state
        c = count
        return True
    isolution = False
    op = -1 if cs == 1 else 1
    for p in possible:
        nm,nc,ns = cm + op*p[0] , cc + op*p[1] , int(not cs)
        if((nm,nc,ns) not in visiteddfs):
            if ((0<= nm <= 3) and (0<= nc <=3)):
                parentdfs[(nm,nc,ns)] = (cm,cc,cs)
                count = count + 1
                isolution = isolution or (dfs(nm, nc, ns,count))

                if(isolution):
                    return True

    return isolution
# %%

def printsolution(curridx,total):
    if(curridx==(3,3,1)):
        print("  Total steps are ---  ", total)
        print("\n")
        print(f"  Moves       ->   Left       River      right")
        print("\n");
        m,c,s = curridx
        print(f"  Initial       -> {m,c}   ---****----  {3-m,3-c}")
        print("\n")
        return
    total = total+1
    printsolution(parent[curridx],total)
    m,c,s = curridx
    print(f"  {side[s]} to {side[1-s]} -> {m,c}   ---****----  {3-m,3-c}")


# %%
def printsolutiondfs(curridx,count):
    if(curridx==(3,3,1)):
        # print(curridx)
        print("  Total steps are ---  ", count)
        print("\n")
        print(f"  Moves       ->   Left       River      right")
        print("\n");
        m,c,s = curridx
        print(f"  Initial       -> {m,c}   ---****----  {3-m,3-c}")
        print("\n")
        return
    count = count + 1
    printsolutiondfs(parentdfs[curridx],count)
    m,c,s = curridx
    print(f"  {side[s]} to {side[1-s]} -> {m,c}   ---****----  {3-m,3-c}")


# %%

if(bfs()==True):
    print("\n")
    count = 1
    print("  Solution using bfs ")
    for i in solpath:
        print("\n")
        printsolution(i,1)
    print(f"  left to right -> {0,0}   ---****----  {3,3}")


# %%

if(dfs(3,3,1,0)==True):
    # print("Total states explored are - ",)
    print("\n")
    print("  Solution using dfs  \n")
    printsolutiondfs((0,0,0),0)