maximin = 0
road_num = 0
tunnel_hight = 0
roads = int(input()) # 2
for i in range(roads): # i = 0, 1
    tunnels = int(input()) # 2
    minn = 9999
    for j in range(tunnels): # 0, 1
        hight = int(input()) # 450
        if hight < minn:
            minn = hight # 450
    if minn > maximin:
        maximin = minn # 450
        road_num = i + 1 # 2
print(road_num, maximin)