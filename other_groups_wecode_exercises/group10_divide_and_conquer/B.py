def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    max_left = 0

    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = float('-inf')
    sum = 0
    max_right = 0

    for i in range(mid + 1, high + 1):
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i

    return max_left, max_right, left_sum + right_sum

def find_max_subarray(arr, low, high):
    if low == high:
        return low, high, arr[low]

    mid = (low + high) // 2

    left_low, left_high, left_sum = find_max_subarray(arr, low, mid)
    right_low, right_high, right_sum = find_max_subarray(arr, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)

    max_subarray = max((left_low, left_high, left_sum), (right_low, right_high, right_sum), (cross_low, cross_high, cross_sum), key=lambda x: x[2])

    return max_subarray

def main():
    n = int(input())
    
    if n > 0:
        arr = [int(x) for x in input().split()]

        low, high, max_sum = find_max_subarray(arr, 0, len(arr) - 1)
        print(max_sum)

if __name__ == "__main__":
    main()