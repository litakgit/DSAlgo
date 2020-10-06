
class BSTNode(object):
    def __init__ (self, data, left=None, right=None):
        self.data = data
        self.left, self.right = left, right

    def __repr__(self):
        return str(self.data) + " left " + str(self.left) + " right " + str(self.right)

def form_tree(inorder, preorder ):
    if not inorder or not preorder:
        return None

    val_to_index_inorder = {node_val : index for index, node_val in enumerate(inorder)}

    transition_index = val_to_index_inorder[preorder[0]]
    return BSTNode(preorder[0],
                    form_tree(inorder[:transition_index], preorder[1:transition_index+1]),
                    form_tree(inorder[transition_index+1:], preorder[transition_index+1:]))

if __name__ == "__main__":
    in_order  = [3, 5, 7, 10, 15, 17, 18, 20, 25, 30, 40]
    pre_order = [17, 10, 5, 3, 7, 15, 30, 20, 18, 25, 40]

    print (form_tree(in_order, pre_order))
