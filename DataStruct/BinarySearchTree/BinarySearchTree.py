# when balanced, a search is O(log(n)), but it could be O(n) if no balanced.

from collections import deque

class TNode:
    def __init__(self, v=0, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r


class BTree:
    def __init__(self, v):
        self.root = TNode(v)

    def insert(self, v):
        p, n = self.find_node(v)

        if v > n.v:
            n.r = TNode(v)
        else:
            n.l = TNode(v)

    def bfs(self):
        q1 = deque()
        q1.append(self.root)

        q2 = deque()

        q = q1
        cq = q2
        while q:
            n = q.popleft()
            print(n.v, end=',')
            if n.l:
                cq.append(n.l)
            if n.r:
                cq.append(n.r)

            if not q and cq:
                print('')
                q, cq = cq, q

    # when you want to manipulate the return node
    # it is helpful to get the parent as well
    def find_node(self, v):
        parent = None
        n = self.root
        while True:
            if v > n.v:
                if n.r:
                    parent = n
                    n = n.r
                else:
                    break
            else:
                if n.l:
                    parent = n
                    n = n.l
                else:
                    break
        return (parent, n)

    def search(self, v):
        p, n = self.find_node(v)

        if n.v == v:
            return True

        return False

    def get_min(self):
        n = self.root
        while n.l:
            n = n.l
        return n.v

    def get_max(self):
        n = self.root
        while n.r:
            n = n.r
        return n.v

    @staticmethod
    def find_node_without_left(n):
        parent = None
        p = n
        while p.l:
            parent = p
            p = p.l
        return parent, p

    @staticmethod
    def replace_child(p, v, n):
        replaced = True
        if p.l and p.l.v == v:
            p.l = n
        elif p.r and p.r.v == v:
            p.r = n
        else:
            replaced = False

        return replaced

    def delete(self, v):
        n_delete = None
        parent = None
        if v == self.root.v:
            n_delete = self.root
        else:
            parent, _ = self.find_node(v)
            if parent.l and parent.l.v == v:
                n_delete = parent.l
            elif parent.r and parent.r.v == v:
                n_delete = parent.r
            else:
                # nothing to delete
                return

        if not n_delete.l and not n_delete.r:
            if parent:
                self.replace_child(parent, v, None)
            else:
                self.root = None
                return
        elif not n_delete.l:
            if parent:
                self.replace_child(parent, v, n_delete.r)
            else:
                self.root = n_delete.r
        elif not n_delete.r:
            if parent:
                self.replace_child(parent, v, n_delete.r)
            else:
                self.root = n_delete.l
        else:
            # n_delete has two child

            # from the right child of n_delete, find a child without left child
            p, n = BTree.find_node_without_left(n_delete.r)
            if parent:
                n_delete.v = v
            else:
                self.root.v = n.v

            if not n.r:
                self.replace_child(p, n.v, None)
            else:
                self.replace_child(p, n.v, n.r)


if __name__ == '__main__':
    btree = BTree(10)
    btree.insert(2)

    btree.insert(1)
    btree.insert(3)
    btree.insert(60)
    btree.insert(5)
    btree.insert(15)

    p, n = btree.find_node(15)

    btree.bfs()
    print(btree.search(60))
    print(btree.search(30))
    print(btree.search(1))
    print(btree.get_min())
    print(btree.get_max())

    btree.delete(5)
    btree.bfs()
    btree.delete(10)
    btree.bfs()