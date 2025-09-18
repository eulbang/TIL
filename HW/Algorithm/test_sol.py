from collections import deque

n, w, L = map(int, input().split())
truck = deque(list(map(int, input().split())))
bridge_t = deque()
bridge_w = deque()

bridge_t.append(w)
bridge_w.append(truck.popleft())

time = 1
while bridge_t:
    time += 1
    for i in range(len(bridge_t)):
        bridge_t[i] -= 1
    if bridge_t[0] == 0:
        bridge_t.popleft()
        bridge_w.popleft()
    if truck and sum(bridge_w)+truck[0] <= L:
        bridge_t.append(w)
        bridge_w.append(truck.popleft())

print(time)