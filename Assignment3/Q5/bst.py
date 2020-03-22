# I learned how to implement binary search tree from https://github.com/peterhil/leftrb/blob/master/leftrb
# Part of my code are original from https://www.cs.princeton.edu/~rs/AlgsDS07/09BalancedTrees.pdf and course slides


class binary_search_tree(object):
    root = None

    class Node(object):
        def __init__(self, key, val=None):
            self.key = key
            self.val = val
            self.l_child = None
            self.r_child = None

        def insert(self, key, val=None):
            if self.key == key:
                self.val = val
            elif self.key > key:
                if self.l_child is None:
                    self.l_child = binary_search_tree.Node(key, val)
                else:
                    self.l_child = self.l_child.insert(key, val)
            else:
                if self.r_child is None:
                    self.r_child = binary_search_tree.Node(key, val)
                else:
                    self.r_child = self.r_child.insert(key, val)
            return self

        def search(self, key):
            if self.key == key:
                if self.val is None:
                    return self.key
                else:
                    return self.val
            elif key < self.key and self.l_child:
                return self.l_child.search(key)
            elif key > self.key and self.r_child:
                return self.r_child.search(key)
            else:
                return None

        def find_min(self):
            if self.l_child is None:
                return self
            else:
                return self.l_child.find_min()

        def find_max(self):
            if self.r_child is None:
                return self
            else:
                return self.r_child.find_max()

    def insert_in_tree(self, key, val=None):
        if self.root is None:
            self.root = self.Node(key, val)
        else:
            self.root.insert(key, val)

    def search_in_tree(self, key):
        if self.root is None:
            return None
        else:
            return self.root.search(key)
