'''
  Luck Balance: There is an array to represent a series of contests.
  Each element(contest) is also an array which has two integer numbers.
  The first number is the luck point; the second is 1 or 0 to indicate if the contest is important or not.
  The rule is if you lose the contest, you can earn the luck point; if you win the contest, you will lose the luck point.
  You cannot lose more than k important contests.
  Given k and contests arrays, work out the maximum luck points you can earn.

  Example: k = 3, contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]] -> 29
  There are 6 contests, 4 of which are important and you cannot lost more than k=3 of them.
  You can get the maximum luck balance by losing all unimportant contests(index = 4, 5) and the first, second and fourth(index = 0, 1, 3) important contests.
  So the total luck balance is 5 + 2 - 1 + 8 + 10 + 5 = 29.
'''
def solution(contests, k):
  contests.sort(key=lambda x: x[0]) # Sort the contests list by point(the first element in each list element)
  reverseSorted = contests[::-1]
  maxLuck = 0
  importantLost = 0

  for c in reverseSorted:
    if c[1] == 0: # If it's an unimportant contest (c[1] == 0), then you can lose it as many as you want
      maxLuck += c[0]
    else: # If it's an important contest...
      if importantLost < k: # You can lose it
        maxLuck += c[0]
        importantLost += 1
      else: # Now, you've already lost k important contests, you can't lose it any more.
        maxLuck -= c[0]
  
  return maxLuck