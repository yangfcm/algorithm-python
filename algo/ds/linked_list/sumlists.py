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

def solution(list1 = LinkedList, list2 = LinkedList()):
  pass