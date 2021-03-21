# linear search algorithm
def linear_search(element, some_list):
    for i in range(len(some_list)):
        if some_list[i] == element:
            return i
    return None


# binary search algorithm
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2

        if some_list[midpoint] == element:
            return midpoint # 함수를 끝내버린다.
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1

    return None


# binary_search(recursion)
def binary_search(left, right):
    if left <= right:
        mid = (left + right) // 2
        if some_list[mid] < target:
            return binary_search(mid+1, right)
        if some_list[mid] > target:
            return binary_search(left, mid-1)
        else:
            return mid
    else:
        return - 1
