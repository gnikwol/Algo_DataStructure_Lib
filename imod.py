def imod(x, mod):
  a = x % mod
  b = mod
  u = 1
  v = 0
  while b:
    t = a // b
    a -= t * b
    a, b = b, a
    u -= t * v
    u, v = v, u
  return u % mod