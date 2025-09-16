class TreeNode:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value

    def insert(self,value):
        if value<self.value:
            if self.left is None:
                self.left=TreeNode(value)
            else:
                self.left.insert(value)
        else: 
            if self.right is None:
                self.right=TreeNode(value)
            else:
                self.right.insert(value)
                
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()
    
    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)
        
    def find_value(self,value):
        if value<self.value:
            if self.left is None:
                return False
            else:
                return self.left.find_value(value)
        elif value>self.value:
            if self.right is None:
                return False
            else:
                return self.right.find_value(value)
        else: 
            return True
        
tree=TreeNode(10)
tree.insert(3)
tree.insert(2)
tree.insert(7)
tree.insert(9)
tree.insert(11)


print(tree.find_value(19))