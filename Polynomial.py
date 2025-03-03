#畳み込めればmultiは計算量が落ちる

#これ
conv = Convolution()
def polymulti(p, q):
  return conv.Convolve(p, q)


def polyadd(p, q):
  res = [0] * max(len(p), len(q))
  for i in range(len(p)): res[i] = p[i]
  for i in range(len(q)):
    res[i] += q[i]
    res[i] %= mod
  return res

def polymulti(p, q):
  res = [0] * (len(p) + len(q) - 1)
  for i in range(len(p)):
    for j in range(len(q)):
      res[i + j] += p[i] * q[j]
      res[i + j] %= mod
  return res

def polymulticonst(p, c):
  for i in range(len(p)): p[i] = p[i] * c % mod
  return p

def polyintegral(p):
  res = [0] * (len(p) + 1)
  for i in range(len(p)): res[i + 1] = p[i] * pow(i + 1, mod - 2, mod) % mod
  return res

def polydifferential(p):
  res = [0] * (len(p) - 1)
  for i in range(1, len(p)): res[i - 1] = p[i] * i % mod
  return res

def polyeval(p, x):
  res = 0
  t = 1
  for i in range(len(p)):
    res += t * p[i]
    res %= mod
    t = t * x % mod
  return res