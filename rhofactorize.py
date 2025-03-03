#確率で因数分解してくれる
#素因数とは限らない
#10^18程度の大きな数でも高速


from math import gcd
def RhoFactorize(n):
  if n == 1: return []
  d = 1
  xs = [0, n // 2, ((n // 2) ** 2 + 1) % n]
  i = 1
  while d == 1:
    d = gcd(abs(xs[i] - xs[2 * i]), n)
    i += 1
    while i * 2 + 1 > len(xs):
      xs.append((xs[-1] ** 2 + 1) % n)
  if 1 < d < n: return [d] + RhoFactorize(n // d)
  else: return [n]