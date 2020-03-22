# Here I wrote a left-leaning red-black tree
# I learned how to implement red-black tree from https://github.com/peterhil/leftrb/blob/master/leftrb
# Part of my code are original from https://www.cs.princeton.edu/~rs/AlgsDS07/09BalancedTrees.pdf and course slides


RED = True
BLACK = False


# First, I define two functions to judge whether the color of a node is red or black
def is_red(node):
    return isinstance(node, left_red_black_tree.Node) and node.color == RED


def is_black(node):
    return isinstance(node, left_red_black_tree.Node) and node.color == BLACK


class left_red_black_tree(object):
    root = None

    class Node(object):
        def __init__(self, key, val=None):
            self.key = key
            self.val = val
            self.l_child = None
            self.r_child = None
            self.color = BLACK

        def insert(self, key, val=None):
            if self.key == key:
                self.val = val
            elif key < self.key:
                if self.l_child is None:
                    self.l_child = left_red_black_tree.Node(key, val)
                else:
                    self.l_child = self.l_child.insert(key, val)
            else:
                if self.r_child is None:
                    self.r_child = left_red_black_tree.Node(key, val)
                else:
                    self.r_child = self.r_child.insert(key, val)
            if is_red(self.r_child) and is_black(self.l_child):
                self = self.rotate_left()
            if is_red(self.l_child) and is_black(self.r_child):
                self = self.rotate_right()
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

        def fix(self):
            if is_red(self.r_child):
                self = self.rotate_left()
            if is_red(self.l_child) and self.l_child and is_red(self.l_child.l_child):
                self = self.rotate_right()
            if is_red(self.l_child) and is_red(self.r_child):
                self.flip_color()
            return self

        def flip_color(self):
            self.color = not self.color
            self.l_child.color = not self.l_child.color
            self.r_child.color = not self.r_child.color

        def rotate_left(self):
            temp = self.r_child
            self.r_child = temp.l_child
            temp.l_child = self
            temp.color = self.color
            self.color = RED
            return temp

        def rotate_right(self):
            temp = self.l_child
            self.l_child = temp.r_child
            temp.r_child = self
            temp.color = self.color
            self.color = RED
            return temp

        def delete(self, key):
            if self.search(key) is not None:
                if key < self.key:
                    if is_black(self.l_child) and self.l_child and is_black(self.l_child.l_child):
                        self.flip_color()
                        if self.r_child and is_red(self.r_child.l_child):
                            self.r_child = self.r_child.rotate_right()
                            self = self.rotate_left()
                            self.flip_color()
                    self.l_child = self.l_child.delete(key)
                else:
                    if is_red(self.l_child):
                        self = self.rotate_right()
                    if key == self.key and self.r_child is None:
                        return None
                    if is_black(self.r_child) and self.r_child and is_black(self.r_child.l_child):
                        self.flip_color()
                        if self.l_child and is_red(self.l_child.l_child):
                            self = self.rotate_right()
                            self.flip_color()
                    if key == self.key:
                        self.val = self.r_child.search(self.r_child.find_min)
                        self.key = self.r_child.find_min()
                        self.r_child = self.r_child.delete_min()
                    else:
                        self.r_child = self.r_child.delete(key)
                return self.fix()
            else:
                return self

        def delete_min(self):
            if self.l_child is None:
                return None
            if is_black(self.l_child) and self.l_child and is_black(self.l_child.l_child):
                self.flip_color()
                if self.r_child and is_red(self.r_child.l_child):
                    self.r_child = self.r_child.rotate_right()
                    self = self.rotate_left()
                    self.flip_color()
            self.l_child = self.l_child.delete_min()
            return self.fix()

        def delete_max(self):
            if is_red(self.l_child):
                self = self.rotate_right()
            if self.r_child is None:
                return None
            if is_black(self.r_child) and self.r_child and is_black(self.r_child.l_child):
                self.flip_color()
                if self.l_child and is_red(self.l_child.l_child):
                    self = self.rotate_right()
                    self.flip_color()
            self.r_child = self.r_child.delete_max()
            return self.fix()

    def find_min_in_tree(self):
        if self.root is None:
            return None
        else:
            return self.root.find_min()

    def find_max_in_tree(self):
        if self.root is None:
            return None
        else:
            return self.root.find_max()

    def insert_in_tree(self, key, val=None):
        if self.root is None:
            self.root = self.Node(key, val)
        else:
            self.root.insert(key, val)
        self.root.color = BLACK

    def search_in_tree(self, key):
        if self.root is None:
            return None
        else:
            return self.root.search(key)

    def delete_in_tree(self, key):
        if self.root is not None:
            self.root = self.root.delete(key)
            if self.root is not None:
                self.root.color = BLACK
        else:
            return self

    def delete_min_in_tree(self):
        self.root.delete_min()
        self.root.color = BLACK

    def delete_max_in_tree(self):
        self.root.delete_max()
        self.root.color = BLACK
