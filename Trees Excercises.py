#Trees Excercises

#Tree Node
class TreeNode: 
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

#Tree Construction
class Tree:
    def __init__ (self, root):
        self.root = root

    def add_node (self, value):
        node = TreeNode(
            left = None,
            right= None,
            value = value
        )
        n = self.root 

        def _add(node, n):
 
            if node.value > n.value:
                if n.right != None:
                    _add(node, n.right)
                else: 
                    n.right = node 
                    
            elif node.value < n.value: 
                if n.left != None:
                    _add(node, n.left)
                else: 
                    n.left = node

        _add(node, n)

    def validate (self):

        def validation_legwork(n):
            if n.left == None and n.right == None:
                return True
            else:
                if n.left.value > n.value:
                    return False

                elif n.right.value < n.value: 
                    return False

                else:
                    validation_legwork(n.left)
                    validation_legwork(n.right)
                    return True
                    
        return validation_legwork(self.root)


#Node Instance with Actual Value 
node_1 = TreeNode(
    left = None,
    right = None,
    value = 4
)

#Tree Instnacne
tree_1 = Tree(node_1)
tree_1.add_node(2) #appends left of root.
tree_1.add_node(6)
tree_1.add_node(1)
tree_1.add_node(3)
tree_1.add_node(5)
tree_1.add_node(7)

## We should add a an asset and test case.

print (tree_1.validate())