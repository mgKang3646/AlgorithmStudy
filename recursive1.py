
# 데이터 영역
# 1) 상하좌우/대각선 이동 데이터
dx = [-1,-1,-1,1,1,1,0,0]
dy = [-1,0,1,-1,0,1,-1,1]

# 2) Boggle 보드판 데이터
b= [['u','r','l','p','m'],
    ['x','p','r','e','t'],
    ['g','i','a','e','t'],
    ['x','t','n','z','y'],
    ['x','o','q','r','s']]

# 알고리즘 영역
def hasWord(x,y,word,board):
    
    # 조건 영역
    # 1) 좌표는 Boggle 판을 넘어서면 안 된다. 
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
        return False
    # 2) 좌표의 단어가 부합하지 않으면 재귀호출 시퀀스를 종료시킨다.
    elif board[x][y] != word[0] :
        return False
    # 3) 1),2) 조건을 통과하고 이번 재귀호출이 마지막 단어탐색이라면 True를 반환하여 재귀호출 시퀀스를 종료시킨다. 
    elif len(word) == 1 :
        return True
    
    # 상하좌우/대각선 모든 경우를 이동(완전탐색)해야하므로 반복문을 사용
    for di in range(8) :
        nx = x + dx[di]
        ny = y + dy[di]
        
        # 재귀호출 
        if hasWord(nx,ny,word[1:],board): # True를 Return하면 True를 반환하여 재귀호출 시퀀스를 종료시킨다. 
            return True
        
    return False # for문을 모두 돌았는데도 True가 반환되지 못하면 False를 반환하여 재귀호출 시퀀스를 종료시킨다.

# Boggle 보드판 첫 이동 : 완전탐색 ( 반복문 )
for i in range(5):
    for j in range(5):
        if hasWord(i,j,"pretty",b): # 재귀호출의 시퀀스의 Return이 True이면 pretty 단어 탐색 성공, COMPLETE 출력!
            print("COMPLETE")
            
            
            