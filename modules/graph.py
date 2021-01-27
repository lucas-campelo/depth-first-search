from typing import List

class Node:
    def __init__(self, label: str, adj: List[int]):
        self.label = label
        self.adj = adj
        self.parent = self
        self.color = 'w'
        # Clock stuff used by DFS
        self.start = None
        self.end = None

    def __repr__(self):
        return f"<Label: {self.label}, Color: {self.color} Parent: {self.parent.label}, Time: {[self.start, self.end]}>"