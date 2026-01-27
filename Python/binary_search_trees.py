class Node():
    def __init__(self, value: int):
        self.value = value
        self.right = None
        self.left = None
        
    def assign_left(self, node: "Node"):
        """
        Docstring for assign_left
        
        :param node: Node to insert as left child
        :type node: Node
        
        a node could either have a left child or not have a left child
        if there is no left child just make it the left child
        if there is already a left child, place the new node as left child then
        make the previous node the left child (if previous was already less and not the same value)
        """
        assert node < self, "left child should be less than parent"
        if self.left == None:
            self.left = node
        else:
            if node > self.left:
                previous_left = self.left
                self.left = node
                self.left.assign_left(previous_left)
            elif node == self.left:
                pass
            else:
                self.left.assign_left(node=node)
            
    def assign_right(self, node: "Node"):
        """
        Docstring for assign_right
        
        :param node: Node to insert as right child
        :type node: Node
        
        a node could either have a right child or not have one
        if it doesn't have a right child make it the right child
        if it does have the right child and the new node is less than the old one make it the
        new right child and make the previous one the right child of the new node
        """
        assert node > self, "right child should be greater than parent"
        if self.right == None:
            self.right = node
        else:
            if node < self.right:
                previous_right = self.right
                self.right = node
                self.right.assign_right(previous_right)
            elif node == self.right:
                pass
            else:
                self.right.assign_right(node=node)
        
            
    def __repr__(self):
        return str(self.value)
    
    def __lt__(self, other):
        if isinstance(other, Node):
            return self.value < other.value
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Node):
            return self.value > other.value
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value
        elif other == None:
            return False
        return NotImplemented

class BinarySearchTree():
    def __init__(self, root: Node):
        self.root = root
        
    def insert(self, node: Node):
        """
        Docstring for insert
        
        :param self: Description
        :param node: node to insert to tree
        :type node: Node
        
        The place for the node is looked for in the tree. If the value is less than root insert it in left
        otherwise insert it as right
        """
        if node < self.root:
            self.root.assign_left(node=node)
        elif node > self.root:
            self.root.assign_right(node=node)
        else:
            print(f"node {node} is same as root {self.root}")
            pass
        
    def search(self, num: int) -> bool:
        """
        Docstring for search
        Checks if an item is in tree
        
        :param self: Description
        :param num: Number to search for in binary search tree
        :type num: int
        """
        # We start search at tree
        node_to_consider = self.root
        
        while True:
            # If root is equal to value return true
            if node_to_consider.value == num:
                return True
            
            # Otherwise if it is greater look at the right child, if no right child return False
            elif num > node_to_consider.value:
                if node_to_consider.right:
                    node_to_consider = node_to_consider.right
                else:
                    return False
             # If it is less look at the left child, if no left child return false
            else:
                if node_to_consider.left:
                    node_to_consider = node_to_consider.left
                else:
                    return False
        
    def __repr__(self):
        tree_string = ""
        nodes = [self.root]
        while len(nodes) > 0:
            node_to_print = nodes.pop(0)
            tree_string += f"node is {node_to_print}, its left child is {node_to_print.left} and its right is {node_to_print.right}\n"
            if node_to_print.right:
                nodes.append(node_to_print.right)
            if node_to_print.left:
                nodes.append(node_to_print.left)
                
        return tree_string
    
tree = BinarySearchTree(root=Node(100))
tree.insert(Node(50))
tree.insert(Node(70))
tree.insert(Node(110))
tree.insert(Node(200))
print(tree)
print(tree.search(200))
        