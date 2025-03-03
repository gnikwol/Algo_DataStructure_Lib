# もーもー
# Q がでかいときは B = N // int(Q ** 0.5) + 1 とかにしていた
# クエリを処理する順番を返すので、あとは地道に区間伸縮して解く

def Mo(ls, rs, B):
  mx = 0
  mxr = 0
  for i in range(len(ls)):
    l, r = ls[i], rs[i]
    mx, mxr = max(mx, l // B), max(mxr, r)
  bucket = [[] for _ in range(mx + 1)]
  for i in range(len(ls)): bucket[ls[i] // B].append(i)
  order = []
  c = 0
  for b in bucket:
    if c & 1: order += sorted(b, key = lambda x: -rs[x])
    else: order += sorted(b, key = lambda x: rs[x])
    c += 1
  return order