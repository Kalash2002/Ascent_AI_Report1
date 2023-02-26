# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:39:36 2022

@author: hp
"""

STARTSTATE = ['A','B','C','_','X','Y','Z']
GOALSTATE = ['X','Y','Z','_','A','B','C']
left = ['A','B','C']
right = ['X','Y','Z']
path = []
# path.append(STARTSTATE)
# =============================================================================
#     # print(i," ")
# =============================================================================
l = len(STARTSTATE)
maxdep = 0
def dfs(s,s1,path,count,maxdep):
    # print(path,"\n")
    if (s1==GOALSTATE):
        print("we have reached to last state ",maxdep,"\n")
        print("INITIAL - ",STARTSTATE)
        C = 1
        for i in path:
            print(C ," - ",i,"")
            C = C +1
            # print("\n")
        print("\n")
        return "Answer found"
    for i in range(len(s)):
        if(s1[i]=='_'):
            if((i-1)>=0 and (s1[i-1] in left)):
                s1[i-1],s1[i] = s1[i],s1[i-1]
                path.append(list(s1))
                count = count + 1
                maxdep = max(count,count)
                dfs(s,s1,path,count,maxdep)
#                 count = count - 1
                path.remove(list(s1))
                s1[i],s1[i-1] = s1[i-1],s1[i]


            if((i+1)<=(len(STARTSTATE)-1) and (s1[i+1] in right)):
                s1[i+1],s1[i] = s1[i],s1[i+1]
                path.append(list(s1))
                count = count +1
                maxdep = max(count,count)
                dfs(s,s1,path,count,maxdep)
#                 count = count -1
                path.remove(list(s1))
                s1[i],s1[i+1] = s1[i+1],s1[i]

            if((i-2)>=0 and (s1[i-2] in left)):
                s1[i-2],s1[i] = s1[i],s1[i-2]
                path.append(list(s1))
                count =  count + 1
                maxdep = max(count,count)
                dfs(s,s1,path,count,maxdep)
#                 count = count -1
                path.remove(list(s1))
                s1[i],s1[i-2] = s1[i-2],s1[i]

            if((i+2)<=(len(STARTSTATE)-1) and (s1[i+2] in right)):
                s1[i+2],s1[i] = s[i],s[i+2]
                path.append(list(s1))
                count = count + 1
                maxdep = max(count,count)
                dfs(s,s1,path,count,maxdep)
#                 count = count -1
                path.remove(list(s1))
                s[i],s[i+2] = s1[i+2],s1[i]


print("Findting soliution here by callling function - ")
print(dfs(STARTSTATE,STARTSTATE,path,0,maxdep))





