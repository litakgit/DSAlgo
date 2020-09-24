
class LinkList(object):
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data) + " " + str(self.next)

class BSTNode(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left, self.right = left, right

    def __repr__(self):
        return str(self.data) + " " + str(self.left) + " " + str(self.right)

def form_node(L):
    s = LinkList(0, L)
    f = L
    while f and f.next:
        s, f = s.next, f.next.next
    node = s.next
    s.next = None
    # Consider the case when there is only one node in the list.
    return (L if L != node else None, node.data, node.next)

def build_bst_from_sorteed_list(L):
    if not L:
        return None
    left_bst_list, node_data, right_bst_list = form_node(L)
    return BSTNode( node_data,
                    build_bst_from_sorteed_list(left_bst_list),
                    build_bst_from_sorteed_list(right_bst_list))

if __name__ == "__main__":
    L = LinkList(1, LinkList(2, LinkList(3, LinkList(4))))
    print (L)
    tree = build_bst_from_sorteed_list(L)
    print (tree)
