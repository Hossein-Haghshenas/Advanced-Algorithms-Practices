# implementing multi pop process & amortized analysis
class Stack:
    def __init__(self):
        self.stack = []
        self.cost = 0
        self.total_operations = 0

    def push(self, value):
        self.stack.append(value)
        self.cost += 1  # each push have O(1) credit
        self.total_operations += 1

    def multipush(self, values):
        for value in values:
            self.push(value)  # use push for each elements
        self.cost += len(values)  # the credit of O(k) for each multi push

    def calculate_amortized_cost(self):
        return self.cost / self.total_operations if self.total_operations > 0 else 0


# use stack class for adding elements
s = Stack()
s.push(5)
s.multipush([1, 2, 3, 4])  # MULTIPUSH

# calculate cost of amortized
print("Amortized Cost:", s.calculate_amortized_cost())
