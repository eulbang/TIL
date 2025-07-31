def perm_no_slice(arr, start_idx):
    '''
    Args:
        arr: 순열을 만들 원본 리스트 (여기서는 변경 가능)
        start_idx: 현재 순열을 만들고 있는 시작 인덱스
    '''
    # 시작해야 하는 인덱스가 내가 선택해야 하는 요소 개수만큼이 되었다.
    # 즉, 시작해야 하는 인덱스가 마지막 번호가 되었다.
    if start_idx == len(arr):
        print(arr)
        return
    # 재귀 호출
    for idx in range(start_idx, len(arr)):
        # start_idx 번째와 idx 번째의 값을 swap
        arr[start_idx], arr[idx] = arr[idx], arr[start_idx]
        perm_no_slice(arr, start_idx + 1)
        arr[start_idx], arr[idx] = arr[idx], arr[start_idx]

# 사용 예시
my_list = [1, 2, 3]
perm_no_slice(my_list, 0)