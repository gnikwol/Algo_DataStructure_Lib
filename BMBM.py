def berlekamp_massey(a, mod):
  b, c = [1], [1]
  l, m, p = 0, 1, 1
  for i in range(len(a)):
    d = a[i]
    for j in range(1, l + 1):
      d += c[j] * a[i - j]
      d %= mod
    if d == 0:
      m += 1
      continue
    oldc = c[: ]
    q = pow(p, mod - 2, mod) * d % mod
    for j in range(len(b)):
      if j + m >= len(c): c += [0] * (j + m + 1 - len(c))
      c[j + m] -= q * b[j]
      c[j + m] %= mod
    if 2 * l <= i:
      b = oldc
      l, m, p = i + 1 - l, 1, d
    else: m += 1
  return [-x % mod for x in c[1:]]

class Convolution:
  def __init__(self):
    self.mod = 998244353
    self.g = 3
    self.ig = 332748118
    self.W = [pow(self.g, (self.mod - 1) >> i, self.mod) for i in range(24)]
    self.iW = [pow(self.ig, (self.mod - 1) >> i, self.mod) for i in range(24)]
  def fmt(self, k, a):
    W = self.W
    mod = self.mod
    for l in range(k, 0, -1):
      d = 1 << l - 1
      U = [1]
      for i in range(d):
        U.append(U[-1] * W[l] % mod)
      
      for i in range(1 << k - l):
        for j in range(d):
          s = i * 2 * d + j
          a[s], a[s + d] = (a[s] + a[s + d]) % mod, U[j] * (a[s] - a[s + d]) % mod
    return a
  def ifmt(self, k, A):
    iW = self.iW
    mod = self.mod
    for l in range(1, k + 1):
      d = 1 << l - 1
      for i in range(1 << k - l):
        u = 1
        for j in range(i * 2 * d, (i * 2 + 1) * d):
          A[j + d] *= u
          A[j], A[j + d] = (A[j] + A[j + d]) % mod, (A[j] - A[j + d]) % mod
          u = u * iW[l] % mod
    return A
  def Convolve(self, a, b):
    mod = self.mod
    n0 = len(a) + len(b) - 1
    k = (n0).bit_length()
    n = 1 << k
    a = a + [0] * (n - len(a))
    b = b + [0] * (n - len(b))
    C = [0] * n
    A = self.fmt(k, a)
    B = self.fmt(k, b)
    for i in range(n):
      C[i] = A[i] * B[i] % mod
    c = self.ifmt(k, C)
    invn = pow(n, mod - 2, mod)
    for i in range(n0):
      c[i] = c[i] * invn % mod
    return c[: n0]

fmt = Convolution()
bm = berlekamp_massey(a, mod)

Q = [1] + [-x % mod for x in bm]
P = fmt.Convolve(a[: len(bm)], Q)[: len(bm)]

def bostan_mori(P, Q, n):
  while n:
    Q1 = Q[: ]
    for i in range(1, len(Q), 2): Q1[i] = -Q1[i]
    PQ = fmt.Convolve(P, Q1)
    QQ = fmt.Convolve(Q, Q1)
    P = PQ[n & 1: : 2]
    Q = QQ[0: : 2]
    n >>= 1
  return P[0]

print(bostan_mori(P, Q, K))