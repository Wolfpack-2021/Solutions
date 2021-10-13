
        

class TreeNode:
    
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

class Tree:  
    
    def __init__(self, root):
        self.root = root     

    def add_node(self, node) -> None:
        x = self.root
        
        while(True):
            if(node.value > x.value):
                if(x.right != None):
                    x = x.right
                else:
                    x.right = node
                    break
            
                    
            elif(node.value < x.value):
                if(x.left != None):
                    x = x.left
                else:
                    x.left = node
                    break
    
    
    def validate_value(self, value) -> None:
        if value == self.value:
            return True
        elif value < self.value and self.left:
            return self.left.validate_value(value)
        elif value > self.value and self.right:
            return self.right.validate_value(value)
        else:
            return False            

node = TreeNode(None, None, 4)

tree = Tree(node)

tree.add_node(TreeNode(None, None, 4))
tree.add_node(TreeNode(None, None, 2))
tree.add_node(TreeNode(None, None, 6))
tree.add_node(TreeNode(None, None, 1))
tree.add_node(TreeNode(None, None, 3))
tree.add_node(TreeNode(None, None, 5))
tree.add_node(TreeNode(None, None, 7))


tree.validate_value(TreeNode(None, None, 1))
tree.validate_value(TreeNode(None, None, 2))
tree.validate_value(TreeNode(None, None, 3))
tree.validate_value(TreeNode(None, None, 4))
tree.validate_value(TreeNode(None, None, 5))
tree.validate_value(TreeNode(None, None, 6))
tree.validate_value(TreeNode(None, None, 7))
