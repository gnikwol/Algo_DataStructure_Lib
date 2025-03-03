#ラグランジュ補間
#y=f(x)のn次多項式をn+1個の異なる入力点から得る
#素数modでできるよ〜やった〜
#出てくるのは各冪乗の係数

def Lagrange(x, y, mod):
  n = len(x) - 1
  for i in range(n + 1):
    t = 1
    for j in range(n + 1):
      if i != j:
        t *= x[i] - x[j]
        t %= mod
    y[i] *= pow(t, mod - 2, mod)
    y[i] %= mod

  p = 0
  q = 1
  dp = [[0] * (n + 2) for _ in range(2)]
  dp[0][0] = -x[0] % mod
  dp[0][1] = 1
  for i in range(1, n + 1):
    for j in range(n + 2):
      dp[q][j] = dp[p][j] * -x[i]
      dp[q][j] %= mod
      if j:
        dp[q][j] += dp[p][j - 1]
        dp[q][j] %= mod
    p, q = q, p

  res = [0] * (n + 1)
  for i in range(n + 1):
    if y[i] == 0: continue
    if x[i]:
      xinv = pow(x[i], mod - 2, mod)
      res[0] -= dp[p][0] * xinv * y[i]
      res[0] %= mod
      prev = -dp[p][0] * xinv % mod
      for j in range(1, n + 1):
        res[j] -= (dp[p][j] - prev) * xinv * y[i]
        res[j] %= mod
        prev = -(dp[p][j] - prev) * xinv % mod
    else:
      for j in range(n + 1):
        res[j] += dp[p][j + 1] * y[i]
        res[j] %= mod

  return res