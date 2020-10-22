import pytest

# A binary tree node 
class Node: 
    # Constructor to create a new binary node 
    def __init__(self, key): 
        self.key =  key 
        self.left = None
        self.right = None
  

class TestLCA: 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    root.right.left.right = Node(6)
    root.left.left = Node(7)
    root.left.left.left = Node(8)
    root.right.right.right = Node(9)
    root.right.left.left = Node(10)
    root.left.left.left.left = Node(11)

    def test_base_case(self):
        assert findLCA(self.root, 4, 5) == 3
        assert findLCA(self.root, 4, 6) == 4
        assert findLCA(self.root, 3, 4) == 3
        assert findLCA(self.root, 2, 2) == 2
        assert findLCA(self.root, 6, 5) == 3
    
    def test_node_missing(self):
        assert findLCA(self.root, 10, 12) == -1

    def test_both_nodes_missing(self):
        assert findLCA(self.root, 0,0) == -1
    
    def test_empty_tree(self):
        assert findLCA(None, 0, 0) == -1


def findPath( root, path, k): 

    if root is None: 
        return False
  
    path.append(root.key) 

    if root.key == k : 
        return True

    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))): 
        return True 

    path.pop()
    return False
  
# Returns LCA if node n1 , n2 are present in the given 
# binary tre otherwise return -1 
def findLCA(root, n1, n2): 
  
    # To store paths to n1 and n2 fromthe root 
    path1 = [] 
    path2 = [] 
  
    # Find paths from root to n1 and root to n2. 
    # If either n1 or n2 is not present , return -1  
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)): 
        return -1 
    
    # Compare the paths to get the first different value 
    i = 0 
    while(i < len(path1) and i < len(path2)): 
        if path1[i] != path2[i]: 
            break
        i += 1
    return path1[i-1] 
  
