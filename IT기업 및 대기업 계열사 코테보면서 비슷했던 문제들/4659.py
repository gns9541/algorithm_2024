a = ['a','e','o','i','u']
b = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','w','z','y','x','v']
while True:
    word = input()
    if word == 'end':
        break
    flag = 0
    cnt_a = 0
    for i in word:
        if i in a:
            cnt_a += 1        
    if cnt_a == 0:
        print(f'<{word}> is not acceptable.')
    else:
        for i in range(len(word)-2):
            if word[i] in a and word[i+1] in a and word[i+2] in a:
                print(f'<{word}> is not acceptable.')
                flag = 1
                break
            elif word[i] in b and word[i+1] in b and word[i+2] in b:
                print(f'<{word}> is not acceptable.')
                flag = 1
                break
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                if word[i] == 'e' or word[i] == 'o':
                    pass
                else:
                    print(f'<{word}> is not acceptable.')
                    flag = 1
                    break
        if flag == 0:
            print(f'<{word}> is acceptable.')


    # for i in word:
    #     if i in a:
    #         cnt_a += 1
    # if cnt_a == 0:
    #     print(f'<{word}> is not acceptable.')
    # else:
    #     print(f'<{word}> is acceptable.')