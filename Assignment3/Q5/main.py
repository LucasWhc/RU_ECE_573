from bst import binary_search_tree


def in_order(node, key_list):
    if node is None:
        return -1
    in_order(node.l_child, key_list)
    key_list.append(node.key)
    in_order(node.r_child, key_list)


def rank(node, key):
    key_list = []
    in_order(node, key_list)
    return key_list.index(key)


def select(node, k):
    key_list = []
    in_order(node, key_list)
    return key_list[k]


def main():
    tree = binary_search_tree()
    file = open('select-data.txt')
    lines = file.readlines()
    for line in lines:
        line = int(line)
        tree.insert_in_tree(line)
    ans1 = select(tree.root, 7)
    ans2 = rank(tree.root, 7)
    print('select(7) in the given tree is', ans1)
    print('rank(7) in the given tree is', ans2)


if __name__ == '__main__':
    main()
