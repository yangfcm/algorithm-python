'''
  Triple Sum: Given 3 arrays of a, b, c of different sizes, find the number of distinct triplets (p, q, r),
  where p is from a, q from b, r from c, satisfying the criteria: p <= q and q >= r.

  Example: a = [3, 5, 7], b = [3, 6], c = [4, 6, 9] -> 4.
  There are 4 such distinct triplets. They are: (3, 6, 4), (3, 6, 6), (5, 6, 4), (5, 6, 6).
'''
def solution(a, b, c):
  a = sorted(list(set(a)), reverse=True)
  b = sorted(list(set(b)), reverse=True)
  c = sorted(list(set(c)), reverse=True)

  count = 0
  ai = 0
  ci = 0
  for bn in b:
    while ai < len(a):
      if a[ai] <= bn: break # The first element from a is less than a particular number from b.
      # So we can stop the loop here, because the remaining must less than bn.
      ai+=1
    
    while ci < len(c):  # Same logic as above.
      if c[ci] <= bn: break;
      ci+=1
    
    count += (len(a) - ai) * (len(c) - ci)

  return count