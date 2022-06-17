def solution(list):
  sorted = [0] * len(list)
  max = list[0]
  for el in list:
    if el > max: max = el
  
  count = [0] * (max+1)

  for el in list:
    count[el] += 1
  
  for i in range(1, len(count)):
    count[i] += count[i-1]
  
  for el in list:
    sorted[count[el] - 1] = el
    count[el] -= 1
  
  return sorted