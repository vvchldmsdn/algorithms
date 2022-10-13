import sys
sys.stdin = open("4948.txt", "r")


def sieve_result(n):  # n 미만의 소수 개수 반환
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    ans = 0
    for i in range(2, n):
        if sieve[i]:
            ans += 1
    return ans


while True:
    n = int(input())

    if n:
        print(sieve_result(2 * n + 1) - sieve_result(n + 1))
    else:
        break
