import sys
sys.stdin = open("input.txt")

from collections import deque


# This function append car_num to parking lot or waited
def if_in(i):
    global area_num

    # searching space
    for s in parking_lot:
        area_num += 1
        # if there is space
        if s == {20000:20000}:
            # there is no wait line
            if len(waited) == 0:
                parking_lot[area_num] = {i:area_num}

                #reset
                i = 20000
                break
            #there is wait line
            else:
                waited.append(i)

    # there is no available space
    if i != 20000:
        waited.append(i)


# if there is available area and wait line
def if_wait():
    area_num = -1
    # searching space
    for s in parking_lot:
        area_num += 1
        # if there is space
        if s == {20000:20000}:
            break
    # just make clealy
    priorty = waited.popleft()
    parking_lot[area_num] = {priorty:area_num}


def if_out(i):
    global total_fare
    global area_idx
    # find car's location
    for dict in parking_lot:
        # if that area in car
        if i in dict:
            # store value(area_index)
            area_idx = dict[i]
            break
    # change to available area
    parking_lot[area_idx] = {20000:20000}

    # calculate fare
    fee = per_fare[area_idx]
    wei = weight[i]
    f = fee * wei


    total_fare += f
    if len(waited) > 0:
        if_wait()





T = int(input())
for tc in range(1,T+1):
    # n is number of parking lots, m is number of car use parking area today
    n, m = map(int, input().split())

    # each parking area has separate rate per weight of car
    per_fare = []

    #make result
    total_fare = 0


    # make rate per weight to list, each index mean number of parking space
    for _ in range(n):
        rate = int(input())
        per_fare.append(rate)

    # each car has different weight
    weight = []
    for _ in range(m):
        kg = int(input())
        weight.append(kg)

    # owner know how many car will come parking lots
    # make log cars in and out record
    # car number is index in weight
    # -number mean out, + mean in
    inout_log = deque()
    for _ in range(2*m):
        log = int(input())
        inout_log.append(log)

    # make parking area list, 0 = empty, 1 = filled
    parking_lot = []
    for _ in range(n):
        parking_lot.append({20000:20000})
    # Waiting line
    waited = deque()

    # operation start
    while inout_log:
        # pop to move other list
        i = inout_log.popleft()

        # if in
        if i > 0:
            i = i - 1
            # tracking number if area
            area_num = -1
            if_in(i)

        # if log is minus int
        else:
           i = -i - 1
           area_num = -1
           if_out(i)

    print(f"#{tc} {total_fare}")