N, K = map(int, input().split())
belt = list(map(int, input().split()))
robot = [0] * 2 * N

def rotate_belt(belt, robot):
    belt = [belt[-1]] + belt[:-1]
    robot = [robot[-1]] + robot[:-1]
    if robot[N - 1]:
        robot[N - 1] = 0
    return belt, robot

def move_robot(belt, robot):
    for i in range(N - 1, 0, -1):
        if robot[i - 1] and not robot[i] and belt[i] > 0:
            robot[i - 1], robot[i] = 0, 1
            belt[i] -= 1
            if i == N - 1:
                robot[i] = 0
    return belt, robot

def put_robot(belt, robot):
    if not robot[0] and belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1
    return belt, robot

step = 1
while True:
    belt, robot = rotate_belt(belt, robot)
    belt, robot = move_robot(belt, robot)
    belt, robot = put_robot(belt, robot)

    cnt = belt.count(0)
    if cnt >= K:
        break

    step += 1

print(step)
