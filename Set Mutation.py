"""
TASK:
The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third line contains integer N, the number of other sets.
The next 2* N lines are divided into N parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.
"""


# Enter your code here. Read input from STDIN. Print output to STDO
no_setA=int(input())
setA=set(map(int,input().split()))
noB=int(input())
for i in range(noB):
    cmd=input().split()
    if cmd[0]== "intersection_update":
        setB=set(map(int,input().split()))
        setA.intersection_update(setB)
    elif cmd[0]=="update":
        setB=set(map(int,input().split()))
        setA.update(setB)
    elif cmd[0]=="symmetric_difference_update":
        setB=set(map(int,input().split()))
        setA.symmetric_difference_update(setB)
    elif cmd[0]=="difference_update":
        setB=set(map(int,input().split()))
        setA.difference_update(setB)
    else:
        assert False
print(sum(setA))
