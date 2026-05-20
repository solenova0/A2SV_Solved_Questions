import heapq
heap = []
ans = []
for _ in range(int(input())):
    parts = input().split()
    operation = parts[0]

    if operation == "insert":
        x = int(parts[1])
        heapq.heappush(heap, x)
        ans.append(f"insert {x}")

    elif operation == "removeMin":
        if not heap:
            heapq.heappush(heap, 0)
            ans.append("insert 0")
            
        heapq.heappop(heap)
        ans.append("removeMin")

    else:
        x = int(parts[1])

        while heap and heap[0] < x:
            heapq.heappop(heap)
            ans.append("removeMin")

        if not heap or heap[0] > x:
            heapq.heappush(heap, x)
            ans.append(f"insert {x}")

        ans.append(f"getMin {x}")

print(len(ans))

for op in ans:
    print(op)