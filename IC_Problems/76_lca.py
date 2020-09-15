
import collections

class TreeNode(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left, self.right = left, right

Status = collections.namedtuple('Status', ('node', 'no_of_nodes'))

def lca(tree, node1, node2):
    if not tree:
        return Status(None, 0)

    left_result = lca(tree.left, node1, node2)
    if left_result.no_of_nodes == 2:
        return left_result

    right_result = lca(tree.right, node1, node2)
    if right_result.no_of_nodes == 2:
        return right_result

    no_of_nodes_under_me = ( left_result.no_of_nodes + right_result.no_of_nodes +
            (node1, node2).count(tree.data) )

    return Status(tree if no_of_nodes_under_me == 2 else None, no_of_nodes_under_me)

if __name__ == "__main__":
    root = TreeNode(30, TreeNode(20, TreeNode(10), TreeNode(25)), TreeNode(40, TreeNode(35), TreeNode(50)))
    print (lca(root, 50, 40).node.data)
