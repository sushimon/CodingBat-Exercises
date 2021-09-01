# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks
# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True
def make_bricks(small, big, goal):
  if small + 5 * big < goal:
    return False
  else:
    # find how many 5 inch bricks are needed
    rem = goal // 5
    if rem <= big:
      # if there are more 5 inch bricks than needed, check if the remaining 1 
      # inch bricks can meet the length requirement
      return small >= goal - rem * 5
    else:
      # if there are less 5 inch bricks than needed, subtract all the 1 inch bricks
      # from the length requirement. if the difference is less than the total length of
      # 5 inch bricks, then you know we can meet the requirement because you can simply
      # remove a certain number of 1 inch bricks and insert a 5 inch brick instead
      # e.g. make_bricks(43, 1, 46)
      # following this logic, the difference would be 3 inches remaining but since we
      # have one 5 inch brick that we haven't used, we can take away two 1 inch bricks
      # and place the 5 inch brick instead (41 + 5 = 46)
      return goal - small <= 5 * big