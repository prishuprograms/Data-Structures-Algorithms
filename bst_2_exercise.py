
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
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            max_val = self.left.find_max_recursive()
            self.data = max_val
            self.left = self.left.delete(max_val)
            
        return self

def build_tree(elements):
    print('Original tree : ',elements)

    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    
    # delete_num_val = 35
    numbers_tree.delete(17)
    print ('Tree after deleting :',numbers_tree.in_order_traversal())
    