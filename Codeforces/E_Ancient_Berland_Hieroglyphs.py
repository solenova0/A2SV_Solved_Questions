import sys
input = lambda: sys.stdin.readline().strip()

# Read input values
len_a, len_b = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

# Store positions of elements in arr_b
position = {}
for index in range(len_b):
    position[arr_b[index]] = index

max_subarray_length = 0
current_sum = 0
right_pointer = 0

for left_pointer in range(len_a):
    if right_pointer < left_pointer:
        right_pointer = left_pointer
        current_sum = 0
    elif left_pointer > 0:
        difference = position[arr_a[left_pointer]] - position[arr_a[left_pointer - 1]]

        if difference < 0:
            difference += len_b

        current_sum -= difference

    if arr_a[left_pointer] not in position:
        continue

    while right_pointer < left_pointer + len_a - 1:
        value = arr_a[(right_pointer + 1) % len_a]
        if value not in position:
            break

        difference = (
            position[arr_a[(right_pointer + 1) % len_a]]
            - position[arr_a[right_pointer % len_a]]
        )

        if difference < 0:
            difference += len_b

        if current_sum + difference >= len_b:
            break

        right_pointer += 1
        current_sum += difference

    sub_array_length = right_pointer - left_pointer + 1
    max_subarray_length = max(sub_array_length, max_subarray_length)

print(max_subarray_length)