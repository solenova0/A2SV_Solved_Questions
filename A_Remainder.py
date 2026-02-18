n, x, y = map(int, input().split())
a = input()

operations = 0
tail = a[-x:]
operations += tail.count('1')

if a[-y-1] == '0':
    operations += 1
else:
    operations -= 1

print(operations)



