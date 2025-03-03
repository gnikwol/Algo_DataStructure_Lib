class Doubling:
  def __init__(self, k, op, prod, prod1):
    self.k = k
    self.op = op
    self.prod = prod
    self.prod1 = prod1

    self.f = [prod1()]
    self.g = [prod1()]

    for i in range(k):
      self.g.append(op(self.g[-1], prod(self.f[-1], self.g[-1])))
      self.f.append(prod(self.f[-1], self.f[-1]))
  def double(self, n):
    n -= 1
    res = self.prod1()
    i = 0
    while n:
      if n & 1: res = self.prod(res, self.f[i])
      n >>= 1
      i += 1
    return res
  def double_sum(self, n):
    n -= 1
    resg = self.prod1()
    resf = self.prod1()
    i = 0
    while n:
      if n & 1:
        resg = self.op(resg, self.prod(resf, self.g[i]))
        resf = self.prod(resf, self.f[i])
      n >>= 1
      i += 1
    return resg


def op(X, Y):
  x = xoriTransformation(X, mod)
  y = xoriTransformation(Y, mod)
  res = [0] * m
  for i in range(m): res[i] = (x[i] + y[i]) % mod
  return xorTransformation(res, mod)

def prod(X, Y):
  res = [0] * m
  for i in range(m): res[i] = X[i] * Y[i] % mod
  return res

def prod1():
  res = [0] * m
  for x in a: res[x] += 1
  return xorTransformation(res, mod)