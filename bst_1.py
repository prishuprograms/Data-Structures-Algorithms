import time

class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None  

    def add_child(self,data):
        if data == self.data:
            return
           
        if data < self.data:
            # add in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)         
        else:
            # add in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data) 
        
    def in_order_traversal(self):
        elements = []

        # start with left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # then base node
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
    
        return elements
    
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            # val may be in left tree
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            # val may be in right tree
            if self.right:
                return self.right.search(val)
            else:
                return False


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == "__main__":
    numbers = [12,23,4,6,34,74, 18, 4, 34, 1234,453,345]
    # Can also be used for strings
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(23))
    print(numbers_tree.search(4))

