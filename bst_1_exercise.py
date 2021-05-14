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

    def pre_order_traversal(self):
        elements = [self.data]
        # elements.append(self.data)
        
        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()

        # elements = [self.data]
        elements.append(self.data)
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
    def find_max(self):
        max_num = max(self.in_order_traversal())
        return max_num

    def find_min(self):
        min_num = min(self.in_order_traversal())
        return min_num

    def find_max_recursive(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max_recursive()

    def find_min_recursive(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min_recursive()

    def calculate_sum(self):
        sum_num = sum(self.in_order_traversal())
        return sum_num
    
    def calculate_sum_recursive(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return left_sum + right_sum + self.data

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == "__main__":
    numbers = [12,23,4,6,34,74, 18, 4, 34, 1234,453,12323,345]
    # Can also be used for strings
    numbers_tree = build_tree(numbers)
    print('In-order-transversal ==>',numbers_tree.in_order_traversal())
    print('Pre-order-transversal ==>',numbers_tree.pre_order_traversal())
    print('Post-order-transversal ==>',numbers_tree.post_order_traversal())
    print("Max_num ==>", numbers_tree.find_max())
    print("Max_num_recursive ==>", numbers_tree.find_max_recursive())
    print("Min_num ==>", numbers_tree.find_min())
    print("Min_num_recursive ==>", numbers_tree.find_min_recursive())
    print("Sum of numbers ==>", numbers_tree.calculate_sum())
    print("Sum of numbers using recursion ==>", numbers_tree.calculate_sum_recursive())
    print(numbers_tree.search(23))
    print(numbers_tree.search(0))

