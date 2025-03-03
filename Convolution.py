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

def xorTransformation(a, mod):
  n = len(a).bit_length() - 1
  A = a[: ]
  for k in range(n):
    i = 1 << k
    for j in range(1 << n):
      if i & j == 0:
        A[j], A[i | j] = A[j] + A[i | j], A[j] - A[i | j]
        A[j] %= mod
        A[i | j] %= mod
  return A

def xoriTransformation(A, mod):
  n = len(A).bit_length() - 1
  a = A[: ]
  for k in range(n):
    i = 1 << k
    for j in range(1 << n):
      if i & j == 0:
        a[j], a[i | j] = a[j] + a[i | j], a[j] - a[i | j]
        a[j] %= mod
        a[i | j] %= mod
  inv = pow(1 << n, mod - 2, mod)
  for i in range(1 << n):
    a[i] *= inv
    a[i] %= mod
  return a