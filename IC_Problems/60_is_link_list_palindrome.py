
"""
    In a while loop of iterating over linklist, don't miss the increment operation.
"""

class LinkList(object):
    def __init__ (self, data=0, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data) + " -> " + str(self.next)

def is_palindrome(node):
    def reverse(nd):
        prev, cur = None, nd
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

    slow, fast = node, node
    prev_slow = None
    while fast and fast.next:
        prev_slow = slow
        slow, fast = slow.next, fast.next.next

    if not prev_slow:
        return True
    prev_slow.next = None
    first_half = node
    second_half = reverse(slow)

    while first_half and second_half:
        if first_half.data != second_half.data:
            return False
        first_half, second_half = first_half.next, second_half.next

    return True

if __name__ == "__main__":
    ll = LinkList(1, LinkList(1))
    print (ll)
    print (is_palindrome(ll))
    print (ll)
