class Heap:
    def __init__(self, items: list[int]):
        self.items = items
        self.size = len(self.items)
        
        # Build min heap
        for i in range(self.size // 2, -1, -1):
            self.__heapify_down(i)
            
    def sort(self):
        """
        Docstring for sort
        
        Sorts the array using heap sort. Since its called after constructor items is already a heap
        """
        # While size of unsorted array is greater than zero
        while self.size - 1 > 0:
            print(f"unsorted size: {self.size} heap before swap -> {self.items}")
            # Swap first item with last item
            self.items[0], self.items[self.size - 1] = self.items[self.size - 1], self.items[0]
            
            print(f"heap after swap -> {self.items}")
            # Decrement unsorted array size
            self.size -= 1
            
            # Heapify
            self.__heapify_down(0)
        
    def get_min(self) -> int:
        assert len(self.items) > 0, "Min Heap is empty"
        root = self.items.pop(0)
        return root
    
    def insert(self, value: int):
        self.items.append(value)
        self.size += 1
        self.__heapify(self.size - 1)
        
        
    def __get_parent(self, child_index: int) -> tuple[int, int]:
        """
        Docstring for __get_parent
        
        :param child_index: index of the child node that we want to get parent for
        :type child_index: int
        :return: The index of parent node and its value
        :rtype: tuple[int, int]
        
        We know that a parent at index p_i that has two children c and d will have the following relationship
        c_i = 2p_i + 1
        d_i = 2p_i + 2
        
        In other words if the index of x of a child of p is odd then its the index of c i.e c_i
        If the index of x of a child of p is even then its the index of d i.e d_i
        
        p_i = (x - 1) / 2, if x is odd
        p_i = (x - 2) / 2, if x is even
        """
        assert child_index > 0, "index of root node has been passed"
        assert self.size - 1 >= child_index, "child_index does not exist in list"
        
        parent_index = 0
        if child_index % 2 == 1:
            parent_index = int((child_index - 1) / 2)
        else:
            parent_index = int((child_index - 2) / 2)
        
        return (parent_index, self.items[parent_index])
    
    def __get_children(self, parent_index: int) -> tuple[int | None, int | None]:
        """
        Docstring for __get_children
        
        parent_index: index of the parent in the array
        We know a node can have two children, a left and a right one
        If i is the index of the parent
        left(i) = 2i + 1
        right(i) = 2i + 2
        
        A node doesn't always have children, we'll know if it doesn't have a child if the index of 
        the possible child is larger than the size of the list i.e.
        
        left(i) = 2i + 1, if self.size > 2i + 1
             = None, if self.size <= 2i + 1        , 0 <= i <= self.size
        right(i) = 2i + 2, if self.size > 2i + 2
              = None, if self.size <= 2i + 2       , 0 <= i <= self.size
        """
        assert parent_index <= self.size - 1, "parent is not in heap"
        
        # Get left child
        left = (2 * parent_index) + 1
        if self.size <= left:
            left = None
            
        right = (2 * parent_index) + 2
        if self.size <= right:
            right = None
            
        return (left, right)
    
    def __heapify_down(self, index: int):
        """
        Docstring for __heapify_down
        
        :param index: Index of the parent that we're checking if nodes meet min heap property
        :type index: int
        """
        print(f"Performing heapify down on {index}")
        assert index < self.size, "node is not in heap"
        
        # Get children of node
        left, right = self.__get_children(index)
        print(f"Node {index} has left child {left} and right child {right}")
        
        # Start by assuming the parent is the smallest when compared to its children
        smallest = index
        
        # If there is a left child, we check if it is smaller than smallest
        if left != None:
            # If smaller we update index of smallest to left
            if self.items[left] < self.items[smallest]:
                smallest = left
        
        # If there is a right child, we check if it is smaller than the smallest
        if right != None:
            # If smaller, we make it the smallest
            if self.items[right] < self.items[smallest]:
                smallest = right
        
        # If smallest is not equal to parent we swap parent with smallest, then run again with smallest
        if smallest != index:
            self.items[smallest], self.items[index] = self.items[index], self.items[smallest]
            self.__heapify_down(smallest)
       
        
        
    def __repr__(self):
        return f'Heap -> {self.items}'
    
heap_1 = Heap([6,5,4,3,2,1])
heap_1.sort()
print(heap_1)