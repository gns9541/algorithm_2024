T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    k=0
    team = list(map(int, input().split()))
    # print(team)
    t = list(set(team))
    delete = []
    for j in range(len(t)):
        cnt = 0
        for i in range(len(team)):
            if team[i] == t[j]:
                cnt += 1
        if cnt<6:
            delete.append(t[j])
    # print(delete)

    fin_lst = []
    for i in team:
        if i in delete:
            pass
        else:
            fin_lst.append(i)
    # print('fin_lst:', fin_lst)

    fin_dict = {}
    for i in range(len(t)):
        cnt = 0
        for j in range(len(fin_lst)):
            if fin_lst[j] == t[i]:
                cnt += j+1
        fin_dict[t[i]] = cnt
    # print(fin_dict)

    filtered_dict = {key: value for key, value in fin_dict.items() if value != 0}
    
    if filtered_dict:
    # 가장 작은 값을 가지는 키(들) 찾기
        min_keys = [key for key, value in filtered_dict.items() if value == min(filtered_dict.values())]
    
    # print("가장 작은 키(들):", min_keys)
    if len(min_keys)>1:
        same_dict = {}
        for i in range(len(min_keys)):
            cnt = 0
            for j in range(len(fin_lst)):
                if min_keys[i] == fin_lst[j]:
                    cnt += 1
                    if cnt == 5:
                        same_dict[min_keys[i]] = j
        min_key = min(same_dict, key=same_dict.get)
        # print(same_dict)
        # print('...',min_key,'.....')
        ans.append(min_key)
    else:
        # print(min_keys[0])
        ans.append(min_keys[0])
    # print('...',ans,k,'...')
    # k+=1
for i in ans:
    print(i)



        
            