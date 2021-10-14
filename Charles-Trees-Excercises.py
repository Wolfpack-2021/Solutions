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

        def _validation_legwork(n):
            if n.left == None and n.right == None:
                return True
            else:
                if n.left.value > n.value:
                    return False

                elif n.right.value < n.value: 
                    return False

                else:
                    return _validation_legwork(n.left) and _validation_legwork(n.right) 
                    
        return _validation_legwork(self.root)


    def search (self, searched_value):
        
        try: 
            int(searched_value)
        except: 
            print("The provided arguments is not an intenger; this function can only take integers")
            return None
        
        def _search (n, searched_value): 

            if n == None:
                return False
            else:
                if searched_value == n.value:
                    return True

                elif searched_value < n.value:
                    return _search(n.left, searched_value)

                
                elif searched_value >= n.value:
                    return _search(n.right, searched_value)

                
                else:
                    return False
                
        return _search(self.root, searched_value)


#Tree Instnacne Funciton - Can Create a Tree with any root to start; utilising pre-determined adds

def assemble_tree(root_left, root_right, root_value, default = True, node_list = None):
    node_1 = TreeNode(
        left = root_left,
        right = root_right,
        value = root_value
    )
    if default == True:
        tree = Tree(node_1)
        tree.add_node(2) 
        tree.add_node(6)
        tree.add_node(1)
        tree.add_node(3)
        tree.add_node(5)
        tree.add_node(7)
    
    elif default == False:
        for i in node_list:
            tree = Tree(node_1)
            tree.add_node(i)
    

    return tree

assert assemble_tree(None, None, 4).validate() == True
assert assemble_tree(None, None, 4).search(6) == True



