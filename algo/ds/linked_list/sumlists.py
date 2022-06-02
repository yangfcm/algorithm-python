'''
  Given two number represented by a linked list, where each node contains a single digit.

  The digits are stored in reverse order, such that the 1's digit is at the head of the list
  Write a function that adds the two numbers and returns the sum as a linked list
  e.g. (7 -> 1 -> 6) + (5 -> 9 -> 2) => 617+295 = 912 => 2 -> 1 -> 9
  Then suppose the digits are stored in forward order. Repeat the above problem
  e.g. (6 -> 1 -> 7) + (2 -> 9 -> 5) => 617+295 = 912 => 9 -> 1 -> 2
  To implement it, either use linked list with double direction or reverse list and use the same implementation as below.
  Do not convert to number.
'''
from algo.ds.linked_list.linkedlist import LinkedList

def solution(list1 = LinkedList(), list2 = LinkedList()):
  sumList = LinkedList()
  list1Size = list1.size()
  list2Size = list2.size()
  maxSize = list1Size if list1Size > list2Size else list2Size

  node1 = list1.getfirst()
  node2 = list2.getfirst()

  for i in range(maxSize):
    digit1 = node1.data if node1 != None else 0
    digit2 = node2.data if node2 != None else 0
    
    lastNode = sumList.getlast()
    lastDigit = lastNode.data if lastNode != None else 0
    sumList.removelast()
    
    digitSum = digit1 + digit2 + lastDigit
    sumList.insertlast(digitSum % 10)
    sumList.insertlast(digitSum // 10)

    if node1 != None: node1 = node1.next
    if node2 != None: node2 = node2.next
  
  return sumList
