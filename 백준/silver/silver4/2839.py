N = int(input())  # 11

num_five = N // 5  # 2
left = N - num_five * 5  # 1
flag = 0

while num_five > 0:
    if left % 3 != 0:
        left += 5
        num_five -= 1
    else:
        print(num_five + left // 3)
        flag = 1
        break

if not flag:
    if left % 3 != 0:
        print(-1)
    else:
        print(left // 3)

'''
17
3, 2
2, 7
1, 12
0, 17
'''
