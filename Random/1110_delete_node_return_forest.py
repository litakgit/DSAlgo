import collections

class TreeNode(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left, self.right = left, right

    def __repr__(self):
        return str(self.data) + " " + str(self.left) + " " + str(self.right)

gpos = 0

def delete_nodes_to_make_forests(root, delete_nodes):
    def update_forests(nd, pos):
        if nd and nd.data in delete_nodes and pos not in forest:
            return
        forest[pos].append(nd.data if nd and nd.data not in delete_nodes else None)

    def build_forests(node, pos):
        global gpos
        update_forests(node, pos)
        if not node:
            return
        for nei in (node.left, node.right):
            if node.data in delete_nodes:
                if nei:
                    gpos += 1
                    build_forests(nei, gpos)
            else:
                build_forests(nei, pos)

    forest = collections.defaultdict(list)
    build_forests(root, gpos)

    print (forest.keys())
    for key in forest:
        print (forest[key])

if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(8, TreeNode(9), TreeNode(10)), TreeNode(12))), TreeNode(3, TreeNode(6), TreeNode(7)))
    print (tree)
    delete_nodes_to_make_forests(tree, [1, 5])
    #delete_nodes_to_make_forests(tree, [12])
