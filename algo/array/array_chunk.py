#  Array Chunk Given an array and chunk size, divide the array into many
#  subarrays where each subarray is of length size. e.g. 
#  chunk([1, 2, 3, 4], 2) -> [[1, 2], [3, 4]] 
#  chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
#  chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
#  chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]] 
#  chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]
def solution(arr, size):
  # chunked = []
  # for i in range(0, len(arr), size):
  #   chunked.append(arr[i:i+size])
  # return chunked
  return [ arr[i:i+size]  for i in range(0, len(arr), size) ]
