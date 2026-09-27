import heapq

arr = [5, 2, 7, 9, 4]
heapq.heapify(arr) # turns into heap
print(arr)

heapq.heappush(arr, 10)
print(arr)

smallest = heapq.heappop(arr)
print(smallest)

print(arr[0])
