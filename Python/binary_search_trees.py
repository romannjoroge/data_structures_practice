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
                
    def delete(self, value: int): 
        """
        Docstring for delete
        
        :param self: Description
        :param value: the value of the node we are deleting
        :type node: int
        
        A node that we're deleting can fall in one of these 3 cases:
        1. A node with no children
        2. A node with 1 child
        3. A node with 2 children
        
        If a node has no child we can safely delete it i.e. update where it was in its parent to null
        If a node n has 1 child c we can go to its parent p, update where it was (p pointer to n) to that of the child c of the node n
        """
        # The node we're deleting could be the root
        # If it is the root call delete_2_children on root and end
        if self.root.value == value:
            print(f"Value {value} was root {self.root}");
            self.__delete_2_children(self.root)
            return
        
        # If it is not the root we look for the node as we keep track of the parent
        # Set initial parent to root
        parent = self.root
        # Set initial node to None
        node = None
        
        # As we are searching while node = None
        while node == None:
            # If value is less than parent check for node in left child
            if value < parent.value:
                # If there is no left child determine that node is not in tree
                if parent.left == None:
                    raise Exception("node is not in tree")
                # If there is left child check if that is the node we are looking for
                elif parent.left.value == value:
                    # If it is the node set it as node
                    node = parent.left
                # If not set it as parent and repeat
                else:
                    parent = parent.left
            # Else check the node in the right
            else:
                # If there is no right child determine that node is not in tree
                if parent.right == None:
                    raise Exception("node is not in tree")
                # If there is a right child check its value
                elif parent.right.value == value:
                    # If it is the same set node to right child
                    node = parent.right
                # Otherwise make it the parent and repeat
                else:
                    parent = parent.right
        
        # Check if the node has children
        # If it has no children go to the parent and remove it (if less than set less to None in parent otherwise make right None)
        if node.right == None and node.left == None:
            if node < parent:
                parent.left = None
            else:
                parent.right = None
        # If it has one child go to the parent, replace its point to node n to that of the child c (left if node is smaller otherwise right)
        elif (node.right == None and node.left != None):
            if node < parent:
                parent.left = node.left
            else:
                parent.right = node.left
        elif node.right != None and node.left == None:
            if node < parent:
                parent.left = node.right
            else:
                parent.right= node.right
        # If it has 2 children call delete_2_children
        else:
            self.__delete_2_children(node=node)
            
    def preorder(self, node: Node | None):
        """
        Docstring for preorder
        
        :param self: Description
        :param node: node that is being visited
        :type node: Node | None
        
        If node is none it means we are visiting the root
        """
        # Visit the current node (if node is None make it the root)
        if node == None:
            node = self.root
        print(node)
        
        # Traverse the left child
        if node.left:
            self.preorder(node.left)
        
        # Traverse the right child
        if node.right:
            self.preorder(node.right)
            
    def inorder(self, node: Node | None):
        """
        Docstring for inorder
        
        :param self: Description
        :param node: node to start traversal from, if None it is the root
        :type node: Node | None
        """
        # If node is None set it to root
        if node == None:
            node = self.root
        
        # If node has a left child visit it
        if node.left:
            self.inorder(node.left)
        
        # Visit node
        print(node)
        
        # If node has right child visit it
        if node.right:
            self.inorder(node.right)
            
    def postorder(self, node: Node | None):
        """
        Docstring for postorder
        
        :param self: Description
        :param node: node to visit
        :type node: Node | None
        """
        # If node is None set it to root
        if node == None:
            node = self.root
        
        # If node has a left child visit it
        if node.left:
            self.postorder(node.left)
        
        # If node has a right child visit it
        if node.right:
            self.postorder(node.right)
        
        # Visit node
        print(node)
        
    def __delete_2_children(self, node: Node):
        """
        Docstring for __delete_2_children
        
        Helper function for dealing with scenario where we're deleting a node that has 2 children.
        
        :param self: Description
        :param node: Node to delete
        :type node: Node
        """
        # We look for the node in the right subtree with the smallest value
        # Set smallest to right child
        smallest = node.right
        
        # While there is a left child smallest.left
        while smallest.left != None:
            # Update smallest to left
            smallest = smallest.left
        
        # After getting smallest value in right sub tree replace node's value with that of the smallest
        self.delete(smallest.value)
        node.value = smallest.value        
        
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

tree.postorder(None)
        