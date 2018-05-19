#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    _set_list_with_single_number = set()
    for element in nums :
        _set_list_with_single_number.add(element)
    return list(_set_list_with_single_number)
  # +++your code here+++

  #HINT: there is such collection like set - set has the feature which You need there - it contains non-repetetive elements.
  #  Please consider this:)
  # Another one method - which is more obvious - is creating another one list in function body and iterate on input list,
  #  and then checking if our new list contains iterator (currently pointed element) or not. Similar to previous one excercises :)

  return

    # _list_without_double = list()
    # for element in nums :
    #     if _list_without_double.__len__() <= nums.__len__()  and element != nums.__iter__().next() :
    #        _list_without_double.append(element)
    # return _list_without_double

# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  # +++your code here+++
  # HINT: iterate on the longer collection (list in this case) and compare elements from both lists.
  # Manipulate indexes (in similar way like below). Try to invent another one solution (different from this below)
  """
  _new_list = []
  _index1 = 0
  _index2 = 0

  while(True):
    if len(_new_list) == len(list1 + list2):
      return _new_list

    if list1[_index1] > list2[_index2]:
       _new_list.append(list2[_index2])
       _index2 += 1
    else:
      _new_list.append(list1[_index1])
      _index1 += 1
  """
  return

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  print 'linear_merge'
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
