import time


flag1 = True
flag2 = True
cur_hours = 0
hours = [i for i in range(24)]
while True:
    my_hours = hours[(cur_hours + 2) - (((cur_hours + 2) // 24) * 24)]
    print(my_hours, cur_hours)

    if my_hours == 8 and flag1:
        print('!!!8!!!')
        flag1 = False
        flag2 = True
    elif my_hours == 20 and flag2:
        print('!!!20!!!')
        flag1 = True
        flag2 = False
    time.sleep(1)
    cur_hours += 1
    if cur_hours == 24:
        cur_hours = 0