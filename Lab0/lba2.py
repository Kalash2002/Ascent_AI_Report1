from collections import deque
# solution using bfs of this problems lets solve this using queue
# defining queue
queue = deque()
STARTSTATE = ['A','B','C','_','X','Y','Z']    #this is our start state
GOALSTATE = ['X','Y','Z','_','A','B','C']     # this is our goal state
left = ['A','B','C']
right = ['X','Y','Z']
path = []
parent = {}                           # this is our parent that contain
solpath = []
# print("before size is ",len(path))
def BFS(s,queue,path,count):
    queue.append(s)
    flag = False
    while queue:
        top = queue.pop()   #poping first element and traverse

        if(top==GOALSTATE):
            # print("hello top",parent['X Y Z _ A B C'])
            print("solution found after visiting ",count," nodes in search tree")
            solpath.append(parent['X Y Z _ A B C'])
            Flag = True
            return True
            # return True

        for i in range(len(top)):
            if(top[i]=='_'):

                if((i-1)>=0 and (top[i-1] in left)):
                    newpath = top.copy()
                    str1 = " "
                    str2 = " "
                    newpath[i-1],newpath[i] = newpath[i],newpath[i-1]
                    parent[str1.join(newpath)] = str2.join(top)
                    queue.append(newpath)
                    count = count +1

                if((i+1)<=(len(STARTSTATE)-1) and (top[i+1] in right)):
                    newpath = top.copy()
                    str1 = " "
                    str2 = " "
                    newpath[i+1],newpath[i] = newpath[i],newpath[i+1]
                    parent[str1.join(newpath)] = str2.join(top)
                    queue.append(newpath)
                    count = count +1


                if((i-2)>=0 and (top[i-2] in left)):
                    newpath = top.copy()
                    str1 = " "
                    str2 = " "
                    newpath[i-2],newpath[i] = newpath[i],newpath[i-2]
                    parent[str1.join(newpath)] = str2.join(top)
                    queue.append(newpath)
                    count = count +1

                if((i+2)<=(len(STARTSTATE)-1) and (top[i+2] in right)):
                    newpath = top.copy()
                    str1 = " "
                    str2 = " "
                    newpath[i+2],newpath[i] = newpath[i],newpath[i+2]
                    parent[str1.join(newpath)] = str2.join(top)
                    queue.append(newpath)
                    count = count +1
    if (Flag):
        return True
    return False


# %%
def printsolution(last):
    if(last=='A B C _ X Y Z'):
        print(last)
        return
    printsolution(parent[last])
    print(last)



# %%
# queue.append(list(STARTSTATE))
# print("Finding Path using BFS --> ")
if(BFS(STARTSTATE,queue,path,0)):
    # print("hello")
    # for (i,j) in parent.items():
        # print(i," -- ",j)
    count = 1
    print("hello solution found ")
    for i in solpath:
        print("\n \n")
        print("solution ->",count,"\n")
        count = count +1
        printsolution(i)
        print('X Y Z _ A B C')
