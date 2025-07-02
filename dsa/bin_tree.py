class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BT:
    def __init__(self, root):
        self.root = root

    def add_child_left(self, child_data, parent_data):
        parent_node = self.find(self.root, parent_data)
        if parent_node:
            parent_node.left = Node(child_data)
        else:
            print(f"Parent {parent_data} not found!")

    def add_child_right(self, child_data, parent_data):
        parent_node = self.find(self.root, parent_data)
        if parent_node:
            parent_node.right = Node(child_data)
        else:
            print(f"Parent {parent_data} not found!")

    def find(self, current_node, target_data):
        if current_node is None:
            return None
        if current_node.data == target_data:
            return current_node
        
        found = self.find(current_node.left, target_data)
        if found:
            return found
        return self.find(current_node.right, target_data)

    def pri(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return

        print(f"{node.data} -> ", end="")
        if node.left:
            print(f"L:{node.left.data} ", end="")
        if node.right:
            print(f"R:{node.right.data} ", end="")
        print()

        if node.left:
            self.pri(node.left)
        if node.right:
            self.pri(node.right)


if __name__ == "__main__":
    b1 = BT(Node(1))
    b1.add_child_left(2, 1)
    b1.add_child_right(3, 1)
    b1.add_child_left(4, 2)
    b1.add_child_right(5, 2)
    b1.add_child_left(6, 3)
    b1.add_child_right(7, 3)

    b1.pri()
