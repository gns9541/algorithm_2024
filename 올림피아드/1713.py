N = int(input())
R = int(input())
S = list(map(int, input().split()))

pic = []
students = [0]*(R+1)
time = [0]*(R+1)
cnt = 0
for i in range(R):
    if cnt<N: # 사진첩 남아있을때
        if S[i] not in pic:
            pic.append(S[i])
            students[S[i]]+=1
            cnt += 1
        else:
            students[S[i]]+=1
    else: # 사진첩 꽉 찼을때
        if S[i] not in pic:
            minnum = 10
            for j in range(len(students)):
                if j in pic:
                    minnum = min(minnum,students[j])
            del_lst = []
            for j in range(len(students)):
                if students[j] == minnum:
                    del_lst.append(j)
            # print(del_lst)
            max_time = 0
            max_time_idx = 0
            for j in range(len(time)):
                if j in del_lst:
                    if max_time<time[j]:
                        max_time = time[j]
                        max_time_idx = j

            time[max_time_idx] = 0
            for j in range(len(pic)):
                if pic[j] == max_time_idx:
                    students[pic[j]] = 0
                    pic[j] = S[i]
            # pic.append(S[i])
            students[S[i]]+=1
            print(del_lst)

        else:
            students[S[i]]+=1
    for j in range(len(time)):
        if j in pic:
            time[j]+=1
    
    print(pic)
    print(time)
    print(students)
    print()


pic.sort()
print(*pic)       



