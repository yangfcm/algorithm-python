def solution(expenditure, d):
  count = 0
  maxExpenditure = max(expenditure)
  countArr = [0] * (maxExpenditure + 1)

  for i in range(d):
    countArr[expenditure[i]] += 1
  
  for i in range(d, len(expenditure)):
    median = get_median(d, countArr)
    if expenditure[i] >= median:
      count += 1
    
    countArr[expenditure[i-d]] -= 1
    countArr[expenditure[i]] += 1

  return count

def get_median(d, count):
  median = 0
  countArr = count.copy()

  for i in range(len(countArr)):
    countArr[i] += countArr[i-1]
  
  if d % 2 == 0:
    m1, m2 = d / 2, d / 2 + 1
    for i in range(len(countArr)):
      if m1 <= countArr[i]:
        median += i
        break
    for i in range(len(countArr)):
      if m2 <= countArr[i]:
        median += i
        break
  else:
    m = (d + 1) / 2
    for i in range(len(countArr)):
      if m <= countArr[i]:
        median = i * 2
        break
  return median