
class BSTNode(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left, self.right = left, right

def get_root_to_leaf(root):
    def helper(root, buf, buf_index):
        if not root:
            return
        if not root.left and not root.right:
            buf[buf_index] = root.data
            res.append(buf[:buf_index+1].copy())
            return
        buf[buf_index] = root.data
        helper(root.left, buf, buf_index+1)
        helper(root.right, buf, buf_index+1)

    def helper1(root, buf):
        if not root:
            return
        if not root.left and not root.right:
            res.append(buf+[root.data])
            return
        helper1(root.left, buf + [root.data])
        helper1(root.right, buf + [root.data])

    res = []
    buf = [-1] * 10
    #helper(root, buf, 0)
    helper1(root, [])
    return res

if __name__ == "__main__":
    tree = BSTNode(20, BSTNode(10, BSTNode(5), BSTNode(15)), BSTNode(32, BSTNode(31)) )
    print (get_root_to_leaf(tree))
