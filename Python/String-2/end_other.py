# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True
def end_other(a, b):
  # make s1 the shorter string and s2 the longer string and initialize them
  s1 = a.lower()
  s2 = b.lower()
  # check if the assigned values to s1 and s2 actually represent the shorter and longer 
  # string. if not, swap them
  if len(b) < len(a):
    s1, s2 = s2, s1
  
  return s2[len(s2) - len(s1):] == s1