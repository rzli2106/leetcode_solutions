import heapq

'''arr = [5, 2, 7, 9, 4]
heapq.heapify(arr) # turns into heap
print(arr)

heapq.heappush(arr, 10)
print(arr)

smallest = heapq.heappop(arr)
print(smallest)

print(arr[0])'''

arr1 = [1, 5, 2, 4, 7, 10]
heapq.heapify(arr1)
print(arr1)

y = 12
heapq.heappush(arr1, y)
x = heapq.heappop(arr1)
print(f"{arr1} popped {x} pushed {y}")

