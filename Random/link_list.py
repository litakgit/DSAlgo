import heapq

class LinkList(object):
    def __init__(self, data=0, next=None):
        self.data, self.next = data, next

    def __lt__(self, other):
        return self.data < other.data

def merge_k_sorted_list(A):
    # Get the first elem from each of the list.
    # Extract the min. Put it in a new list.
    # Move to the next elem and add it to the Heap if not None.
    dummy_head = tail = LinkList()
    pq = []

    for a in A:
        if a:
            heapq.heappush(pq, (a.data, a))

    while pq:
        smallest_value, node = heapq.heappop(pq)
        tail.next = node
        tail, node = tail.next, node.next
        if node:
            heapq.heappush(pq, (node.data, node))

    return dummy_head.next

def delete_duplicate(L):
    dummy_head = tail = LinkList()
    it = L

    #import pdb; pdb.set_trace()
    while it:
        next_it = it.next
        while next_it and next_it.data == it.data:
            next_it = next_it.next
        if it.next == next_it:
            tail.next = it
            tail = tail.next
        it = next_it
    tail.next = None
    return dummy_head.next

if __name__ == "__main__":
    #ll = [LinkList(1, LinkList(4, LinkList(7))), LinkList(4, LinkList(6)), LinkList(1)]
    ll = [LinkList(1), LinkList(1)]
    merged_list = merge_k_sorted_list(ll)

    while merged_list:
        #print (merged_list.data)
        merged_list = merged_list.next

    l = delete_duplicate(LinkList(3, LinkList(3, LinkList(7, LinkList(7, LinkList(9))))))
    while l:
        print (l.data)
        l = l.next
