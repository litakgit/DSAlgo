
class LinkList(object):
    def __init__ (self, data=0, next=None):
        self.data = data
        self.next = next

def get_odd_even_list(L):
    dummy_odd = tail_odd = LinkList()
    dummy_even = tail_even = LinkList()

    tail = [dummy_even, dummy_odd]
    toggle = 0

    while L:
        tail[toggle].next = L
        tail[toggle] = tail[toggle].next
        toggle ^= 1
        L = L.next

    tail[0].next = None
    tail[1].next = None

    return (dummy_even.next, dummy_odd.next)

if __name__ == "__main__":
    L = LinkList(0, LinkList(1, LinkList(2, LinkList(3, LinkList(4, LinkList(5, LinkList(6)))))))
    l1, l2 =get_odd_even_list(L)
