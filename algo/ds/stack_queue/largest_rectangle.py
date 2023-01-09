'''
Return the area of the largest rectangle in the histogram.
'''
from algo.ds.stack_queue.stack import Stack

def solution(heights):
  maxArea = 0
  stack = Stack()
  
  for i in range(len(heights)):
    height = heights[i]
    if(stack.isempty() or height >= heights[stack.peek()]):
      stack.push(i)
    else:
      while(not stack.isempty() and heights[stack.peek()] > height):
        top = stack.pop()
        high = i
        low = -1 if stack.isempty() else stack.peek()
        area = heights[top] * (high - low - 1)
        maxArea = max(maxArea, area)
      stack.push(i)
  
  while(not stack.isempty()):
    top = stack.pop()
    high = len(heights)
    low = -1 if stack.isempty() else stack.peek()
    area = heights[top] * (high - low - 1)
    maxArea = max(maxArea, area)

  return maxArea