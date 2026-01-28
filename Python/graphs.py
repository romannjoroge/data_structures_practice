class Graph():
    def __init__(self):
        self.adjacency_list = {
            1: [5, 4, 2],
            2: [7, 6, 3, 1],
            3: [2],
            4: [1],
            5: [1],
            6: [2],
            7: [2]
        }
        
    def breadth_first_search(self, first_node: int):
        """
        Docstring for breadth_first_search
        
        :param self: Description
        :param first_node: The node to start traversal from
        :type first_node: int
        """
        # Have a queue for managing nodes to visit
        queue = []
        # Have a list to store visited nodes
        visited_nodes = []
        
        # Put first node in queue
        queue.append(first_node)
        
        # while there are nodes to visit (queue not empty)
        while len(queue) > 0:
            # Remove first item from queue
            first = queue.pop(0)
            # Visit and add to visited list
            print(first)
            visited_nodes.append(first)
            
            # For all of first's neighbours
            for neighbour in self.adjacency_list[first]:
                # Check if has been visited
                if neighbour not in visited_nodes:
                    # If not visited add them to end of queue
                    queue.append(neighbour)
                    
        
graph = Graph()
graph.breadth_first_search(1)