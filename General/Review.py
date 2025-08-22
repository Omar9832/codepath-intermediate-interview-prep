from collections import deque 

def is_anagram(s, t):
    dict1={}
    dict2={}
    for x in s:
        if x not in dict1:
            dict1[x]=1
        else:
            dict1[x]+=1
    for y in t:
        if y not in dict2:
            dict2[y]=1
        else:
            dict2[y]+=1
    
    
    return dict1==dict2


print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))


class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def tree_diameter(root):
    result=[]
    def helper(root, result):
        if not root:
            return 0
        if not root.left and root.right:
            return 0
        
        if root.right and root.right.val not in result:
            result.append(root.right.val)
        elif root.left and root.left.val not in result:
            result.append(root.left.val)


        helper(root.left, result)
        helper(root.right, result)
    helper(root, result)
    
    return len(result)+1


# Using build_tree() function included at top of page
tree_1 = build_tree([1, 2, 3, 4, 5])
print(tree_diameter(tree_1))

"""
   1
  /
 2
"""
tree_2 = build_tree([1, 2])
print(tree_diameter(tree_2))

tree_3 = build_tree([1, 2, None, 3, None, 4])
print(tree_diameter(tree_3))


def can_attend_meetings(intervals):
    for x in intervals:
        for y in intervals:
            if x[0]<y[0] and y[1]<x[1]:
                return False
    return True

intervals_1 = [[0,30],[5,10],[15,20]]
intervals_2 = [[7,10],[2,4]]

print(can_attend_meetings(intervals_1))
print(can_attend_meetings(intervals_2))