
if __name__ == '__main__':
    n = int(input())
    list=[]
for i in range(1,n+1):
    list.append(i)
listToStr = ''.join([str(elem) for elem in list])
print(listToStr)
    

