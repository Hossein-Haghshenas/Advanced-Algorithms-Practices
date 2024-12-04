# define test graphs as a adjacency list
test_graph_1 = {
    0: [1, 2, 3],
    1: [0],
    2: [0, 4],
    3: [0],
    4: [2]
}

test_graph_2 = {
    1: [2, 4],
    2: [5],
    3: [5, 6],
    4: [2],
    5: [4],
    6: [6]
}

test_graph_3 = {
    "s": ["r", "u", "v"],
    "r": ["s", "t", "w"],
    "u": ["s", "t", "y"],
    "v": ["s", "w", "y"],
    "t": ["u", "r"],
    "w": ["r", "v", "x", "z"],
    "y": ["u", "v", "x"],
    "x": ["w", "z"],
    "z": ["w", "x"],
}

test_graph_4 = {
    "s": ["v"],
    "v": ["w"],
    "w": ["s"],
    "q": ["s", "w", "t"],
    "t": ["x", "y"],
    "x": ["z"],
    "y": ["q"],
    "z": ["x"],
    "r": ["u", "y"],
    "u": ["y"],
}

test_graph_5 = {
    0: [1, 2],
    1: [3],
    2: [3, 4],
    3: [5],
    4: [5],
    5: []
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


def search_on_graph(graph, start_node, print_text):
    # initializer dfs class
    dfs_class = DepthFirstSearchClass(graph)
    # call dfs process function
    visited_nodes = dfs_class.dfs_process(start_node)

    # print the result
    print(f"{print_text} : {visited_nodes}")


search_on_graph(test_graph_1, 0, 'visited nodes list for graph test-1 is')
print("-------------------------------------------------------------------")
search_on_graph(test_graph_2, 1, 'visited nodes list for graph test-2 is')
print("-------------------------------------------------------------------")
search_on_graph(test_graph_3, 's', 'visited nodes list for graph test-3 is')
print("-------------------------------------------------------------------")
search_on_graph(test_graph_4, 's', 'visited nodes list for graph test-4 is')
print("-------------------------------------------------------------------")
search_on_graph(test_graph_5, 0, 'visited nodes list for graph test-5 is')
