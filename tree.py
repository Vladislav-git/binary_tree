from binarytree import *
values_1 = [20,16,24,15,22,10,21,None,23,18,None,25]
values_ = [20,16,24,15,22,10,21,23]
values = [20, 16, 24, 12, 18, 22, 28, 8, 16, None, None, 21, 24, 26, None]
root = build(values) #or values_ or values_1

def height(root):  
    if root is None: 
        return 0
    return max(height(root.left), height(root.right)) + 1
  

def isBalanced(root): 
      
 
    if root is None: 
        return True
  
 
    lh = height(root.left) 
    rh = height(root.right) 
  
    # allowed values for (lh - rh) are 1, -1, 0 
    if (abs(lh - rh) < 1) : 
        return True
  
    # if we reach here means tree is not  
    # height-balanced tree 
    return False



lst = []
for node in root:
	if isBalanced(node) == False:
		lst.append(node)
print(root)
print(lst)
