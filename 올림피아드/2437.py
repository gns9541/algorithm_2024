
def min_unmeasurable_weight(N, weights):
    weights.sort()  

    min_weight = 1 

    for weight in weights:
        if min_weight >= weight:
            min_weight += weight
        else:
            break

    return min_weight


N = int(input())
weights = list(map(int, input().split()))


result = min_unmeasurable_weight(N, weights)
print(result)