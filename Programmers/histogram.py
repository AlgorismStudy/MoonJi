def solution(H):
    # 가능한 높이 구하기
    heights = list(set(H))
    answer = []

    for h in heights:
        t_h = 0     # Th의 합
        count = 0   # 같은 높이가 연속될 경우 카운트

        for i in range(len(H)):
            if H[i] == h:
                # 해당 높이보다 좌우로 더 높은 높이의 사각형이 연속으로 존재하는 인덱스
                l, r = find_lr(i, i, i, H)
                t_h += cal_th(i-l, r-i)

                if i+1 < len(H):
                    # 같은 값이 연속되는 경우 예외 처리
                    if H[i] == H[i+1]:
                        count += 1
                    if count > 0 and H[i] != H[i+1]:
                        l, r = find_lr(i-count, i, i, H)
                        t_h += cal_th(i-count-l, r-i)
        answer.append([h, t_h])
                    
    return answer

# 가운데 값을 기준으로 좌우로 큰 값의 개수에 따라 꽉 찬 사각형 갯수 구하기
def cal_th(l, r):
    v = min(l, r)
    result = v * (v + 1) + (abs(l-r) + 1) * (v + 1)
    return result

# 기준값보다 큰 값이 연속되는 인덱스 찾기
def find_lr(l, r, i, H):
    while True:
        new_l = l - 1
        if new_l >= 0 and H[new_l] > H[i]:
            l = new_l
        else:
            break
    while True:
        new_r = r + 1
        if new_r < len(H) and H[new_r] > H[i]:
            r = new_r
        else:
            break

    return [l, r]

print(solution([1,2,3,4,5,3,3,2,2,1,2,3,4,4,2,1,2,3,4,3,2,2,1,2,2,2,1,3,4,5,6,4,3]))