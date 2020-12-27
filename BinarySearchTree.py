class TreeNode():
    def __init__(self,key=None):
        self.key = key
        self.left=None
        self.right=None
        self.parent=None



class BinarySearchTree():
    def __init__(self):
        self.root=None

    def minimum_of_subtree(self,root_node):
        curr=root_node
        while(curr.left is not None):
            curr=curr.left

        return(curr)

    def maximum_of_subtree(self,root_node):
        curr = root_node
        while (curr.right is not None):
            curr = curr.right

        return (curr)

    def inorder(self):
        self.print_inorder(self.root)
        print()

    def print_inorder(self, node):
        if node is not None:
            self.print_inorder(node.left)
            print(node.key,end = " ")
            self.print_inorder(node.right)

    def insert_many(self, element_list):
        for element in element_list:
            self.insert(element)


    def insert(self,element):

        new_node = TreeNode(key=element)

        # Finding proper place for new node
        if self.root is None:
            self.root = new_node
        else:
            parent=self.root
            child=self.root
            while child is not None:
                parent=child
                if(new_node.key < child.key):
                    child=child.left
                else:
                    child=child.right

            # Setting new node's parent value
            new_node.parent=parent

            # Setting parent's child value
            if(new_node.key < parent.key):
                parent.left = new_node
            else:
                parent.right = new_node

    def search(self, element):
        curr = self.root

        while curr is not None:
            if element < curr.key:
                curr = curr.left
            elif element > curr.key:
                curr = curr.right
            else:
                return(True)

        return(False)

    def transplant(self, node_rem, node_put):
        # Transplantation used for deletion
        # Refer to CLRS
        if node_rem.parent is None:
            self.root = node_put
        elif node_rem.parent.left is node_rem:
            node_rem.parent.left = node_put
        else:
            node_rem.parent.right = node_put

        if node_put is not None:
            node_put.parent = node_rem.parent

    def delete(self, element):
        # 3 cases - Node to be deleted is leaf, has one child, has both children

        if not self.search(element):
            return

        # Get element
        curr = self.root
        while curr.key != element:
            if element < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        if curr.left is None:
            self.transplant(curr, curr.right)
        elif curr.right is None:
            self.transplant(curr, curr.left)
        else:
            successor = self.minimum_of_subtree(curr.right)
            if successor.parent != curr:
                self.transplant(successor, successor.right)
                successor.right = curr.right
                successor.right.parent = successor

            self.transplant(curr, successor)
            successor.left = curr.left
            successor.left.parent = successor

    def successor(self,element):
        # Finds successor of the element in the BST
        # element itself may not exist in BST

        successor=None
        parent = self.root
        curr=self.root

        while(curr is not None and element != curr.key):
            parent = curr
            if element < curr.key:
                curr=curr.left
            else:
                curr=curr.right

        # if curr is not None:
        #     print("Found the node in the tree")

        if curr is not None and curr.right is not None:
            return self.minimum_of_subtree(curr.right).key

        elif curr is None and parent.key > element:
            return parent.key

        else:
            # Normalising to the same case
            if curr is None:
                curr = parent
                parent = parent.parent

            while parent is not None and parent is not self.root and parent.right == curr:
                curr = curr.parent
                parent = parent.parent

            if parent is self.root and parent.right == curr:
                return None
            else:
                return parent.key

    def predecessor(self,element):
        # Finds predecessor of the element in the BST
        # element itself may not exist in BST

        parent = self.root
        curr=self.root

        while(curr is not None and element != curr.key):
            parent = curr
            if element < curr.key:
                curr=curr.left
            else:
                curr=curr.right

        # if curr is not None:
        #     print("Found the node in the tree")

        if curr is not None and curr.left is not None:
            return self.maximum_of_subtree(curr.left).key

        elif curr is None and parent.key < element:
            return parent.key

        else:
            # Normalising to the same case
            if curr is None:
                # print("curr parent is", parent)
                curr = parent
                parent = parent.parent

            while parent is not self.root and parent.left == curr:
                curr = curr.parent
                parent = parent.parent

            if parent is self.root and parent.left == curr:
                return None
            else:
                return parent.key



# example
bst = BinarySearchTree()
bst.insert_many([50, 36, 24, 105, 340, 243, 245, 15, 23, 22, 137])
bst.inorder()
print()

print("Successors")
print(bst.successor(50))
print(bst.successor(340))
print(bst.successor(15))
print(bst.successor(16))
print()

print("Predecessors")
print(bst.predecessor(50))
print(bst.predecessor(340))
print(bst.predecessor(15))
print(bst.predecessor(16))
print(bst.predecessor(22))
print(bst.predecessor(21))
print(bst.predecessor(28))
print()

print("Delete")
bst.inorder()
bst.delete(50)
bst.inorder()
bst.delete(24)
bst.inorder()


