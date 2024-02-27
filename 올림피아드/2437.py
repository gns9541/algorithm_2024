
def min_unmeasurable_weight(N, weights):
    weights.sort()  # 추의 무게를 오름차순으로 정렬

    min_weight = 1  # 측정할 수 없는 무게 중 최솟값 초기화

    for weight in weights:
        # 현재까지의 추로 측정할 수 있는 무게가 weight보다 작으면
        # 새로운 추(weight)를 추가하여 범위를 확장
        if min_weight >= weight:
            min_weight += weight
        else:
            break

    return min_weight

# 입력 받기
N = int(input())
weights = list(map(int, input().split()))

# 결과 출력
result = min_unmeasurable_weight(N, weights)
print(result)