# define graph as a adjacency list
test_graph = {
    0: [1, 2, 3],
    1: [0],
    2: [0, 4],
    3: [0],
    4: [2]
}


# implement dfs functionalities
class DepthFirstSearchClass:
    def __init__(self, graph):
        # initialize class variables
        self.target_graph = graph
        self.visited_nodes = []

    def dfs_process(self, start_node):

        # processing nodes list
        stack_nodes = [start_node]

        while stack_nodes:

            # pop a node from stack
            current_node = stack_nodes.pop()

            if current_node not in self.visited_nodes:
                # visit the node
                self.visited_nodes.append(current_node)

                # check neighbor nodes to visited or not and then if not visited add them to the stack list
                for neighbor_node in reversed(self.target_graph[current_node]):
                    if neighbor_node not in self.visited_nodes:
                        stack_nodes.append(neighbor_node)

        # return the final result
        return self.visited_nodes


# initializer dfs class
dfs_class = DepthFirstSearchClass(test_graph)
# call dfs process function
visited_nodes = dfs_class.dfs_process(0)

# print the result
print(f"visited nodes list is : {visited_nodes}")
