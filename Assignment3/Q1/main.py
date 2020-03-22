from llrbt import left_red_black_tree


class symbol_table:
    tree = left_red_black_tree()

    def insert_in_st(self, key, val=None):
        self.tree.insert_in_tree(key, val)

    def delete_in_st(self, key):
        self.tree.delete_in_tree(key)

    def search_in_st(self, key):
        return self.tree.search_in_tree(key)

    def st_is_empty(self):
        if self.tree.root is None:
            return True
        else:
            return False


def main():
    keys = ['T', 'H', 'I', 'S', 'I', 'S', 'A', 'N', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    st = symbol_table()
    for key, val in zip(keys, values):
        st.insert_in_st(key, val)
    print(st.search_in_st('S'))
    print(st.search_in_st('A'))
    print(st.search_in_st('E'))
    st.delete_in_st('X')
    print(st.search_in_st('X'))
    st.insert_in_st('X', 20)
    print(st.search_in_st('X'))


if __name__ == '__main__':
    main()
