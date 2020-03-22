from bst import binary_search_tree
import random
import numpy as np


# I learned from # https://stackoverflow.com/questions/36242046/internal-path-length-of-red-black-tree
def calculate_path_length(node, length_cur=0):
    if node is None:
        return 0
    else:
        return length_cur + calculate_path_length(node.l_child, length_cur + 1) \
               + calculate_path_length(node.r_child, length_cur + 1)


def main():
    trials = 10
    shuffled_tree = binary_search_tree()
    sorted_tree = binary_search_tree()
    for length in range(50, 1000, 50):
        shuffled_lengths = []
        sorted_lengths = []
        for i in range(trials):
            shuffled_values = list(range(length))
            sorted_values = shuffled_values.copy()
            random.shuffle(shuffled_values)
            for val in shuffled_values:
                shuffled_tree.insert_in_tree(val, val)
            for val in sorted_values:
                sorted_tree.insert_in_tree(val, val)
            shuffled_length = calculate_path_length(shuffled_tree.root)
            sorted_length = calculate_path_length(sorted_tree.root)
            shuffled_lengths.append(shuffled_length/length)
            sorted_lengths.append(sorted_length/length)
        print('In a shuffled insertion of', length, 'elements, the average path length of the tree is',
              np.mean(shuffled_lengths))
        print('In a sorted insertion of', length, 'elements, the average path length of the tree is',
              np.mean(sorted_lengths))


if __name__ == '__main__':
    main()
