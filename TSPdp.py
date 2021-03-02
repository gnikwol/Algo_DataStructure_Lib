#頂点数n, infを十分大きな数（初期化の値）, dを隣接行列としてTSPを行う。
#時間計算量O(2^N N^2)

def TSPdp(n, d, inf):
  ln = 1 << n
  dp = [inf] * (ln * n)
  for k in range(n): dp[ln * k + (1 << k)] = 0
  for i in range(1, 1 << n):
    for x in range(n):
      t = i + x * ln
      j = 1
      for y in range(n):
        if i & j:
          j <<= 1
          continue
        tt = (i | j) + y * ln
        if dp[tt] > dp[t] + d[x * n + y]: dp[tt] = dp[t] + d[x * n + y]
        j <<= 1
  return dp