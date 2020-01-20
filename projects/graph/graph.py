"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        elif v1 not in self.vertices:
            self.add_vertex(v1)
            if v1 in self.vertices and v2 in self.vertices:
                self.vertices[v1].add(v2)
        elif v2 not in self.vertices:
            self.add_vertex(v2)
            if v1 in self.vertices and v2 in self.vertices:
                self.vertices[v1].add(v2)


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if self.vertices[vertex_id]:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue
        q = Queue()
        # Create a set to keep track of visited nodes
        visited = set()
        # Create a counter to keep track of the order of the nodes
        counter = 0
        # Add the starting node to the queue
        q.enqueue(starting_vertex)
        # While there are nodes in the queue
        while q.size() > 0:
            # Dequeue them and if not visited, add them to visited and print them
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                counter += 1
                print(F"BFT node #{counter}: {v}")
                # Repeat for the next nodes
                for next_v in self.vertices[v]:
                    q.enqueue(next_v)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Same concept as BFT but using a stack instead of a queue
        s = Stack()
        visited = set()
        counter = 0
        s.push(starting_vertex)
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                counter += 1
                print(F"DFT node #{counter}: {v}")
                for next_v in self.vertices[v]:
                    s.push(next_v)

    def dft_recursive(self, starting_vertex, visited = set(), counter = 0):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Add the starting vertex to the visited set and print it
        visited.add(starting_vertex)
        counter += 1
        print(F"Recur DFT node #{counter}: {starting_vertex}")
        # For each following node, check if it is in visited and if not, recur the function,
        # add it, and print it
        for next_v in self.vertices[starting_vertex]:
            if next_v not in visited:
                self.dft_recursive(next_v, visited, counter)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue and a set to keep track of visited nodes
        q = Queue()
        visited = set()
        # Enqueue the starting node as a list
        q.enqueue([starting_vertex])
        # While there are nodes in the queue
        while q.size() > 0:
            # Create a path variable which is a list of nodes
            path = q.dequeue()
            # path[-1] is the always the last node in the list
            v = path[-1]
            # If the node has not been visited...
            if v not in visited:
                # Check if it's our destination and if so return the path
                if v == destination_vertex:
                    return path
                # Otherwise add it to visited
                visited.add(v)
                # And get the next node
                for next_v in self.vertices[v]:
                    # Create a new path by spreading in the values of the old path
                    # and appending the next node to that list. Then enqueue the new
                    # path for the loop to start again.
                    new_path = [*path]
                    new_path.append(next_v)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Exact same concept as above but using a stack
        s = Stack()
        visited = set()
        s.push([starting_vertex])
        while s.size() > 0:
            path = s.pop()
            v = path[-1]
            if v not in visited:
                if v == destination_vertex:
                    return path
                visited.add(v)
                for next_v in self.vertices[v]:
                    new_path = [*path]
                    new_path.append(next_v)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Create visited set and path list
        visited = set()
        path = []
        # Start by appending the starting vert
        path.append(starting_vertex)
        # The function will return multiple paths, to be stored in valid paths
        valid_paths = []

        def dfs_recur(path, visited):
            v = path[-1]
            # Check if we've reached our destination
            if v == destination_vertex:
                # If so append this new path to valid paths and return
                valid_paths.append(path)
                return
            # If not, add the vert to our visited set and continue the recursion for each neighboring node
            elif v not in visited:
                visited.add(v)
                for next_v in self.vertices[v]:
                    new_path = [*path]
                    new_path.append(next_v)
                    dfs_recur(new_path, visited)
        # Call the function
        dfs_recur(path, visited)
        # Keep track of the shortest path
        shortest_path = valid_paths[0]
        # Loop over the valid paths to find the shortest one
        for path in valid_paths:
            if len(path) < len(shortest_path):
                shortest_path = path
        # Return it
        return shortest_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
