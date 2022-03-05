# Do we need a heap?

# The heap can help to do the sort of the first ele of the sorted lists
from heapq import heappush
from heapq import heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # this can allow heappush/heappop to compare directly
    #def __lt__(self, other):
    #    return self.val < other.val


def merge_lists(lists):
    k = len(lists)

    heap = []
    for i in range(k):
        heappush(heap, (lists[i].val, lists[i]))

    dummy = ListNode()
    cur = dummy

    while len(heap) > 0:
        tup = heappop(heap)
        node = tup[1]
        cur.next = node
        if node.next:
            heappush(heap, (node.next.val, node.next))
        cur = node

    return dummy.next


def convert(root):
    ret = []
    node = root
    while node:
        ret.append(node.val)
        node = node.next
    return ret


if __name__ == '__main__':
    root1 = ListNode(1)
    root1.next = ListNode(4)
    root1.next.next = ListNode(7)
    root1.next.next.next = ListNode(10)
    root1.next.next.next.next = ListNode(13)

    root2 = ListNode(2)
    root2.next = ListNode(5)
    root2.next.next = ListNode(8)
    root2.next.next.next = ListNode(11)
    root2.next.next.next.next = ListNode(14)

    root3 = ListNode(3)
    root3.next = ListNode(6)
    root3.next.next = ListNode(9)
    root3.next.next.next = ListNode(12)
    root3.next.next.next.next = ListNode(15)

    ret = merge_lists([root1, root2, root3])

    print(convert(ret))
