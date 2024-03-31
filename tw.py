t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(k):
            if 2 ** j <= i:
                dp[i] += dp[i - 2 ** j]

    print(dp[n])
