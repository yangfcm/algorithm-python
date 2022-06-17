def solution(arr):
  for i in range(len(arr)):
    indexOfMin = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[indexOfMin]:
        indexOfMin = j
    if indexOfMin != i:
      arr[i], arr[indexOfMin] = arr[indexOfMin], arr[i]