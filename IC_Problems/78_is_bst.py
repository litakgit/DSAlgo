
class BSTNode(object):
    def __init__ (self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_bst(root):
    def is_bst_helper(node, left_boundary=float('-inf'), right_boundary=float('inf')):
        #import pdb; pdb.set_trace()
        if not node:
            return True
        if node.data > right_boundary or node.data < left_boundary:
            return False
        #left_bst  = is_bst_helper(node.left, left_boundary, node.data)
        #if not left_bst:
        #    return left_bst
        #right_bst = is_bst_helper(node.right, node.data, right_boundary)
        #if not right_bst:
        #    return right_bst

        #return True
        # AND makes sense here! Condition is - if False then I dont need to evaluate anything else;
        # and simply return False. OW evaluate all the expressions.
        return (is_bst_helper(node.left, left_boundary, node.data) and
                is_bst_helper(node.right, node.data, right_boundary))

    return is_bst_helper(root)

if __name__ == "__main__":
    tree = BSTNode(20, BSTNode(10, BSTNode(8), BSTNode(15)), BSTNode(30, BSTNode(25), BSTNode(40)))
    if is_bst(tree):
        print ("I am BST")
    else:
        print ("I am NOT BST")
