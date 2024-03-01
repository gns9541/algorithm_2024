from collections import deque
wheel = [0]+[deque(input()) for _ in range(4)]
K = int(input())
ways = [list(map(int, input().split())) for _ in range(K)]
# print(ways)
# print(*wheel,sep="\n")
# print('')
# 1 - 2
# 2 - 6,2
# 3 - 6,2
# 4 - 6 
def rotation(i,K):
    t = 0
    k = K
    rot = []
    while True:
        if t == 3:
            break
        if i == 1:
            if wheel[i][2] != wheel[2][6]:
                if k == -1:
                    wheel[2].rotate(1)
                    k = 1
                else:
                    wheel[2].rotate(-1)
                    k = -1
            rot.append(i)
            t+=1
            i = 2
        elif i == 2:
            if t == 0:
                if wheel[i][2] != wheel[3][6]:
                    if k == -1:
                        wheel[3].rotate(1)
                        k = 1
                    else:
                        wheel[3].rotate(-1)
                        k = -1
                    rot.append(1)
                    t+=1
                if wheel[i][6] != wheel[1][2]:
                    if k == -1:
                        wheel[1].rotate(1)
                    else:
                        wheel[1].rotate(-1)
                    rot.append(3)
                    t+=1
                i = 3
            else:
                if 1 not in rot:
                    if wheel[i][6] != wheel[1][2]:
                        if k == -1:
                            wheel[1].rotate(1)
                            k = 1
                        else:
                            wheel[1].rotate(-1)
                            k = -1
                    rot.append(1)
                    t+=1
                    i = 1
                elif 3 not in rot:
                    if wheel[i][2] != wheel[3][6]:
                        if k == -1:
                            wheel[3].rotate(1)
                            k = 1
                        else:
                            wheel[3].rotate(-1)
                            k = -1
                    rot.append(3)
                    t+=1
                    i = 3
        elif i == 3:
            if t == 0:
                if wheel[i][6] != wheel[2][2]:
                    if k == -1:
                        wheel[2].rotate(1)
                        k = 1
                    else:
                        wheel[2].rotate(-1)
                        k = -1
                    rot.append(2)
                    t+=1
                if wheel[i][2] != wheel[4][6]:
                    if k == -1:
                        wheel[4].rotate(1)
                    else:
                        wheel[4].rotate(-1)
                    rot.append(4)
                    t+=1
                i = 2
            else:
                if 2 not in rot:
                    if wheel[i][6] != wheel[2][2]:
                        if k == -1:
                            wheel[2].rotate(1)
                            k = 1
                        else:
                            wheel[2].rotate(-1)
                            k = -1
                    rot.append(2)
                    t+=1
                    i = 2
                elif 4 not in rot:
                    if wheel[i][2] != wheel[4][6]:
                        if k == -1:
                            wheel[4].rotate(1)
                            k = 1
                        else:
                            wheel[4].rotate(-1)
                            k = -1
                    rot.append(4)
                    t+=1
                    i = 4
        elif i == 4:
            if wheel[i][6] != wheel[3][2]:
                if k == -1:
                    wheel[3].rotate(1)
                    k = 1
                else:
                    wheel[3].rotate(-1)
                    k = -1
            rot.append(i)  
            t+=1
            i = 3
    # print(*wheel,sep="\n")
    # print('')
    return


for i in range(K):
    if ways[i][1] == -1:
        wheel[ways[i][0]].rotate(-1)
        rotation(ways[i][0],-1)
    else:
        wheel[ways[i][0]].rotate(1)
        rotation(ways[i][0],1)
    print(*wheel,sep="\n")
    print('')