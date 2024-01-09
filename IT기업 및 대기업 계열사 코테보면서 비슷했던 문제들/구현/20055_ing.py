import copy
N,K = map(int, input().split())
belt = list(map(int, input().split()))
robot = [0]*2*N
new_belt = [0]*2*N
new_robot = [0]*2*N
stack = 0
destroy = 0
i = 2*N-1
k=0
r = 1
cnt = 0
while True:
    # 1번 작업
    if k == 5:
        break
    for j in range(2*N):
        if j == 2*N-1:
            new_belt[0] = belt[j]
            new_robot[0] = robot[j]
            new_robot[j] = 0
        else:
            new_belt[j+1] = belt[j]
            new_robot[j+1] = robot[j]
            # new_robot[j] = 0
            if robot[j+1] == N-1:
                robot[j+1] = 0
    belt = copy.deepcopy(new_belt)
    robot = copy.deepcopy(new_robot)

    # 2번 작업
    for i in range(N-2,-1,-1):
        if robot[i]>0 and belt[i+1]>0 and robot[i+1] == 0:
            robot[i] = 0
            belt[i+1]-1
            if belt[i+1] == 0:
                cnt += 1

    # 3번 작업
    if belt[2*N-1] > 0:
        robot[2*N-1] = 1

    # 4번 작업
    if cnt == K:
        print(k)
        break
    # robot = copy.deepcopy(new_robot)
    print('ㄹㅂ',new_robot)
    print('로봇',robot)
    print('벨트',belt)
    print(' ')
    k+=1
    
    
    
    