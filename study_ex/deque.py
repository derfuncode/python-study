from collections import deque
queue = deque([])

for i in range(10):
    queue.append(i)

print(queue)

print(queue.popleft())
print(queue)

print(queue.pop())
print(queue)

