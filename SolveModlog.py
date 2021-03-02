def SolveModlog(a, b, mod):
  a %= mod
  b %= mod
  m = int(mod ** 0.5 + 0.9) + 1
  s = 1
  for i in range(m):
    if s == b: return i
    s = s * a % mod
        
  inva = pow(a, mod - 2, mod)
  am = pow(a, m, mod)
  D = {}
  k = b
  for i in range(m):
    if k not in D: D[k] = i
    k = k * inva % mod
  k = 1
  for i in range(m):
    if k in D: return D[k] + i * m
    k = k * am % mod
  return -1