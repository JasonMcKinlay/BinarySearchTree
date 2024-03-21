# Jason McKinlay
# Binary Search Tree
# Practice using helper methods

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    """
        >>> my_tree = BinarySearchTree() 
        >>> my_tree.isEmpty()
        True
        >>> my_tree.isBalanced
        True
        >>> my_tree.insert(9) 
        >>> my_tree.insert(5) 
        >>> my_tree.insert(14) 
        >>> my_tree.insert(4)  
        >>> my_tree.insert(6) 
        >>> my_tree.insert(5.5) 
        >>> my_tree.insert(7)   
        >>> my_tree.insert(25) 
        >>> my_tree.insert(23) 
        >>> my_tree.getMin
        4
        >>> my_tree.getMax
        25
        >>> 67 in my_tree
        False
        >>> 5.5 in my_tree
        True
        >>> my_tree.isEmpty()
        False
        >>> my_tree.getHeight(my_tree.root)
        3
        >>> my_tree.getHeight(my_tree.root.left.right)
        1
        >>> my_tree.getHeight(my_tree.root.right)
        2
        >>> my_tree.getHeight(my_tree.root.right.right)
        1
        >>> my_tree.isBalanced
        False
        >>> my_tree.insert(10)
        >>> my_tree.isBalanced
        True
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    

    def isEmpty(self):
        return self.root == None

    @property
    def getMin(self): 
        temp = self.root
        while temp.left != None:
            temp = temp.left
        return temp.value 


    @property
    def getMax(self): 
        temp = self.root
        while temp.right != None:
            temp = temp.right
        return temp.value 


    def __contains__(self,value):
        temp = self.root
        return self.contains_helper(temp, value)

    def contains_helper(self, node, value):
        if node == None:
            return False
        elif value == node.value:
            return True
        elif value < node.value:
            node = node.left
            return self.contains_helper(node, value)
        else:
            node = node.right
            return self.contains_helper(node, value)


    def getHeight(self, node):
        if node == None:
            return -1
        else:
            leftHeight = self.getHeight(node.left)
            rightHeight = self.getHeight(node.right)
            return max(leftHeight, rightHeight) + 1


    @property
    def isBalanced(self):
        return self.isBalanced_helper(self.root)
    
    
    def isBalanced_helper(self, node):
        if node == None:
            return True
        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)
        if abs(leftHeight - rightHeight) <= 1:
            if self.isBalanced_helper(node.left) and self.isBalanced_helper(node.right):
                return True
        return False


def run_tests():
    import doctest
    doctest.testmod(verbose=True)
    
if __name__ == "__main__":
    run_tests()