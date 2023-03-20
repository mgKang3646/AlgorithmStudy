n = int(input())
data = list(map(str,input().split()))

dx = [ 0, 0, -1, 1 ]
dy = [ -1, 1, 0, 0 ]

curX = 1
curY = 1

directType = ['L','R', 'U','D']


def changeDirecToIndex(direcValue):
    for i in range(len(directType)):
        if direcValue == directType[i]:
            return i

for move in data :
    index = changeDirecToIndex(move)
    moveX = dx[index]
    moveY = dy[index]
    
    tmpX = curX + moveX
    tmpY = curY + moveY
    
    if tmpX < 1 or tmpX > n or tmpY < 1 or tmpY > n :
        continue
    else :
        curX += moveX
        curY += moveY
    
print(curX, curY)
        

        
        





            



            


