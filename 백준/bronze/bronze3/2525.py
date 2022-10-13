ct = list(map(int, input().split()))
nt = int(input())

tmp_minute = ct[1] + nt
add_hour = tmp_minute // 60
r_minute = tmp_minute % 60
tmp_hour = ct[0] + add_hour
tmp = tmp_hour // 24
r_hour = tmp_hour - tmp * 24

print(r_hour, r_minute)
