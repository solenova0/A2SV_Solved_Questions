# n = int(input())
# sequences = ""
# for num in range(1 , 10000):
#     sequences += str(num)

#     if len(sequences) >= n:
#         break
# print(sequences[n - 1])
n = int(input())

length = 1
count = 9
start = 1

while n > length * count:
    n -= length * count
    length += 1
    count *= 10
    start *= 10

number = start + (n - 1) // length
digit_index = (n - 1) % length

print(str(number)[digit_index])
