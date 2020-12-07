'''
There are three types of edits that can be performed on a string: 
  insert a character, 
  remove a character or 
  replace a character. 
Given two strings, check if they are one edit(or zero edit) away. 
e.g. pale, ple -> true(remove a character) 
    pale, pales -> true(add a character) 
    pale, bale -> true(replace a character) 
    pale, bake -> false
''' 

def solution(str1, str2):
  lenDiff = abs(len(str1) - len(str2))
  if lenDiff > 1:
    return False
  
  if lenDiff == 0:
    awayCnt = 0
    for i in range(len(str1)):
      if str1[i] != str2[i]:
        awayCnt += 1
      if awayCnt > 1:
        return False
    return True
  
  if lenDiff == 1:
    longer = str1 if len(str1) > len(str2) else str2
    shorter = str1 if len(str1) < len(str2) else str2
    for i in range(len(shorter)):
      if shorter[i] != longer[i]:
        longer = longer[:i] + longer[i+1:]
    if len(longer) > len(shorter):
      longer = longer[0:len(longer)-1]
    return longer == shorter
