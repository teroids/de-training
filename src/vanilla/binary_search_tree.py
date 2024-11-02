class Node:
    def __init__(self, val, left=None, right=None, father=None):
        self.val = val
        self.left = left
        self.right = right
        self.father = father
    
class Tree:
    def __init__(self, root: None = None):
        self.root = root

    def insert(self, val):
        node = self.root
        father = node
        while node:
            father = node
            if val < node.val:
                node = node.left
                if not node:
                    father.left = Node(val, father=father)
            else:
                node = node.right
                if not node:
                    father.right = Node(val, father=father)
    @staticmethod
    def inorder(root):
        # Visits left -> root -> right
        if not root:
            return 
        Tree.inorder(root.left)
        print(root.val, end=" ")
        Tree.inorder(root.right)
        return
    
    @staticmethod
    def preorder(root):
        # Visits root -> left -> right
        if not root:
            return
        print(root.val, end=" ")
        Tree.preorder(root.left)
        Tree.preorder(root.right)
        return

    @staticmethod
    def postorder(root):
        # Visits Left -> Right -> Root
        if not root:
            return
        Tree.postorder(root.left)
        Tree.postorder(root.right)
        print(root.val, end=" ")
        return

    @staticmethod
    def level_order_traversal(root):
        stack = [root]
        result = []
        while stack:
            node = stack.pop(0)
            print(node.val, end="")
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result
    
    @staticmethod
    def search(root, val):
        node = root
        while node:
            if node.val == val:
                return True
            elif val < node.val:
                node = node.left
            else:
                node = node.right
        return False

tree = Tree(Node(1))
tree.insert(3)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
Tree.inorder(root)
print("----")
Tree.preorder(root)
print("----")
Tree.postorder(root)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
r = Tree.level_order_traversal(root)


root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

# Searching for keys in the BST
print("Found" if Tree.search(root, 19) else "Not Found")
print("Found" if Tree.search(root, 80) else "Not Found")
print("Found" if Tree.search(root, 40) else "Not Found")
print("Found" if Tree.search(root, 31) else "Not Found")
print("Found" if Tree.search(root, 60) else "Not Found")