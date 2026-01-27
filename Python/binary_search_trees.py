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
            else:
                raise "new node is smaller than existing left can't insert it here"
            
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
            else:
                raise "new node is greater than right node, should not be assigned here"
        
            
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

root = Node(10)
root.assign_right(Node(15))
root.assign_right(Node(11))

print(f"root node is {root} and its right child is {root.right} and its right child is {root.right.right}")