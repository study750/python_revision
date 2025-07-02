class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.child = []
        self.parent = parent

class Tree:
    def __init__(self):
        self.root = None

    def add_child(self, data, parent=None):
        if parent is None:
            n = Node(data, None)
            self.root = n
            return
        
        parent_node = self.find(self.root, parent)
        if parent_node is None:
            print(f"Parent {parent} not found!")
            return
        
        n = Node(data, parent_node)
        parent_node.child.append(n)

    def find(self, current_node, parent_data):
        if current_node is None:
            return None
        
        if current_node.data == parent_data:
            return current_node
        
        for chi in current_node.child:
            found = self.find(chi, parent_data)
            if found:
                return found
        
        return None
        
    def Pri(self, current_node=None, level=0):
        if current_node is None:
            current_node = self.root
        
        if current_node is None:
            return
        
        print(" " * (level * 4) + str(current_node.data) + " ->")
        
        for child in current_node.child:
            self.Pri(child, level + 1)


if __name__ == '__main__':
    tr = Tree()
    tr.add_child(15)        # Root
    tr.add_child(3, 15)     
    tr.add_child(54, 3)
    tr.add_child(5, 15)
    tr.add_child(8, 3)
    
    tr.Pri()  # Print entire tree
