def SuffixArray(n, s):
  order = [n - 1 - i for i in range(n)]
  order.sort(key = lambda x: s[x])
  sa = [0] * n
  classes = [0] * n
  for i in range(n):
    sa[i] = order[i]
    classes[i] = S[i]
  k = 1
  while k < n:
    c = classes[: ]
    for i in range(n): 
      if i > 0 and (c[sa[i - 1]] == c[sa[i]]) and ((sa[i - 1] + k) < n) and ((c[sa[i - 1] + k // 2]) == c[sa[i] + k // 2]):
        classes[sa[i]] = classes[sa[i - 1]]
      else: classes[sa[i]] = i
    cc = [i for i in range(n)]
    ss = sa[: ]
    for i in range(n):
      if ss[i] - k >= 0:
        sa[cc[classes[ss[i] - k]]] = ss[i] - k
        cc[classes[ss[i] - k]] += 1
    k <<= 1
  return sa